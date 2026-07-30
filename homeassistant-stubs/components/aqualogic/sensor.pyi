from . import AquaLogicConfigEntry as AquaLogicConfigEntry, AquaLogicProcessor as AquaLogicProcessor
from .const import UPDATE_TOPIC as UPDATE_TOPIC
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.const import PERCENTAGE as PERCENTAGE, UnitOfPower as UnitOfPower, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import override

@dataclass(frozen=True)
class AquaLogicSensorEntityDescription(SensorEntityDescription):
    unit_metric: str | None = ...
    unit_imperial: str | None = ...

SENSOR_TYPES: tuple[AquaLogicSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: AquaLogicConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class AquaLogicSensor(SensorEntity):
    entity_description: AquaLogicSensorEntityDescription
    _attr_should_poll: bool
    _processor: Incomplete
    _attr_name: Incomplete
    def __init__(self, processor: AquaLogicProcessor, description: AquaLogicSensorEntityDescription) -> None: ...
    @override
    async def async_added_to_hass(self) -> None: ...
    _attr_native_unit_of_measurement: Incomplete
    _attr_native_value: Incomplete
    @callback
    def async_update_callback(self) -> None: ...
