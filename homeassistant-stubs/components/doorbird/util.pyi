from .const import DOMAIN as DOMAIN
from .device import ConfiguredDoorBird as ConfiguredDoorBird
from .models import DoorBirdData as DoorBirdData
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

def get_mac_address_from_door_station_info(door_station_info: dict[str, Any]) -> str: ...
def get_door_station_by_token(hass: HomeAssistant, token: str) -> ConfiguredDoorBird | None: ...
