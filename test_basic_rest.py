from dotenv import load_dotenv
load_dotenv()
import os

from src import HASS

hass = HASS(os.getenv("ADDR"), os.getenv("TOKEN"))
print(hass.rest.api_status())
print(hass.rest.get_config())
print(hass.rest.get_services())
print(hass.rest.get_states())
print(hass.rest.get_state("sensor.zariel_1_bme280_humidity"))
print(hass.rest.evaluate_template("Current time: {{ now() }}"))
print(hass.rest.call_service("switch", "toggle", {"entity_id": "switch.bed_test"}))