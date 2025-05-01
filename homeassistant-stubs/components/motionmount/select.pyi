import motionmount
from . import MotionMountConfigEntry as MotionMountConfigEntry
from .const import DOMAIN as DOMAIN, WALL_PRESET_NAME as WALL_PRESET_NAME
from .entity import MotionMountEntity as MotionMountEntity
from _typeshed import Incomplete
from homeassistant.components.select import SelectEntity as SelectEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

_LOGGER: Incomplete
SCAN_INTERVAL: Incomplete
PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: MotionMountConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class MotionMountPresets(MotionMountEntity, SelectEntity):
    _attr_should_poll: bool
    _attr_translation_key: str
    _attr_unique_id: Incomplete
    _presets: list[motionmount.Preset]
    _attr_current_option: Incomplete
    def __init__(self, mm: motionmount.MotionMount, config_entry: MotionMountConfigEntry) -> None: ...
    _attr_options: Incomplete
    def _update_options(self, presets: list[motionmount.Preset]) -> None: ...
    pin: Incomplete
    async def _ensure_connected(self) -> bool: ...
    async def async_update(self) -> None: ...
    @property
    def current_option(self) -> str | None: ...
    async def async_select_option(self, option: str) -> None: ...
