#include "RobotAnalyzer.hpp"

#include <cmath>
#include <stdexcept>

namespace {

double magnitude(const Vector3& vector) {
    return std::sqrt(
        vector.x * vector.x +
        vector.y * vector.y +
        vector.z * vector.z
    );
}

} // namespace

AnalysisResult RobotAnalyzer::analyze(const std::vector<Sample>& samples) const {
    if (samples.size() < 3) {
        throw std::runtime_error(
            "At least 3 position samples are required to calculate acceleration"
        );
    }

    AnalysisResult result;
    result.velocities = calculateVelocities(samples);
    result.accelerations = calculateAccelerations(result.velocities);
    result.velocity_statistics = calculateVectorStatistics(result.velocities);
    result.acceleration_statistics = calculateVectorStatistics(result.accelerations);
    return result;
}

std::vector<TimedVector> RobotAnalyzer::calculateVelocities(
    const std::vector<Sample>& samples
) {
    std::vector<TimedVector> velocities;
    velocities.reserve(samples.size() - 1);

    for (std::size_t i = 0; i + 1 < samples.size(); ++i) {
        const Sample& current = samples[i];
        const Sample& next = samples[i + 1];
        const double dt = next.time_seconds - current.time_seconds;
        if (dt <= 0.0) {
            throw std::runtime_error("Sample times must be strictly increasing");
        }

        const Vector3 velocity{
            (next.position.x - current.position.x) / dt,
            (next.position.y - current.position.y) / dt,
            (next.position.z - current.position.z) / dt
        };
        velocities.push_back({
            (current.time_seconds + next.time_seconds) / 2.0,
            velocity,
            magnitude(velocity)
        });
    }
    return velocities;
}

std::vector<TimedVector> RobotAnalyzer::calculateAccelerations(
    const std::vector<TimedVector>& velocities
) {
    std::vector<TimedVector> accelerations;
    accelerations.reserve(velocities.size() - 1);

    for (std::size_t i = 0; i + 1 < velocities.size(); ++i) {
        const TimedVector& current = velocities[i];
        const TimedVector& next = velocities[i + 1];
        const double dt = next.time_seconds - current.time_seconds;

        const Vector3 acceleration{
            (next.value.x - current.value.x) / dt,
            (next.value.y - current.value.y) / dt,
            (next.value.z - current.value.z) / dt
        };
        accelerations.push_back({
            (current.time_seconds + next.time_seconds) / 2.0,
            acceleration,
            magnitude(acceleration)
        });
    }
    return accelerations;
}

Statistics RobotAnalyzer::calculateStatistics(const std::vector<double>& values) {
    if (values.empty()) {
        throw std::runtime_error("Cannot calculate statistics for empty data");
    }

    double sum = 0.0;
    for (const double value : values) {
        sum += value;
    }
    const double mean = sum / static_cast<double>(values.size());

    double squared_difference_sum = 0.0;
    for (const double value : values) {
        const double difference = value - mean;
        squared_difference_sum += difference * difference;
    }
    const double variance =
        squared_difference_sum / static_cast<double>(values.size());
    return {mean, variance};
}

VectorStatistics RobotAnalyzer::calculateVectorStatistics(
    const std::vector<TimedVector>& records
) {
    std::vector<double> x_values;
    std::vector<double> y_values;
    std::vector<double> z_values;
    std::vector<double> magnitudes;
    x_values.reserve(records.size());
    y_values.reserve(records.size());
    z_values.reserve(records.size());
    magnitudes.reserve(records.size());

    for (const TimedVector& record : records) {
        x_values.push_back(record.value.x);
        y_values.push_back(record.value.y);
        z_values.push_back(record.value.z);
        magnitudes.push_back(record.magnitude);
    }

    return {
        calculateStatistics(x_values),
        calculateStatistics(y_values),
        calculateStatistics(z_values),
        calculateStatistics(magnitudes)
    };
}
