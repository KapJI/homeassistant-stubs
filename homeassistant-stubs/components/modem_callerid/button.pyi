from .const import DATA_KEY_API as DATA_KEY_API, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.button import ButtonEntity as ButtonEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_DEVICE as CONF_DEVICE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from phone_modem import PhoneModem as PhoneModem

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class PhoneModemButton(ButtonEntity):
    _attr_icon: str
    _attr_name: str
    device: Incomplete
    api: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, api: PhoneModem, device: str, server_unique_id: str) -> None: ...
    async def async_press(self) -> None: ...
