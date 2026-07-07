from .provider import Provider
from datetime import datetime


class ManualProvider(Provider):

    def get_ipos(self):

        return {
            "updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "active": [],
            "upcoming": [],
            "completed": []
        }
