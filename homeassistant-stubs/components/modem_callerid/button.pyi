from .const import DATA_KEY_API as DATA_KEY_API, DOMAIN as DOMAIN
from homeassistant.components.button import ButtonEntity as ButtonEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_DEVICE as CONF_DEVICE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import entity_platform as entity_platform
from phone_modem import PhoneModem as PhoneModem
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: entity_platform.AddEntitiesCallback) -> None: ...

class PhoneModemButton(ButtonEntity):
    _attr_icon: str
    _attr_name: str
    device: Any
    api: Any
    _attr_unique_id: Any
    def __init__(self, api: PhoneModem, device: str, server_unique_id: str) -> None: ...
    async def async_press(self) -> None: ...
