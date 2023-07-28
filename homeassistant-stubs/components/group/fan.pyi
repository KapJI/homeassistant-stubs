from . import GroupEntity as GroupEntity
from .util import attribute_equal as attribute_equal, most_frequent_attribute as most_frequent_attribute, reduce_attribute as reduce_attribute, states_equal as states_equal
from _typeshed import Incomplete
from homeassistant.components.fan import ATTR_DIRECTION as ATTR_DIRECTION, ATTR_OSCILLATING as ATTR_OSCILLATING, ATTR_PERCENTAGE as ATTR_PERCENTAGE, ATTR_PERCENTAGE_STEP as ATTR_PERCENTAGE_STEP, DOMAIN as DOMAIN, FanEntity as FanEntity, FanEntityFeature as FanEntityFeature, PLATFORM_SCHEMA as PLATFORM_SCHEMA, SERVICE_OSCILLATE as SERVICE_OSCILLATE, SERVICE_SET_DIRECTION as SERVICE_SET_DIRECTION, SERVICE_SET_PERCENTAGE as SERVICE_SET_PERCENTAGE, SERVICE_TURN_OFF as SERVICE_TURN_OFF, SERVICE_TURN_ON as SERVICE_TURN_ON
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_ASSUMED_STATE as ATTR_ASSUMED_STATE, ATTR_ENTITY_ID as ATTR_ENTITY_ID, ATTR_SUPPORTED_FEATURES as ATTR_SUPPORTED_FEATURES, CONF_ENTITIES as CONF_ENTITIES, CONF_NAME as CONF_NAME, CONF_UNIQUE_ID as CONF_UNIQUE_ID, STATE_ON as STATE_ON, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import HomeAssistant as HomeAssistant, State as State, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.event import EventStateChangedData as EventStateChangedData, async_track_state_change_event as async_track_state_change_event
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType, EventType as EventType
from typing import Any

SUPPORTED_FLAGS: Incomplete
DEFAULT_NAME: str
PARALLEL_UPDATES: int
_LOGGER: Incomplete

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = ...) -> None: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class FanGroup(GroupEntity, FanEntity):
    _attr_available: bool
    _attr_assumed_state: bool
    _entities: Incomplete
    _fans: Incomplete
    _percentage: Incomplete
    _oscillating: Incomplete
    _direction: Incomplete
    _speed_count: int
    _is_on: bool
    _attr_name: Incomplete
    _attr_extra_state_attributes: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, unique_id: str | None, name: str, entities: list[str]) -> None: ...
    @property
    def speed_count(self) -> int: ...
    @property
    def is_on(self) -> bool | None: ...
    @property
    def percentage(self) -> int | None: ...
    @property
    def current_direction(self) -> str | None: ...
    @property
    def oscillating(self) -> bool | None: ...
    def _update_supported_features_event(self, event: EventType[EventStateChangedData]) -> None: ...
    def async_update_supported_features(self, entity_id: str, new_state: State | None, update_state: bool = ...) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_set_percentage(self, percentage: int) -> None: ...
    async def async_oscillate(self, oscillating: bool) -> None: ...
    async def async_set_direction(self, direction: str) -> None: ...
    async def async_turn_on(self, percentage: int | None = ..., preset_mode: str | None = ..., **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def _async_call_supported_entities(self, service: str, support_flag: int, data: dict[str, Any]) -> None: ...
    async def _async_call_all_entities(self, service: str) -> None: ...
    def _async_states_by_support_flag(self, flag: int) -> list[State]: ...
    def _set_attr_most_frequent(self, attr: str, flag: int, entity_attr: str) -> None: ...
    _attr_supported_features: Incomplete
    def async_update_group_state(self) -> None: ...
