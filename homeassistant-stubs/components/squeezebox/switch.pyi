from .const import ATTR_ALARM_ID as ATTR_ALARM_ID, DOMAIN as DOMAIN, SIGNAL_PLAYER_DISCOVERED as SIGNAL_PLAYER_DISCOVERED
from .coordinator import SqueezeBoxPlayerUpdateCoordinator as SqueezeBoxPlayerUpdateCoordinator
from .entity import SqueezeboxEntity as SqueezeboxEntity
from _typeshed import Incomplete
from homeassistant.components.switch import SwitchEntity as SwitchEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import format_mac as format_mac
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.event import async_track_time_change as async_track_time_change
from pysqueezebox.player import Alarm as Alarm
from typing import Any

_LOGGER: Incomplete
PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class SqueezeBoxAlarmEntity(SqueezeboxEntity, SwitchEntity):
    _attr_translation_key: str
    _attr_entity_category: Incomplete
    _alarm_id: Incomplete
    _attr_translation_placeholders: Incomplete
    _attr_unique_id: str
    def __init__(self, coordinator: SqueezeBoxPlayerUpdateCoordinator, alarm_id: str) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @property
    def alarm(self) -> Alarm: ...
    @property
    def available(self) -> bool: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
    @property
    def is_on(self) -> bool: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...

class SqueezeBoxAlarmsEnabledEntity(SqueezeboxEntity, SwitchEntity):
    _attr_translation_key: str
    _attr_entity_category: Incomplete
    _attr_unique_id: str
    def __init__(self, coordinator: SqueezeBoxPlayerUpdateCoordinator) -> None: ...
    @property
    def is_on(self) -> bool: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
