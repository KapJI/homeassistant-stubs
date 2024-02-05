import motionmount
from .const import DOMAIN as DOMAIN, WALL_PRESET_NAME as WALL_PRESET_NAME
from .entity import MotionMountEntity as MotionMountEntity
from _typeshed import Incomplete
from homeassistant.components.select import SelectEntity as SelectEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class MotionMountPresets(MotionMountEntity, SelectEntity):
    _attr_translation_key: str
    _attr_current_option: str | None
    _attr_unique_id: Incomplete
    def __init__(self, mm: motionmount.MotionMount, config_entry: ConfigEntry) -> None: ...
    _attr_options: Incomplete
    def _update_options(self, presets: dict[int, str]) -> None: ...
    async def async_update(self) -> None: ...
    async def async_select_option(self, option: str) -> None: ...
