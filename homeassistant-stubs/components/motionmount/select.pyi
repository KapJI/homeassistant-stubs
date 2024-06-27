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
    _attr_unique_id: Incomplete
    _presets: Incomplete
    def __init__(self, mm: motionmount.MotionMount, config_entry: ConfigEntry) -> None: ...
    _attr_options: Incomplete
    def _update_options(self, presets: list[motionmount.Preset]) -> None: ...
    async def async_update(self) -> None: ...
    _attr_current_option: Incomplete
    @property
    def current_option(self) -> str | None: ...
    async def async_select_option(self, option: str) -> None: ...
