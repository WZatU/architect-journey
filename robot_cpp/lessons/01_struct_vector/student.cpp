#include <cmath>
#include <iostream>
#include <vector>

// 第 1 关：struct 表示一条机器人位置记录。
struct Sample {
    double time_seconds;
    double x;
};

// TODO 1：返回三个样本：
// time=0, x=0
// time=1, x=2
// time=2, x=6
std::vector<Sample> makeSamples() {
    return {}; // 请修改这一行
}

// TODO 2：返回所有 x 的平均值。
// 提示：先遍历 samples 求和，再除以 samples.size()。
double calculateMeanX(const std::vector<Sample>& samples) {
    (void)samples; // 完成函数后删掉这一行
    return 0.0;    // 请修改这里
}

// TODO 3：返回最后时刻减去最初时刻。
double calculateDuration(const std::vector<Sample>& samples) {
    (void)samples; // 完成函数后删掉这一行
    return 0.0;    // 请修改这里
}

// 下面是自动检查代码。第一关暂时不需要修改。
bool near(double actual, double expected) {
    return std::abs(actual - expected) < 1e-9;
}

int main() {
    const std::vector<Sample> samples = makeSamples();
    int failures = 0;

    if (samples.size() != 3) {
        std::cerr << "FAIL: 应该生成 3 个样本，实际是 "
                  << samples.size() << " 个\n";
        ++failures;
    }

    if (samples.size() == 3) {
        if (!near(samples[0].time_seconds, 0.0) || !near(samples[0].x, 0.0) ||
            !near(samples[1].time_seconds, 1.0) || !near(samples[1].x, 2.0) ||
            !near(samples[2].time_seconds, 2.0) || !near(samples[2].x, 6.0)) {
            std::cerr << "FAIL: 三个样本的 time 或 x 不正确\n";
            ++failures;
        }

        const double mean_x = calculateMeanX(samples);
        if (!near(mean_x, 8.0 / 3.0)) {
            std::cerr << "FAIL: x 均值应为 " << 8.0 / 3.0
                      << "，实际是 " << mean_x << '\n';
            ++failures;
        }

        const double duration = calculateDuration(samples);
        if (!near(duration, 2.0)) {
            std::cerr << "FAIL: 总时长应为 2，实际是 "
                      << duration << '\n';
            ++failures;
        }
    }

    if (failures != 0) {
        std::cerr << "尚有 " << failures << " 项未通过，请继续修改。\n";
        return 1;
    }

    std::cout << "PASS: 第一关全部通过！\n"
              << "样本数量: " << samples.size() << '\n'
              << "x 均值: " << calculateMeanX(samples) << '\n'
              << "总时长: " << calculateDuration(samples) << " 秒\n";
    return 0;
}
