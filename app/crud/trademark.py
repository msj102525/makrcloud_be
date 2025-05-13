import json
from typing import List
import os
from schemas.trademark import Trademark

def load_trademark_data() -> List[dict]:
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    json_path = os.path.join(base_path, "data", "trademark_sample.json")
    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)

def search_trademark_by_name(name: str) -> List[Trademark]:
    data = load_trademark_data()
    name_lower = name.lower()
    result = [
        Trademark(**item)
        for item in data
        if (item.get("productName") and name_lower in item["productName"].lower())
        or (item.get("productNameEng") and name_lower in item["productNameEng"].lower())
    ]
    return result

def search_by_application_date(start_date: str, end_date: str) -> List[Trademark]:
    data = load_trademark_data()
    result = [
        Trademark(**item)
        for item in data
        if item.get("applicationDate") and start_date <= item["applicationDate"] <= end_date
    ]
    return result