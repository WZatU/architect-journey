# Robot CSV tools (C++17)

Three command-line programs share one core library:

- `read_robot_csv`: read and validate `time,x,y,z` CSV data.
- `analyze_robot_csv`: calculate velocity, acceleration, mean, and population variance.
- `export_robot_json`: run the complete pipeline and write JSON.

## Build and test

```bash
cmake -S . -B build
cmake --build build
ctest --test-dir build --output-on-failure
```

## Run

```bash
./build/read_robot_csv tests/data/known_motion.csv
./build/analyze_robot_csv tests/data/known_motion.csv
./build/export_robot_json tests/data/known_motion.csv result.json
```

CSV format:

```csv
time,x,y,z
0,0,0,0
1,1,0,0
2,4,0,0
```
