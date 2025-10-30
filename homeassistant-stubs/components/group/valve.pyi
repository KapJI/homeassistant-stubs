from .entity import GroupEntity as GroupEntity
from .util import reduce_attribute as reduce_attribute
from _typeshed import Incomplete
from homeassistant.components.valve import ATTR_CURRENT_POSITION as ATTR_CURRENT_POSITION, ATTR_POSITION as ATTR_POSITION, ValveEntity as ValveEntity, ValveEntityFeature as ValveEntityFeature, ValveState as ValveState
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, ATTR_SUPPORTED_FEATURES as ATTR_SUPPORTED_FEATURES, CONF_ENTITIES as CONF_ENTITIES, CONF_NAME as CONF_NAME, CONF_UNIQUE_ID as CONF_UNIQUE_ID, SERVICE_CLOSE_VALVE as SERVICE_CLOSE_VALVE, SERVICE_OPEN_VALVE as SERVICE_OPEN_VALVE, SERVICE_SET_VALVE_POSITION as SERVICE_SET_VALVE_POSITION, SERVICE_STOP_VALVE as SERVICE_STOP_VALVE, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import HomeAssistant as HomeAssistant, State as State, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback, AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

KEY_OPEN_CLOSE: str
KEY_STOP: str
KEY_SET_POSITION: str
DEFAULT_NAME: str
PARALLEL_UPDATES: int
PLATFORM_SCHEMA: Incomplete

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...
@callback
def async_create_preview_valve(hass: HomeAssistant, name: str, validated_config: dict[str, Any]) -> ValveGroup: ...

class ValveGroup(GroupEntity, ValveEntity):
    _attr_available: bool
    _attr_current_valve_position: int | None
    _attr_is_closed: bool | None
    _attr_is_closing: bool | None
    _attr_is_opening: bool | None
    _attr_reports_position: bool
    _entity_ids: Incomplete
    _valves: dict[str, set[str]]
    _attr_name: Incomplete
    _attr_extra_state_attributes: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, unique_id: str | None, name: str, entities: list[str]) -> None: ...
    @callback
    def async_update_supported_features(self, entity_id: str, new_state: State | None) -> None: ...
    async def async_open_valve(self) -> None: ...
    async def async_handle_open_valve(self) -> None: ...
    async def async_close_valve(self) -> None: ...
    async def async_handle_close_valve(self) -> None: ...
    async def async_set_valve_position(self, position: int) -> None: ...
    async def async_stop_valve(self) -> None: ...
    _attr_supported_features: Incomplete
    @callback
    def async_update_group_state(self) -> None: ...
