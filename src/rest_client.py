import requests

class HASS_Rest:
    def __init__(self, address: str, token: str) -> None:
        self.address = address
        self.token = token
        self.session = requests.Session()
        self.session.headers["Authorization"] = "Bearer " + token
    
    def url(self, endpoint: str) -> str:
        return f"{self.address}/api{endpoint}"
    
    