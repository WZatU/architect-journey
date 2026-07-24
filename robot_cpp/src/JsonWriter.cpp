#include "JsonWriter.hpp"

#include <fstream>
#include <iomanip>
#include <stdexcept>

namespace {

std::string escapeJsonString(const std::string& text) {
    std::string escaped;
    for (const char character : text) {
        if (character == '\\' || character == '"') {
            escaped.push_back('\\');
        }
        escaped.push_back(character);
    }
    return escaped;
}

void writeStatistics(std::ostream& output, const VectorStatistics& statistics) {
    output << "{\n"
           << "      \"x\": {\"mean\": " << statistics.x.mean
           << ", \"variance\": " << statistics.x.variance << "},\n"
           << "      \"y\": {\"mean\": " << statistics.y.mean
           << ", \"variance\": " << statistics.y.variance << "},\n"
           << "      \"z\": {\"mean\": " << statistics.z.mean
           << ", \"variance\": " << statistics.z.variance << "},\n"
           << "      \"magnitude\": {\"mean\": " << statistics.magnitude.mean
           << ", \"variance\": " << statistics.magnitude.variance << "}\n"
           << "    }";
}

void writeRecords(std::ostream& output, const std::vector<TimedVector>& records) {
    output << "[\n";
    for (std::size_t i = 0; i < records.size(); ++i) {
        const TimedVector& record = records[i];
        output << "      {\"time\": " << record.time_seconds
               << ", \"x\": " << record.value.x
               << ", \"y\": " << record.value.y
               << ", \"z\": " << record.value.z
               << ", \"magnitude\": " << record.magnitude << "}";
        if (i + 1 < records.size()) {
            output << ',';
        }
        output << '\n';
    }
    output << "    ]";
}

} // namespace

void JsonWriter::write(
    const std::string& filename,
    const std::string& source_csv,
    std::size_t sample_count,
    const AnalysisResult& result,
    double elapsed_milliseconds
) const {
    std::ofstream output(filename);
    if (!output.is_open()) {
        throw std::runtime_error("Cannot open JSON output file: " + filename);
    }
    output << std::setprecision(15);
    output << "{\n"
           << "  \"source\": \"" << escapeJsonString(source_csv) << "\",\n"
           << "  \"sample_count\": " << sample_count << ",\n"
           << "  \"elapsed_milliseconds\": " << elapsed_milliseconds << ",\n"
           << "  \"variance_type\": \"population\",\n"
           << "  \"velocity\": {\n"
           << "    \"records\": ";
    writeRecords(output, result.velocities);
    output << ",\n    \"statistics\": ";
    writeStatistics(output, result.velocity_statistics);
    output << "\n  },\n"
           << "  \"acceleration\": {\n"
           << "    \"records\": ";
    writeRecords(output, result.accelerations);
    output << ",\n    \"statistics\": ";
    writeStatistics(output, result.acceleration_statistics);
    output << "\n  }\n}\n";
}
