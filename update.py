import json
from datetime import datetime

from providers.provider_manual import ManualProvider
from providers.provider_spk import SpkProvider


manual = ManualProvider().get_ipos()
spk = SpkProvider().get_ipos()

completed = spk["completed"] + manual["completed"]

stats = {
    "completed_count": len(completed),
    "active_count": len(manual["active"]),
    "upcoming_count": len(manual["upcoming"])
}

data = {
    "updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "stats": stats,
    "active": manual["active"],
    "upcoming": manual["upcoming"],
    "completed": completed
}

with open("halkaarz.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"SPK'dan {len(spk['completed'])} kayıt alındı.")
print("halkaarz.json güncellendi.")
