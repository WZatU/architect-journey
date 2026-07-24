#pragma once

#include "RobotTypes.hpp"

#include <string>
#include <vector>

// class 表示“拥有一种明确行为的对象”。
class CsvReader {
public:
    std::vector<Sample> read(const std::string& filename) const;
};
