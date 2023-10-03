from . import PLATFORMS as PLATFORMS
from .const import ATTR_GRADIENT as ATTR_GRADIENT, ATTR_INVERT as ATTR_INVERT, ATTR_MIN_GRADIENT as ATTR_MIN_GRADIENT, ATTR_SAMPLE_COUNT as ATTR_SAMPLE_COUNT, ATTR_SAMPLE_DURATION as ATTR_SAMPLE_DURATION, CONF_INVERT as CONF_INVERT, CONF_MAX_SAMPLES as CONF_MAX_SAMPLES, CONF_MIN_GRADIENT as CONF_MIN_GRADIENT, CONF_SAMPLE_DURATION as CONF_SAMPLE_DURATION, DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, DEVICE_CLASSES_SCHEMA as DEVICE_CLASSES_SCHEMA, ENTITY_ID_FORMAT as ENTITY_ID_FORMAT, PLATFORM_SCHEMA as PLATFORM_SCHEMA
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, ATTR_FRIENDLY_NAME as ATTR_FRIENDLY_NAME, CONF_ATTRIBUTE as CONF_ATTRIBUTE, CONF_DEVICE_CLASS as CONF_DEVICE_CLASS, CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_FRIENDLY_NAME as CONF_FRIENDLY_NAME, CONF_SENSORS as CONF_SENSORS, STATE_ON as STATE_ON, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity import generate_entity_id as generate_entity_id
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.event import EventStateChangedData as EventStateChangedData, async_track_state_change_event as async_track_state_change_event
from homeassistant.helpers.reload import async_setup_reload_service as async_setup_reload_service
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType, EventType as EventType
from homeassistant.util.dt import utcnow as utcnow
from typing import Any

_LOGGER: Incomplete
SENSOR_SCHEMA: Incomplete

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = ...) -> None: ...

class SensorTrend(BinarySensorEntity, RestoreEntity):
    _attr_should_poll: bool
    _gradient: float
    _state: bool | None
    _hass: Incomplete
    entity_id: Incomplete
    _attr_name: Incomplete
    _attr_device_class: Incomplete
    _entity_id: Incomplete
    _attribute: Incomplete
    _invert: Incomplete
    _sample_duration: Incomplete
    _min_gradient: Incomplete
    samples: Incomplete
    def __init__(self, hass: HomeAssistant, device_id: str, friendly_name: str, entity_id: str, attribute: str, device_class: BinarySensorDeviceClass, invert: bool, max_samples: int, min_gradient: float, sample_duration: int) -> None: ...
    @property
    def is_on(self) -> bool | None: ...
    @property
    def extra_state_attributes(self) -> Mapping[str, Any]: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_update(self) -> None: ...
    def _calculate_gradient(self) -> None: ...
