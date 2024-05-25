import csv
from loguru import logger
from pathlib import Path
from typing import TextIO, cast, TypeVar
from collections.abc import Iterator, Iterable


def row_iter(source: TextIO) -> Iterator[list[str]]:
    return csv.reader(source, delimiter="\t")


def head_split_fixed(row_iter: Iterator[list[str]]) -> Iterator[list[str]]:
    title = next(row_iter)
    assert len(title) == 1 and title[0] == "Anscombe's quartet"
    heading = next(row_iter)
    assert len(heading) == 4 and heading == ["I", "II", "III", "IV"]
    columns = next(row_iter)
    assert len(columns) == 8 and columns == ["x", "y", "x", "y", "x", "y", "x", "y"]

    return row_iter


def get_rows(path: Path) -> Iterable[list[str]]:
    with path.open() as source:
        yield from head_split_fixed(row_iter(source))


# this forces the input and output types to be the same
SrcT = TypeVar("SrcT")


def series(n: int, row_iter: Iterator[list[SrcT]]) -> Iterator[tuple[SrcT, SrcT]]:
    for row in row_iter:
        yield cast(tuple[SrcT, SrcT], tuple(row[n * 2 : n * 2 + 2]))


if __name__ == "__main__":
    logger.info("--- Chapter 3: Iterators and Generators ---")
    logger.info("--- Example 3-1: Reading a CSV file with a fixed format ---")
    source_path = Path("../data/Anscombe.txt")

    logger.info("Read the file and covert it to a list of lists")
    with source_path.open() as source:
        print(list(row_iter(source)))

    logger.info("Read the file and print each row")
    for row in get_rows(source_path):
        print(row)

    logger.info("Read the file and save the data in a tuple")
    with source_path.open() as source:
        data = tuple(head_split_fixed(row_iter(source)))

    logger.info("Extract the first pair of values from each row")
    series_i = tuple(series(0, iter(data)))
    print(series_i)

    logger.info("Extract the second pair of values from each row")
    series_ii = tuple(series(1, iter(data)))
    print(series_ii)
