from . import AquaLogicProcessor as AquaLogicProcessor, DOMAIN as DOMAIN, UPDATE_TOPIC as UPDATE_TOPIC
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.const import CONF_MONITORED_CONDITIONS as CONF_MONITORED_CONDITIONS, PERCENTAGE as PERCENTAGE, UnitOfPower as UnitOfPower, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType

@dataclass(frozen=True)
class AquaLogicSensorEntityDescription(SensorEntityDescription):
    unit_metric: str | None = ...
    unit_imperial: str | None = ...
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., last_reset=..., native_unit_of_measurement=..., options=..., state_class=..., suggested_display_precision=..., suggested_unit_of_measurement=..., unit_metric=..., unit_imperial=...) -> None: ...

SENSOR_TYPES: tuple[AquaLogicSensorEntityDescription, ...]
SENSOR_KEYS: list[str]
PLATFORM_SCHEMA: Incomplete

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...

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
