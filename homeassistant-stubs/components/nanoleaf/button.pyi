from . import NanoleafEntryData as NanoleafEntryData
from .const import DOMAIN as DOMAIN
from .entity import NanoleafEntity as NanoleafEntity
from _typeshed import Incomplete
from aionanoleaf import Nanoleaf as Nanoleaf
from homeassistant.components.button import ButtonEntity as ButtonEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class NanoleafIdentifyButton(NanoleafEntity, ButtonEntity):
    _attr_unique_id: Incomplete
    _attr_name: Incomplete
    _attr_icon: str
    _attr_entity_category: Incomplete
    def __init__(self, nanoleaf: Nanoleaf, coordinator: DataUpdateCoordinator[None]) -> None: ...
    async def async_press(self) -> None: ...
