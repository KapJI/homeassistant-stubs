from .const import CONF_HYSTERESIS as CONF_HYSTERESIS, CONF_LOWER as CONF_LOWER, CONF_UPPER as CONF_UPPER
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Mapping
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, DEVICE_CLASSES_SCHEMA as DEVICE_CLASSES_SCHEMA
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, CONF_DEVICE_CLASS as CONF_DEVICE_CLASS, CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_NAME as CONF_NAME, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, Event as Event, EventStateChangedData as EventStateChangedData, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device import async_device_info_to_link_from_entity as async_device_info_to_link_from_entity
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.event import async_track_state_change_event as async_track_state_change_event
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

_LOGGER: Incomplete
ATTR_HYSTERESIS: str
ATTR_LOWER: str
ATTR_POSITION: str
ATTR_SENSOR_VALUE: str
ATTR_TYPE: str
ATTR_UPPER: str
DEFAULT_NAME: str
DEFAULT_HYSTERESIS: float
POSITION_ABOVE: str
POSITION_BELOW: str
POSITION_IN_RANGE: str
POSITION_UNKNOWN: str
TYPE_LOWER: str
TYPE_RANGE: str
TYPE_UPPER: str
PLATFORM_SCHEMA: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...
def _threshold_type(lower: float | None, upper: float | None) -> str: ...

class ThresholdSensor(BinarySensorEntity):
    _attr_should_poll: bool
    _preview_callback: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    _entity_id: Incomplete
    _attr_name: Incomplete
    _threshold_lower: Incomplete
    _threshold_upper: Incomplete
    threshold_type: Incomplete
    _hysteresis: Incomplete
    _attr_device_class: Incomplete
    _state_position: Incomplete
    _state: Incomplete
    sensor_value: Incomplete
    def __init__(self, entity_id: str, name: str, lower: float | None, upper: float | None, hysteresis: float, device_class: BinarySensorDeviceClass | None, unique_id: str | None, device_info: DeviceInfo | None = None) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    def _async_setup_sensor(self) -> None: ...
    @property
    def is_on(self) -> bool | None: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
    def _update_state(self) -> None: ...
    _attr_available: bool
    def async_start_preview(self, preview_callback: Callable[[str, Mapping[str, Any]], None]) -> CALLBACK_TYPE: ...
