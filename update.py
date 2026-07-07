import json

from providers.provider_manual import ManualProvider

provider = ManualProvider()

data = provider.get_ipos()

with open("halkaarz.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("JSON güncellendi")
