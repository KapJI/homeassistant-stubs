from .const import DOMAIN as DOMAIN
from elgato import Elgato as Elgato, Info as Info
from homeassistant.components.button import ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ENTITY_CATEGORY_CONFIG as ENTITY_CATEGORY_CONFIG
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

_LOGGER: Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ElgatoIdentifyButton(ButtonEntity):
    elgato: Any
    _info: Any
    entity_description: Any
    _attr_unique_id: Any
    def __init__(self, elgato: Elgato, info: Info) -> None: ...
    @property
    def device_info(self) -> DeviceInfo: ...
    async def async_press(self) -> None: ...
