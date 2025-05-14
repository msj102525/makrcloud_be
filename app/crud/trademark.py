from typing import List
from schemas.trademark import Trademark
from app.utils.json_loader import load_trademark_data


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