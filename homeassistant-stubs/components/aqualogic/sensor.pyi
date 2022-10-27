from . import AquaLogicProcessor as AquaLogicProcessor, DOMAIN as DOMAIN, UPDATE_TOPIC as UPDATE_TOPIC
from _typeshed import Incomplete
from homeassistant.components.sensor import PLATFORM_SCHEMA as PLATFORM_SCHEMA, SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.const import CONF_MONITORED_CONDITIONS as CONF_MONITORED_CONDITIONS, PERCENTAGE as PERCENTAGE, POWER_WATT as POWER_WATT, TEMP_CELSIUS as TEMP_CELSIUS, TEMP_FAHRENHEIT as TEMP_FAHRENHEIT
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType

class AquaLogicSensorEntityDescription(SensorEntityDescription):
    unit_metric: Union[str, None]
    unit_imperial: Union[str, None]
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, unit_of_measurement, suggested_unit_of_measurement, last_reset, native_unit_of_measurement, state_class, unit_metric, unit_imperial) -> None: ...

SENSOR_TYPES: tuple[AquaLogicSensorEntityDescription, ...]
SENSOR_KEYS: list[str]

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: Union[DiscoveryInfoType, None] = ...) -> None: ...

class AquaLogicSensor(SensorEntity):
    entity_description: AquaLogicSensorEntityDescription
    _attr_should_poll: bool
    _processor: Incomplete
    _attr_name: Incomplete
    def __init__(self, processor: AquaLogicProcessor, description: AquaLogicSensorEntityDescription) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    _attr_native_unit_of_measurement: Incomplete
    _attr_native_value: Incomplete
    def async_update_callback(self) -> None: ...
