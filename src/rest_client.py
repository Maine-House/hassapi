from requests import Session, Response
from .typings import *
from typing import *
from .util import HASSException

class HASS_Rest:
    def __init__(self, address: str, token: str) -> None:
        self.address = address
        self.token = token
        self.session = Session()
        self.session.headers["Authorization"] = "Bearer " + token
        self.session.headers["Content-Type"] = "appplication/json"
    
    def url(self, endpoint: str) -> str:
        return f"{self.address}/api{endpoint}"
    
    def handle_exc(self, response: Response) -> Any:
        if response.status_code < 400:
            try:
                return response.json()
            except:
                return response.text
        else:
            raise HASSException(response.status_code, response.reason, response.text)
    
    def api_status(self) -> Status:
        return Status(**self.handle_exc(self.session.get(self.url("/"))))
    
    def get_config(self) -> Config:
        return Config(**self.handle_exc(self.session.get(self.url("/config"))))
    
    