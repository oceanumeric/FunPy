import time
from pathlib import Path
from typing import Dict, Any, Iterator, TypeVar, TextIO

# Simulate a log file with streaming data
def simulate_log_file(file_path: Path) -> None:
    with open(file_path, 'w') as file:
        for i in range(1, 101):
            file.write(f"Log entry {i}: Something happened.\n")
            file.flush()
            time.sleep(0.1)  # Simulate time delay for streaming data
            

def read_log_file(file_path: Path) -> Iterator[str]:
    with open(file_path, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            yield line.strip()


if __name__ == "__main__":
    file_path = Path("log.txt")
    simulate_log_file(file_path)
    for line in read_log_file(file_path):
        print(line)