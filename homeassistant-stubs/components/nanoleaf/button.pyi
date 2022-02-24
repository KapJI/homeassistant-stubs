from . import NanoleafEntryData as NanoleafEntryData
from .const import DOMAIN as DOMAIN
from .entity import NanoleafEntity as NanoleafEntity
from aionanoleaf import Nanoleaf as Nanoleaf
from homeassistant.components.button import ButtonEntity as ButtonEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class NanoleafIdentifyButton(NanoleafEntity, ButtonEntity):
    _attr_unique_id: Any
    _attr_name: Any
    _attr_icon: str
    _attr_entity_category: Any
    def __init__(self, nanoleaf: Nanoleaf, coordinator: DataUpdateCoordinator) -> None: ...
    async def async_press(self) -> None: ...
