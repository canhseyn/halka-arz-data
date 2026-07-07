import requests
from datetime import datetime

from .provider import Provider


class SpkProvider(Provider):

    BASE_URL = "https://ws.spk.gov.tr/BorclanmaAraclari/api/IlkHalkaArzVerileri"

    def get_ipos(self):

        completed = []

        current_year = datetime.now().year

        for year in range(current_year - 2, current_year + 1):

            response = requests.get(
                self.BASE_URL,
                params={"yil": year},
                timeout=30
            )

            response.raise_for_status()

            records = response.json()

            for item in records:

                completed.append({
                    "company": item.get("sirketUnvani"),
                    "code": item.get("borsaKodu"),
                    "price": item.get("halkaArzFiyatiTl"),
                    "ratio": item.get("halkaArzOrani"),
                    "method": item.get("halkaArzSekli"),
                    "market": item.get("ilkIslemGorduguPazar"),
                    "broker": item.get("halkaArzaAracilikEdenKurum"),
                    "listing_date": item.get("borsadaIslemGormeTarihi"),
                    "year": year
                })

        return {
            "active": [],
            "upcoming": [],
            "completed": completed
        }
