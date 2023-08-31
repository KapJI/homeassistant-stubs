from . import GroupEntity as GroupEntity
from .const import CONF_IGNORE_NON_NUMERIC as CONF_IGNORE_NON_NUMERIC
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components.sensor import CONF_STATE_CLASS as CONF_STATE_CLASS, DEVICE_CLASSES_SCHEMA as DEVICE_CLASSES_SCHEMA, DOMAIN as DOMAIN, STATE_CLASSES_SCHEMA as STATE_CLASSES_SCHEMA, SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, CONF_DEVICE_CLASS as CONF_DEVICE_CLASS, CONF_ENTITIES as CONF_ENTITIES, CONF_NAME as CONF_NAME, CONF_TYPE as CONF_TYPE, CONF_UNIQUE_ID as CONF_UNIQUE_ID, CONF_UNIT_OF_MEASUREMENT as CONF_UNIT_OF_MEASUREMENT, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import HomeAssistant as HomeAssistant, State as State, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType, StateType as StateType
from typing import Any

DEFAULT_NAME: str
ATTR_MIN_VALUE: str
ATTR_MIN_ENTITY_ID: str
ATTR_MAX_VALUE: str
ATTR_MAX_ENTITY_ID: str
ATTR_MEAN: str
ATTR_MEDIAN: str
ATTR_LAST: str
ATTR_LAST_ENTITY_ID: str
ATTR_RANGE: str
ATTR_SUM: str
ATTR_PRODUCT: str
SENSOR_TYPES: Incomplete
SENSOR_TYPE_TO_ATTR: Incomplete
PARALLEL_UPDATES: int
PLATFORM_SCHEMA: Incomplete
_LOGGER: Incomplete

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = ...) -> None: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
def async_create_preview_sensor(name: str, validated_config: dict[str, Any]) -> SensorGroup: ...
def calc_min(sensor_values: list[tuple[str, float, State]]) -> tuple[dict[str, str | None], float | None]: ...
def calc_max(sensor_values: list[tuple[str, float, State]]) -> tuple[dict[str, str | None], float | None]: ...
def calc_mean(sensor_values: list[tuple[str, float, State]]) -> tuple[dict[str, str | None], float | None]: ...
def calc_median(sensor_values: list[tuple[str, float, State]]) -> tuple[dict[str, str | None], float | None]: ...
def calc_last(sensor_values: list[tuple[str, float, State]]) -> tuple[dict[str, str | None], float | None]: ...
def calc_range(sensor_values: list[tuple[str, float, State]]) -> tuple[dict[str, str | None], float]: ...
def calc_sum(sensor_values: list[tuple[str, float, State]]) -> tuple[dict[str, str | None], float]: ...
def calc_product(sensor_values: list[tuple[str, float, State]]) -> tuple[dict[str, str | None], float]: ...

CALC_TYPES: dict[str, Callable[[list[tuple[str, float, State]]], tuple[dict[str, str | None], float | None]]]

class SensorGroup(GroupEntity, SensorEntity):
    _attr_available: bool
    _attr_should_poll: bool
    _entity_ids: Incomplete
    _sensor_type: Incomplete
    _attr_state_class: Incomplete
    calc_state_class: Incomplete
    _attr_device_class: Incomplete
    calc_device_class: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    calc_unit_of_measurement: Incomplete
    _attr_name: Incomplete
    _attr_extra_state_attributes: Incomplete
    _attr_unique_id: Incomplete
    mode: Incomplete
    _state_calc: Incomplete
    _state_incorrect: Incomplete
    _extra_state_attribute: Incomplete
    def __init__(self, unique_id: str | None, name: str, entity_ids: list[str], mode: bool, sensor_type: str, unit_of_measurement: str | None, state_class: SensorStateClass | None, device_class: SensorDeviceClass | None) -> None: ...
    _attr_native_value: Incomplete
    def async_update_group_state(self) -> None: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
    @property
    def device_class(self) -> SensorDeviceClass | None: ...
    @property
    def icon(self) -> str | None: ...
    @property
    def state_class(self) -> SensorStateClass | str | None: ...
    @property
    def native_unit_of_measurement(self) -> str | None: ...
    def _calculate_entity_properties(self) -> None: ...
