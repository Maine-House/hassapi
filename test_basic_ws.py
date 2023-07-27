from dotenv import load_dotenv
load_dotenv()
import os
import asyncio

from src import HASS

hass = HASS(os.getenv("ADDR"), os.getenv("TOKEN"))

@hass.ws.handle_entity_update("switch.bed_test")
def handle_state_change(event):
    print("OUT", event)

asyncio.run(hass.ws.run())