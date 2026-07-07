import json
from datetime import datetime

data = {
    "updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "active": [],
    "upcoming": [],
    "completed": []
}

with open("halkaarz.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("halkaarz.json güncellendi")
