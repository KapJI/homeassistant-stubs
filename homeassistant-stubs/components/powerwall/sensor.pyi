from .const import DOMAIN as DOMAIN, POWERWALL_COORDINATOR as POWERWALL_COORDINATOR
from .entity import PowerWallEntity as PowerWallEntity
from .models import PowerwallRuntimeData as PowerwallRuntimeData
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import PERCENTAGE as PERCENTAGE, UnitOfElectricCurrent as UnitOfElectricCurrent, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfEnergy as UnitOfEnergy, UnitOfFrequency as UnitOfFrequency, UnitOfPower as UnitOfPower
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from tesla_powerwall import Meter as Meter, MeterType as MeterType

_METER_DIRECTION_EXPORT: str
_METER_DIRECTION_IMPORT: str

class PowerwallRequiredKeysMixin:
    value_fn: Callable[[Meter], float]
    def __init__(self, value_fn) -> None: ...

class PowerwallSensorEntityDescription(SensorEntityDescription, PowerwallRequiredKeysMixin):
    def __init__(self, value_fn, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement) -> None: ...

def _get_meter_power(meter: Meter) -> float: ...
def _get_meter_frequency(meter: Meter) -> float: ...
def _get_meter_total_current(meter: Meter) -> float: ...
def _get_meter_average_voltage(meter: Meter) -> float: ...

POWERWALL_INSTANT_SENSORS: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class PowerWallChargeSensor(PowerWallEntity, SensorEntity):
    _attr_translation_key: str
    _attr_state_class: Incomplete
    _attr_native_unit_of_measurement = PERCENTAGE
    _attr_device_class: Incomplete
    @property
    def unique_id(self) -> str: ...
    @property
    def native_value(self) -> int: ...

class PowerWallEnergySensor(PowerWallEntity, SensorEntity):
    entity_description: PowerwallSensorEntityDescription
    _meter: Incomplete
    _attr_translation_key: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, powerwall_data: PowerwallRuntimeData, meter: MeterType, description: PowerwallSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> float: ...

class PowerWallBackupReserveSensor(PowerWallEntity, SensorEntity):
    _attr_translation_key: str
    _attr_state_class: Incomplete
    _attr_native_unit_of_measurement = PERCENTAGE
    _attr_device_class: Incomplete
    @property
    def unique_id(self) -> str: ...
    @property
    def native_value(self) -> int | None: ...

class PowerWallEnergyDirectionSensor(PowerWallEntity, SensorEntity):
    _attr_state_class: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    _attr_device_class: Incomplete
    _meter: Incomplete
    _attr_translation_key: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, powerwall_data: PowerwallRuntimeData, meter: MeterType, meter_direction: str) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def meter(self) -> Meter: ...

class PowerWallExportSensor(PowerWallEnergyDirectionSensor):
    def __init__(self, powerwall_data: PowerwallRuntimeData, meter: MeterType) -> None: ...
    @property
    def native_value(self) -> float: ...

class PowerWallImportSensor(PowerWallEnergyDirectionSensor):
    def __init__(self, powerwall_data: PowerwallRuntimeData, meter: MeterType) -> None: ...
    @property
    def native_value(self) -> float: ...
