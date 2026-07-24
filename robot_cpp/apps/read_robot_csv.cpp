#include "CsvReader.hpp"
#include "Stopwatch.hpp"

#include <exception>
#include <iostream>

int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cerr << "Usage: read_robot_csv <input.csv>\n";
        return 1;
    }

    try {
        Stopwatch stopwatch;
        CsvReader reader;
        const std::vector<Sample> samples = reader.read(argv[1]);

        std::cout << "Read " << samples.size() << " samples\n"
                  << "First time: " << samples.front().time_seconds << " s\n"
                  << "Last time: " << samples.back().time_seconds << " s\n"
                  << "Elapsed: " << stopwatch.elapsedMilliseconds() << " ms\n";
    } catch (const std::exception& error) {
        std::cerr << "Error: " << error.what() << '\n';
        return 1;
    }
    return 0;
}
