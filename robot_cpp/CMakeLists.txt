cmake_minimum_required(VERSION 3.16)
project(robot_test_tools VERSION 1.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

add_library(robot_core
    src/CsvReader.cpp
    src/RobotAnalyzer.cpp
    src/JsonWriter.cpp
)
target_include_directories(robot_core PUBLIC include)
target_compile_options(robot_core PRIVATE -Wall -Wextra -Wpedantic)

add_executable(read_robot_csv apps/read_robot_csv.cpp)
target_link_libraries(read_robot_csv PRIVATE robot_core)

add_executable(analyze_robot_csv apps/analyze_robot_csv.cpp)
target_link_libraries(analyze_robot_csv PRIVATE robot_core)

add_executable(export_robot_json apps/export_robot_json.cpp)
target_link_libraries(export_robot_json PRIVATE robot_core)

enable_testing()
add_executable(robot_tests tests/robot_tests.cpp)
target_link_libraries(robot_tests PRIVATE robot_core)
target_compile_definitions(robot_tests PRIVATE
    TEST_DATA_DIR="${CMAKE_CURRENT_SOURCE_DIR}/tests/data"
)
add_test(NAME robot_tests COMMAND robot_tests)
