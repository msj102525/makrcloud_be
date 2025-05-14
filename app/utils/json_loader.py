import json
import os
from typing import List


def load_trademark_data() -> List[dict]:
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    json_path = os.path.join(base_path, "data", "trademark_sample.json")
    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)
