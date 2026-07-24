#pragma once

#include <cstddef>
#include <vector>

// struct 表示“只有数据，没有复杂行为”的记录。
struct Vector3 {
    double x{};
    double y{};
    double z{};
};

struct Sample {
    double time_seconds{};
    Vector3 position;
};

struct TimedVector {
    double time_seconds{};
    Vector3 value;
    double magnitude{};
};

struct Statistics {
    double mean{};
    double variance{};
};

struct VectorStatistics {
    Statistics x;
    Statistics y;
    Statistics z;
    Statistics magnitude;
};

struct AnalysisResult {
    std::vector<TimedVector> velocities;
    std::vector<TimedVector> accelerations;
    VectorStatistics velocity_statistics;
    VectorStatistics acceleration_statistics;
};
