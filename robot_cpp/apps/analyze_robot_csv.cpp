#include "CsvReader.hpp"
#include "RobotAnalyzer.hpp"
#include "Stopwatch.hpp"

#include <exception>
#include <iostream>

void printStatistics(const char* name, const VectorStatistics& statistics) {
    std::cout << name << " statistics (mean, population variance)\n"
              << "  x: " << statistics.x.mean << ", " << statistics.x.variance << '\n'
              << "  y: " << statistics.y.mean << ", " << statistics.y.variance << '\n'
              << "  z: " << statistics.z.mean << ", " << statistics.z.variance << '\n'
              << "  magnitude: " << statistics.magnitude.mean << ", "
              << statistics.magnitude.variance << '\n';
}

int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cerr << "Usage: analyze_robot_csv <input.csv>\n";
        return 1;
    }

    try {
        Stopwatch stopwatch;
        CsvReader reader;
        RobotAnalyzer analyzer;
        const std::vector<Sample> samples = reader.read(argv[1]);
        const AnalysisResult result = analyzer.analyze(samples);

        std::cout << "Velocity records: " << result.velocities.size() << '\n'
                  << "Acceleration records: " << result.accelerations.size() << '\n';
        printStatistics("Velocity", result.velocity_statistics);
        printStatistics("Acceleration", result.acceleration_statistics);
        std::cout << "Elapsed: " << stopwatch.elapsedMilliseconds() << " ms\n";
    } catch (const std::exception& error) {
        std::cerr << "Error: " << error.what() << '\n';
        return 1;
    }
    return 0;
}
