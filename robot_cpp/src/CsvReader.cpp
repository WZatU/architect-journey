#include "CsvReader.hpp"

#include <fstream>
#include <sstream>
#include <stdexcept>

namespace {

std::vector<std::string> splitCsvLine(const std::string& line) {
    std::vector<std::string> cells;
    std::stringstream stream(line);
    std::string cell;

    while (std::getline(stream, cell, ',')) {
        if (!cell.empty() && cell.back() == '\r') {
            cell.pop_back();
        }
        cells.push_back(cell);
    }
    return cells;
}

double parseNumber(const std::string& text, std::size_t line_number) {
    try {
        std::size_t parsed_characters = 0;
        const double value = std::stod(text, &parsed_characters);
        if (parsed_characters != text.size()) {
            throw std::invalid_argument("extra characters");
        }
        return value;
    } catch (const std::exception&) {
        throw std::runtime_error(
            "CSV line " + std::to_string(line_number) +
            " contains a non-numeric value: '" + text + "'"
        );
    }
}

} // namespace

std::vector<Sample> CsvReader::read(const std::string& filename) const {
    std::ifstream input(filename);
    if (!input.is_open()) {
        throw std::runtime_error("Cannot open CSV file: " + filename);
    }

    std::string line;
    if (!std::getline(input, line)) {
        throw std::runtime_error("CSV file is empty: " + filename);
    }

    const auto header = splitCsvLine(line);
    if (header != std::vector<std::string>{"time", "x", "y", "z"}) {
        throw std::runtime_error("CSV header must be exactly: time,x,y,z");
    }

    std::vector<Sample> samples;
    std::size_t line_number = 1;
    while (std::getline(input, line)) {
        ++line_number;
        if (line.empty()) {
            continue;
        }

        const auto cells = splitCsvLine(line);
        if (cells.size() != 4) {
            throw std::runtime_error(
                "CSV line " + std::to_string(line_number) +
                " must contain exactly 4 columns"
            );
        }

        samples.push_back({
            parseNumber(cells[0], line_number),
            {
                parseNumber(cells[1], line_number),
                parseNumber(cells[2], line_number),
                parseNumber(cells[3], line_number)
            }
        });
    }

    if (samples.empty()) {
        throw std::runtime_error("CSV contains no data rows");
    }
    return samples;
}
