from . import ValloxStateProxy as ValloxStateProxy
from .const import DOMAIN as DOMAIN, METRIC_KEY_MODE as METRIC_KEY_MODE, MODE_ON as MODE_ON, SIGNAL_VALLOX_STATE_UPDATE as SIGNAL_VALLOX_STATE_UPDATE, VALLOX_PROFILE_TO_STR_REPORTABLE as VALLOX_PROFILE_TO_STR_REPORTABLE
from homeassistant.components.sensor import STATE_CLASS_MEASUREMENT as STATE_CLASS_MEASUREMENT, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.const import CONCENTRATION_PARTS_PER_MILLION as CONCENTRATION_PARTS_PER_MILLION, DEVICE_CLASS_CO2 as DEVICE_CLASS_CO2, DEVICE_CLASS_HUMIDITY as DEVICE_CLASS_HUMIDITY, DEVICE_CLASS_TEMPERATURE as DEVICE_CLASS_TEMPERATURE, DEVICE_CLASS_TIMESTAMP as DEVICE_CLASS_TIMESTAMP, PERCENTAGE as PERCENTAGE, TEMP_CELSIUS as TEMP_CELSIUS
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

_LOGGER: Any

class ValloxSensor(SensorEntity):
    _attr_should_poll: bool
    entity_description: ValloxSensorEntityDescription
    _state_proxy: Any
    _attr_name: Any
    _attr_available: bool
    def __init__(self, name: str, state_proxy: ValloxStateProxy, description: ValloxSensorEntityDescription) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    def _update_callback(self) -> None: ...
    _attr_native_value: Any
    async def async_update(self) -> None: ...

class ValloxProfileSensor(ValloxSensor):
    _attr_available: bool
    _attr_native_value: Any
    async def async_update(self) -> None: ...

class ValloxFanSpeedSensor(ValloxSensor):
    _attr_available: bool
    _attr_native_value: int
    async def async_update(self) -> None: ...

class ValloxFilterRemainingSensor(ValloxSensor):
    _attr_available: bool
    _attr_native_value: Any
    async def async_update(self) -> None: ...

class ValloxSensorEntityDescription(SensorEntityDescription):
    metric_key: Union[str, None]
    sensor_type: type[ValloxSensor]

SENSORS: tuple[ValloxSensorEntityDescription, ...]

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: Union[DiscoveryInfoType, None] = ...) -> None: ...
