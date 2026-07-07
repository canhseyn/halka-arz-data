import json
from datetime import datetime

from providers.provider_manual import ManualProvider
from providers.provider_spk import SpkProvider

manual = ManualProvider().get_ipos()
spk = SpkProvider().get_ipos()

data = {
    "updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "active": spk["active"] + manual["active"],
    "upcoming": spk["upcoming"] + manual["upcoming"],
    "completed": spk["completed"] + manual["completed"]
}

with open("halkaarz.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("halkaarz.json güncellendi")
