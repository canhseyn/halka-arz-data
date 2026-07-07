import json
from pathlib import Path

from .provider import Provider


class ManualProvider(Provider):

    def get_ipos(self):

        file_path = Path("data/manual_ipos.json")

        if not file_path.exists():
            return {
                "active": [],
                "upcoming": [],
                "completed": []
            }

        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
