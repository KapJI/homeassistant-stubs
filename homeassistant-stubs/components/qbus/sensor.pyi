from .coordinator import QbusConfigEntry as QbusConfigEntry
from .entity import QbusEntity as QbusEntity, create_new_entities as create_new_entities, determine_new_outputs as determine_new_outputs
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import CONCENTRATION_PARTS_PER_MILLION as CONCENTRATION_PARTS_PER_MILLION, LIGHT_LUX as LIGHT_LUX, PERCENTAGE as PERCENTAGE, UnitOfElectricCurrent as UnitOfElectricCurrent, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfEnergy as UnitOfEnergy, UnitOfLength as UnitOfLength, UnitOfPower as UnitOfPower, UnitOfPressure as UnitOfPressure, UnitOfSoundPressure as UnitOfSoundPressure, UnitOfSpeed as UnitOfSpeed, UnitOfTemperature as UnitOfTemperature, UnitOfVolume as UnitOfVolume, UnitOfVolumeFlowRate as UnitOfVolumeFlowRate
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from qbusmqttapi.discovery import QbusMqttOutput as QbusMqttOutput
from qbusmqttapi.state import QbusMqttGaugeState, QbusMqttHumidityState, QbusMqttThermoState, QbusMqttVentilationState, QbusMqttWeatherState

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class QbusWeatherDescription(SensorEntityDescription):
    property: str

_WEATHER_DESCRIPTIONS: Incomplete
_GAUGE_VARIANT_DESCRIPTIONS: Incomplete

def _is_gauge_with_variant(output: QbusMqttOutput) -> bool: ...
def _is_ventilation_with_co2(output: QbusMqttOutput) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: QbusConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class QbusGaugeVariantSensor(QbusEntity, SensorEntity):
    _state_cls = QbusMqttGaugeState
    _attr_name: Incomplete
    _attr_suggested_display_precision: int
    entity_description: Incomplete
    def __init__(self, mqtt_output: QbusMqttOutput) -> None: ...
    _attr_native_value: Incomplete
    async def _handle_state_received(self, state: QbusMqttGaugeState) -> None: ...

class QbusHumiditySensor(QbusEntity, SensorEntity):
    _state_cls = QbusMqttHumidityState
    _attr_device_class: Incomplete
    _attr_name: Incomplete
    _attr_native_unit_of_measurement = PERCENTAGE
    _attr_state_class: Incomplete
    _attr_native_value: Incomplete
    async def _handle_state_received(self, state: QbusMqttHumidityState) -> None: ...

class QbusThermoSensor(QbusEntity, SensorEntity):
    _state_cls = QbusMqttThermoState
    _attr_device_class: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    _attr_state_class: Incomplete
    _attr_native_value: Incomplete
    async def _handle_state_received(self, state: QbusMqttThermoState) -> None: ...

class QbusVentilationSensor(QbusEntity, SensorEntity):
    _state_cls = QbusMqttVentilationState
    _attr_device_class: Incomplete
    _attr_name: Incomplete
    _attr_native_unit_of_measurement = CONCENTRATION_PARTS_PER_MILLION
    _attr_state_class: Incomplete
    _attr_suggested_display_precision: int
    _attr_native_value: Incomplete
    async def _handle_state_received(self, state: QbusMqttVentilationState) -> None: ...

class QbusWeatherSensor(QbusEntity, SensorEntity):
    _state_cls = QbusMqttWeatherState
    entity_description: QbusWeatherDescription
    _attr_name: Incomplete
    def __init__(self, mqtt_output: QbusMqttOutput, description: QbusWeatherDescription) -> None: ...
    native_value: Incomplete
    async def _handle_state_received(self, state: QbusMqttWeatherState) -> None: ...
