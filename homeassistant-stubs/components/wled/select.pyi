from .const import DOMAIN as DOMAIN
from .coordinator import WLEDDataUpdateCoordinator as WLEDDataUpdateCoordinator
from .helpers import wled_exception_handler as wled_exception_handler
from .models import WLEDEntity as WLEDEntity
from _typeshed import Incomplete
from homeassistant.components.select import SelectEntity as SelectEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class WLEDLiveOverrideSelect(WLEDEntity, SelectEntity):
    _attr_entity_category: Incomplete
    _attr_icon: str
    _attr_name: str
    _attr_translation_key: str
    _attr_unique_id: Incomplete
    _attr_options: Incomplete
    def __init__(self, coordinator: WLEDDataUpdateCoordinator) -> None: ...
    @property
    def current_option(self) -> str: ...
    async def async_select_option(self, option: str) -> None: ...

class WLEDPresetSelect(WLEDEntity, SelectEntity):
    _attr_icon: str
    _attr_name: str
    _attr_unique_id: Incomplete
    _attr_options: Incomplete
    def __init__(self, coordinator: WLEDDataUpdateCoordinator) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def current_option(self) -> str | None: ...
    async def async_select_option(self, option: str) -> None: ...

class WLEDPlaylistSelect(WLEDEntity, SelectEntity):
    _attr_icon: str
    _attr_name: str
    _attr_unique_id: Incomplete
    _attr_options: Incomplete
    def __init__(self, coordinator: WLEDDataUpdateCoordinator) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def current_option(self) -> str | None: ...
    async def async_select_option(self, option: str) -> None: ...

class WLEDPaletteSelect(WLEDEntity, SelectEntity):
    _attr_entity_category: Incomplete
    _attr_icon: str
    _attr_name: str
    _segment: int
    _attr_unique_id: Incomplete
    _attr_options: Incomplete
    def __init__(self, coordinator: WLEDDataUpdateCoordinator, segment: int) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def current_option(self) -> str | None: ...
    async def async_select_option(self, option: str) -> None: ...

def async_update_segments(coordinator: WLEDDataUpdateCoordinator, current_ids: set[int], async_add_entities: AddEntitiesCallback) -> None: ...
