import json
import os


def load_data():
    file_path = os.path.join(os.path.dirname(__file__), "../data/trademark_sample.json")
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    for item in data:
        # Null 방지
        item["productName"] = item.get("productName") or ""
        item["productNameEng"] = item.get("productNameEng") or ""
        item["registerStatus"] = item.get("registerStatus") or ""
        item["registrationDate"] = (item.get("registrationDate") or [None])[0] or ""
        item["asignProductMainCodeList"] = item.get("asignProductMainCodeList") or []

    return data
