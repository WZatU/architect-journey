"""Check coverage, dependencies and local references; not learner mastery."""
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]


def validate():
    points = json.loads((ROOT/'curriculum/knowledge-map.json').read_text())
    lessons = json.loads((ROOT/'curriculum/curriculum.json').read_text())['lessons']
    assert len(points) == 200 and [row['id'] for row in points] == list(range(1,201))
    assert len(lessons) == 24 and len({row['id'] for row in lessons}) == 24
    by_id = {row['id']:row for row in lessons}
    assert {row['project'] for row in lessons} == {f'P{i:02}' for i in range(1,7)}
    for row in points:
        lesson = by_id[row['primary_lesson']]
        assert lesson['project'] == row['primary_project']
        assert row['id'] in lesson['knowledge_ids']
        assert row['learner_status'] in {'not_started','in_progress','completed_with_evidence'}
        if row['learner_status'] == 'completed_with_evidence':
            assert row.get('learner_evidence'), f"missing learner evidence: {row['id']}"
    active, done = set(), set()

    def visit(key):
        assert key not in active, f'cyclic lesson dependency: {key}'
        if key in done:
            return
        active.add(key)
        for parent in by_id[key]['prerequisites']:
            visit(parent)
        active.remove(key)
        done.add(key)

    for key in by_id:
        visit(key)
    for row in lessons:
        assert (ROOT/row['path']).is_file(), row['path']
        assert row['tasks'] and row['acceptance'] and row['sources']
    broken = []
    checked = 0
    # Existing repository paths outside this new subtree are reviewed separately
    # against the base Git tree and are intentionally not required for this check.
    for doc in ROOT.rglob('*.md'):
        if any(part in {'.venv','__pycache__','outputs'} for part in doc.parts):
            continue
        for target in re.findall(r'(?<!!)\[[^\]]*\]\(([^)]+)\)', doc.read_text()):
            if target.startswith(('https://','http://','mailto:','#')):
                continue
            path = unquote(target.split('#',1)[0])
            resolved = (doc.parent/path).resolve()
            if not resolved.is_relative_to(ROOT):
                continue
            checked += 1
            if not resolved.exists():
                broken.append(f'{doc.relative_to(ROOT)} -> {target}')
    assert not broken, '\n'.join(broken)
    return {'knowledge_points':len(points),'lessons':len(lessons),'projects':6,
            'local_links_checked':checked,'acyclic_prerequisites':True,
            'meaning':'structure and coverage index validated; learner mastery not evaluated'}


if __name__ == '__main__':
    print(json.dumps(validate(), ensure_ascii=False))
