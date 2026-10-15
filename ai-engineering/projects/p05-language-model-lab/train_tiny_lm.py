"""Independent toy byte-level LM starter; not a Stanford assignment solution.

Requires PyTorch, separately installed for the learner's CPU/GPU platform. This
environment did not have PyTorch; runtime results must be recorded after running.
"""
import argparse
import hashlib
import json
import math
from pathlib import Path
import platform

import torch
from torch import nn
from torch.nn import functional as F

ROOT = Path(__file__).resolve().parents[2]


class TinyLM(nn.Module):
    def __init__(self, width=64, context=64):
        super().__init__()
        self.tokens = nn.Embedding(256, width)
        self.positions = nn.Embedding(context, width)
        layer = nn.TransformerEncoderLayer(width, 4, width*2, dropout=0.0,
                                           batch_first=True, norm_first=True)
        self.transformer = nn.TransformerEncoder(layer, 2, enable_nested_tensor=False)
        self.head = nn.Linear(width, 256)

    def forward(self, tokens):
        length = tokens.size(1)
        hidden = self.tokens(tokens) + self.positions(torch.arange(length, device=tokens.device))
        mask = nn.Transformer.generate_square_subsequent_mask(length, device=tokens.device)
        return self.head(self.transformer(hidden, mask=mask, is_causal=True))


def make_batch(corpus, context, batch=8):
    positions = torch.randint(0, len(corpus)-context, (batch,))
    x = torch.stack([corpus[i:i+context] for i in positions])
    y = torch.stack([corpus[i+1:i+context+1] for i in positions])
    return x, y


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--steps', type=int, default=20, help='additional optimizer steps')
    parser.add_argument('--seed', type=int, default=17)
    parser.add_argument('--resume', type=Path)
    parser.add_argument('--output', type=Path, default=Path('outputs/p05-smoke.pt'))
    args = parser.parse_args()
    if not 1 <= args.steps <= 10000:
        parser.error('steps must be in [1,10000]')
    torch.set_num_threads(1)
    torch.manual_seed(args.seed)
    config = {'width':64,'context':64,'batch':8,'lr':0.001,'seed':args.seed}
    documents = json.loads((ROOT/'data/documents.json').read_text())
    # Separate documents before tokenization. Private and retired fixtures excluded.
    eligible = [row for row in documents if row['tenant']=='public' and not row.get('valid_until')]
    train_ids = [row['id'] for row in eligible[:-2]]
    val_ids = [row['id'] for row in eligible[-2:]]
    train_bytes = '\n'.join(row['text'] for row in eligible[:-2]).encode()
    val_bytes = '\n'.join(row['text'] for row in eligible[-2:]).encode()
    data_hash = hashlib.sha256(train_bytes + b'\x00' + val_bytes).hexdigest()
    train = torch.tensor(list(train_bytes),dtype=torch.long)
    val = torch.tensor(list(val_bytes),dtype=torch.long)
    if min(len(train),len(val)) <= config['context']:
        raise ValueError('corpus too short')
    model = TinyLM(config['width'],config['context'])
    optimizer = torch.optim.AdamW(model.parameters(),lr=config['lr'])
    start_step = 0
    if args.resume:
        saved = torch.load(args.resume,map_location='cpu',weights_only=True)
        if saved['config'] != config or saved['data_hash'] != data_hash:
            raise ValueError('checkpoint config or data mismatch')
        model.load_state_dict(saved['model'])
        optimizer.load_state_dict(saved['optimizer'])
        torch.set_rng_state(saved['rng'])
        start_step = saved['step']
    model.train()
    last_loss = None
    for _ in range(args.steps):
        x,y = make_batch(train,config['context'],config['batch'])
        optimizer.zero_grad(set_to_none=True)
        logits = model(x)
        loss = F.cross_entropy(logits.flatten(0,1),y.flatten())
        if not torch.isfinite(loss):
            raise RuntimeError('non-finite loss')
        loss.backward()
        nn.utils.clip_grad_norm_(model.parameters(),1.0)
        optimizer.step()
        last_loss = float(loss.detach())
    # Preserve training RNG before validation so resumed sampling stays comparable.
    training_rng = torch.get_rng_state()
    model.eval()
    with torch.no_grad():
        x,y = make_batch(val,config['context'],config['batch'])
        val_loss = float(F.cross_entropy(model(x).flatten(0,1),y.flatten()))
    report = {'measurement_origin':'measured_toy_cpu_training','scope':'smoke test only',
              'step':start_step+args.steps,'train_loss_last':last_loss,'validation_loss':val_loss,
              'parameters':sum(p.numel() for p in model.parameters()),'data_hash':data_hash,
              'train_document_ids':train_ids,'validation_document_ids':val_ids,
              'python':platform.python_version(),'torch':str(torch.__version__),'device':'cpu'}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    torch.save({'config':config,'data_hash':data_hash,'model':model.state_dict(),
                'optimizer':optimizer.state_dict(),'rng':training_rng,'step':report['step']},args.output)
    args.output.with_suffix('.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report))


if __name__ == '__main__':
    main()
