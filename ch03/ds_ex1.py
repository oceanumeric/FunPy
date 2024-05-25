import timeit
import pathlib
from loguru import logger
from typing import TextIO, List


def line_sort_key(line: str) -> str:
    # set the fourth word as the key
    words = line.split()
    if len(words) >= 4:
        return words[3]
    else:
        # use a sentinel value to keep the short lines at the end
        return '\uffff'

if __name__ == "__main__":
    file_path = pathlib.Path('../data/apple.txt')
    with open(file_path, 'r') as f:
        # read all lines
        lines = f.readlines()
        lines = [line.strip() for line in lines]
    
    logger.info(f"Original lines")
    print('\n'.join(lines))
    logger.info("Sort lines by default")
    lines.sort()
    print('\n'.join(lines))
    logger.info("Sort lines by length")
    lines.sort(key=lambda x: len(x), reverse=True)
    print('\n'.join(lines))
    logger.info("Sort lines by the fourth word")
    start_time = timeit.default_timer()
    lines.sort(key=line_sort_key)
    logger.success(f"Time: {timeit.default_timer() - start_time}")
    print('\n'.join(lines))
    
    # use tuple as the key
    start_time = timeit.default_timer()
    
    transformed_line = [
        (line.split()[3], line) if len(line.split()) >= 4 else ('\uffff', line)
        for line in lines
    ]
    
    # sort the transformed lines
    transformed_line.sort()
    logger.success(f"Time: {timeit.default_timer() - start_time}")
    print('\n'.join([line for _, line in transformed_line]))
    
    # test the performance of the two methods for a long text
    file_path = pathlib.Path('../data/sort_long_text.txt')
    with open(file_path, 'r') as f:
        # read all lines
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        
    start_time = timeit.default_timer()
    lines.sort(key=line_sort_key)
    logger.success(f"Time: {timeit.default_timer() - start_time}")
    
    start_time = timeit.default_timer()
    transformed_line = [
        (line.split()[3], line) if len(line.split()) >= 4 else ('\uffff', line)
        for line in lines
    ]
    transformed_line.sort()
    logger.success(f"Time: {timeit.default_timer() - start_time}")