from .const import ATTR_DURATION as ATTR_DURATION, ATTR_TARGET_BRIGHTNESS as ATTR_TARGET_BRIGHTNESS, ATTR_UDP_PORT as ATTR_UDP_PORT
from .coordinator import WLEDConfigEntry as WLEDConfigEntry, WLEDDataUpdateCoordinator as WLEDDataUpdateCoordinator
from .entity import WLEDEntity as WLEDEntity
from .helpers import wled_exception_handler as wled_exception_handler
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any
from wled import WLED as WLED

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class WLEDSegmentSwitchEntityDescription(SwitchEntityDescription):
    segment_translation_key: str
    set_segment: Callable[[WLED, int, bool], Awaitable[None]]

SEGMENT_SWITCHES: tuple[WLEDSegmentSwitchEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: WLEDConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class WLEDNightlightSwitch(WLEDEntity, SwitchEntity):
    _attr_entity_category: Incomplete
    _attr_translation_key: str
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: WLEDDataUpdateCoordinator) -> None: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any] | None: ...
    @property
    def is_on(self) -> bool: ...
    @wled_exception_handler
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @wled_exception_handler
    async def async_turn_on(self, **kwargs: Any) -> None: ...

class WLEDSyncSendSwitch(WLEDEntity, SwitchEntity):
    _attr_entity_category: Incomplete
    _attr_translation_key: str
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: WLEDDataUpdateCoordinator) -> None: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any] | None: ...
    @property
    def is_on(self) -> bool: ...
    @wled_exception_handler
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @wled_exception_handler
    async def async_turn_on(self, **kwargs: Any) -> None: ...

class WLEDSyncReceiveSwitch(WLEDEntity, SwitchEntity):
    _attr_entity_category: Incomplete
    _attr_translation_key: str
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: WLEDDataUpdateCoordinator) -> None: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any] | None: ...
    @property
    def is_on(self) -> bool: ...
    @wled_exception_handler
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @wled_exception_handler
    async def async_turn_on(self, **kwargs: Any) -> None: ...

class WLEDSegmentSwitch(WLEDEntity, SwitchEntity):
    entity_description: WLEDSegmentSwitchEntityDescription
    _attr_entity_category: Incomplete
    _segment: Incomplete
    _attr_translation_key: Incomplete
    _attr_translation_placeholders: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: WLEDDataUpdateCoordinator, segment: int, description: WLEDSegmentSwitchEntityDescription) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def is_on(self) -> bool: ...
    async def _async_set_state(self, value: bool) -> None: ...
    @wled_exception_handler
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @wled_exception_handler
    async def async_turn_off(self, **kwargs: Any) -> None: ...

@callback
def async_update_segments(coordinator: WLEDDataUpdateCoordinator, current_ids: set[int], async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...
