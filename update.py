import json
from datetime import datetime

from providers.provider_manual import ManualProvider

provider = ManualProvider()

manual = provider.get_ipos()

data = {
    "updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "active": manual.get("active", []),
    "upcoming": manual.get("upcoming", []),
    "completed": manual.get("completed", [])
}

with open("halkaarz.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("halkaarz.json güncellendi")
