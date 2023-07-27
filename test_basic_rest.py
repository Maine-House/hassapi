from dotenv import load_dotenv
load_dotenv()
import os

from src import HASS

hass = HASS(os.getenv("ADDR"), os.getenv("TOKEN"))
print(hass.rest.api_status().model_dump())