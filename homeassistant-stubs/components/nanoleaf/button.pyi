from . import NanoleafEntryData as NanoleafEntryData
from .const import DOMAIN as DOMAIN
from .entity import NanoleafEntity as NanoleafEntity
from aionanoleaf import Nanoleaf as Nanoleaf
from homeassistant.components.button import ButtonEntity as ButtonEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ENTITY_CATEGORY_CONFIG as ENTITY_CATEGORY_CONFIG
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class NanoleafIdentifyButton(NanoleafEntity, ButtonEntity):
    _attr_unique_id: Any
    _attr_name: Any
    _attr_icon: str
    _attr_entity_category: Any
    def __init__(self, nanoleaf: Nanoleaf) -> None: ...
    async def async_press(self) -> None: ...
