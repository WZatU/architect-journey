#pragma once

#include "RobotTypes.hpp"

#include <vector>

class RobotAnalyzer {
public:
    AnalysisResult analyze(const std::vector<Sample>& samples) const;

    static Statistics calculateStatistics(const std::vector<double>& values);

private:
    static std::vector<TimedVector> calculateVelocities(
        const std::vector<Sample>& samples
    );
    static std::vector<TimedVector> calculateAccelerations(
        const std::vector<TimedVector>& velocities
    );
    static VectorStatistics calculateVectorStatistics(
        const std::vector<TimedVector>& records
    );
};
