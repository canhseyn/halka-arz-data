
import requests

from .provider import Provider


class SpkProvider(Provider):

    BASE_URL = ""

    def get_ipos(self):
        """
        SPK verilerini döndürecek.
        Şimdilik boş liste döndürüyoruz.
        """

        return {
            "active": [],
            "upcoming": [],
            "completed": []
        }
