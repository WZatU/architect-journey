#pragma once

#include "RobotTypes.hpp"

#include <string>

class JsonWriter {
public:
    void write(
        const std::string& filename,
        const std::string& source_csv,
        std::size_t sample_count,
        const AnalysisResult& result,
        double elapsed_milliseconds
    ) const;
};
