from dotenv import load_dotenv
load_dotenv()
import os
import json

from src import HASS

hass = HASS(os.getenv("ADDR"), os.getenv("TOKEN"))
print(hass.rest.api_status())
print(hass.rest.get_config())
print(hass.rest.get_services())