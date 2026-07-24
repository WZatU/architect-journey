#include "CsvReader.hpp"
#include "RobotAnalyzer.hpp"

#include <cmath>
#include <exception>
#include <iostream>
#include <stdexcept>
#include <string>

namespace {

int failures = 0;

void expectNear(double actual, double expected, const std::string& message) {
    constexpr double tolerance = 1e-9;
    if (std::abs(actual - expected) > tolerance) {
        std::cerr << "FAIL: " << message << "; expected " << expected
                  << ", got " << actual << '\n';
        ++failures;
    }
}

void expectEqual(std::size_t actual, std::size_t expected, const std::string& message) {
    if (actual != expected) {
        std::cerr << "FAIL: " << message << "; expected " << expected
                  << ", got " << actual << '\n';
        ++failures;
    }
}

void testCsvReader() {
    CsvReader reader;
    const auto samples = reader.read(std::string(TEST_DATA_DIR) + "/known_motion.csv");
    expectEqual(samples.size(), 4, "reader gets four rows");
    expectNear(samples[2].time_seconds, 2.0, "third sample time");
    expectNear(samples[2].position.x, 4.0, "third sample x position");
}

void testRobotAnalyzer() {
    const std::vector<Sample> samples{
        {0.0, {0.0, 0.0, 0.0}},
        {1.0, {1.0, 0.0, 0.0}},
        {2.0, {4.0, 0.0, 0.0}},
        {3.0, {9.0, 0.0, 0.0}}
    };
    RobotAnalyzer analyzer;
    const AnalysisResult result = analyzer.analyze(samples);

    expectEqual(result.velocities.size(), 3, "four positions make three velocities");
    expectEqual(result.accelerations.size(), 2, "three velocities make two accelerations");
    expectNear(result.velocities[0].value.x, 1.0, "first x velocity");
    expectNear(result.velocities[1].value.x, 3.0, "second x velocity");
    expectNear(result.velocities[2].value.x, 5.0, "third x velocity");
    expectNear(result.velocity_statistics.x.mean, 3.0, "velocity x mean");
    expectNear(result.velocity_statistics.x.variance, 8.0 / 3.0, "velocity x variance");
    expectNear(result.accelerations[0].value.x, 2.0, "first x acceleration");
    expectNear(result.acceleration_statistics.x.mean, 2.0, "acceleration x mean");
    expectNear(result.acceleration_statistics.x.variance, 0.0, "acceleration x variance");
}

void testInvalidTimeIsRejected() {
    const std::vector<Sample> samples{
        {0.0, {0.0, 0.0, 0.0}},
        {0.0, {1.0, 0.0, 0.0}},
        {1.0, {2.0, 0.0, 0.0}}
    };
    try {
        RobotAnalyzer analyzer;
        (void)analyzer.analyze(samples);
        std::cerr << "FAIL: duplicate time should throw an exception\n";
        ++failures;
    } catch (const std::runtime_error&) {
        // Expected path.
    }
}

} // namespace

int main() {
    testCsvReader();
    testRobotAnalyzer();
    testInvalidTimeIsRejected();

    if (failures != 0) {
        std::cerr << failures << " test(s) failed\n";
        return 1;
    }
    std::cout << "All tests passed\n";
    return 0;
}
