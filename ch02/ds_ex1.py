import json
from loguru import logger
from functools import reduce
from collections.abc import Iterator
from typing import Dict, Any, TypeVar, Union, List


# sample nested JSON data
json_data = """
{
    "users": [
        {
            "id": 1,
            "name": "Alice",
            "activities": [
                {"date": "2023-01-01", "type": "running", "distance": 5.2},
                {"date": "2023-01-02", "type": "cycling", "distance": 20.0}
            ]
        },
        {
            "id": 2,
            "name": "Bob",
            "activities": [
                {"date": "2023-01-01", "type": "swimming", "distance": 1.0},
                {"date": "2023-01-02", "type": "running", "distance": 3.0}
            ]
        }
    ]
}
"""

StruT = TypeVar("StruT")


def extract_running_activities(data: Dict[str, StruT]) -> Iterator[Dict[str, StruT]]:
    """Generator to extract all running activities (entry-level)"""
    for user in data["users"]:
        for activity in user["activities"]:
            if activity["type"] == "running":
                yield {
                    "user": user["name"],
                    "date": activity["date"],
                    "distance": activity["distance"],
                }


def extract_running_activities2(data: Dict[str, StruT]) -> Iterator[Dict[str, StruT]]:
    """Generator to extract all running activites (medium-level)"""
    return (
        {
            "user": user["name"],
            "date": activity["date"],
            "distance": activity["distance"],
        }
        for user in data["users"]
        for activity in user["activities"]
        if activity["type"] == "running"
    )


def json_to_csv(data: Dict[str, Any]) -> str:
    # Generate csv rows using a generator expression
    rows = (
        [
            user["id"],
            user["name"],
            activity["type"],
            activity["date"],
            activity["distance"],
        ]
        for user in data["users"]
        for activity in user["activities"]
    )

    # concatnate
    csv_content = "\n".join(",".join(map(str, row)) for row in rows)

    # add header
    header = "id, name, activity, date, distance"
    csv_content = f"{header}\n{csv_content}"

    return csv_content


def flatten_json(
    json_data: Union[Dict[str, Any], list[Any]],
    parent_key: str = "",
    sep: str = "_") -> Dict[str, Any]:
    """Flatten a nested JSON structure"""
    items = {}
    
    for key, value in json_data.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key
        if isinstance(value, dict):
            items.update(flatten_json(value, new_key, sep=sep))
        elif isinstance(value, list):
            for i, item in enumerate(value):
                items.update(flatten_json(item, f"{new_key}{sep}{i}", sep=sep))
        else:
            items[new_key] = value
            
    return items


if __name__ == "__main__":
    logger.info("----- Ch02 DS Example 1 -----")
    data: Dict[str, Any] = json.loads(json_data)
    running_activities = extract_running_activities(data)
    for activity in running_activities:
        print(activity)

    logger.info("-" * 10)

    running_activities = extract_running_activities2(data)
    for act in running_activities:
        print(act)

    logger.info("----- convert to csv -----")
    csv_data = json_to_csv(data)
    print(csv_data)
    
    logger.info("----- convert to csv (flattened) -----")
    flat_data = flatten_json(data)
    print(flat_data)