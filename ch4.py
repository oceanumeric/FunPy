import urllib.request
from pprint import pprint
from loguru import logger
from collections.abc import Iterable
from typing import TextIO
import xml.etree.ElementTree as XML


def comma_split(text: str) -> list[str]:
    return text.split(",")


def row_iter_kml(file_obj: TextIO) -> Iterable[list[str]]:
    ns_map = {
        "ns0": "http://www.opengis.net/kml/2.2",
        "ns1": "http://www.google.com/kml/ext/2.2",
    }
    path_to_points = (
        "./ns0:Document/ns0:Folder/ns0:Placemark/" "ns0:Point/ns0:coordinates"
    )
    doc = XML.parse(file_obj)
    text_blocks = (
        coordinates.text for coordinates in doc.iterfind(path_to_points, ns_map)
    )

    return (comma_split(text) for text in text_blocks if text is not None)


if __name__ == "__main__":
    logger.info("----- Chapter 4 -----")
    source_file = "file:./data/winter_2012_2013.kml"
    with urllib.request.urlopen(source_file) as source:
        v1 = list(row_iter_kml(source))
    pprint(v1)
