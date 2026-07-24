#include "CsvReader.hpp"
#include "JsonWriter.hpp"
#include "RobotAnalyzer.hpp"
#include "Stopwatch.hpp"

#include <exception>
#include <iostream>

int main(int argc, char* argv[]) {
    if (argc != 3) {
        std::cerr << "Usage: export_robot_json <input.csv> <output.json>\n";
        return 1;
    }

    try {
        Stopwatch stopwatch;
        CsvReader reader;
        RobotAnalyzer analyzer;
        JsonWriter writer;

        const std::vector<Sample> samples = reader.read(argv[1]);
        const AnalysisResult result = analyzer.analyze(samples);
        writer.write(
            argv[2], argv[1], samples.size(), result,
            stopwatch.elapsedMilliseconds()
        );
        std::cout << "Wrote " << argv[2] << '\n';
    } catch (const std::exception& error) {
        std::cerr << "Error: " << error.what() << '\n';
        return 1;
    }
    return 0;
}
