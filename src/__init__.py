from rest_client import HASS_Rest

class HASS:
    def __init__(self, address: str, token: str):
        self.address = address
        self.token = token
        self.rest = HASS_Rest(address, token)