from .const import ATTR_FREQUENCY as ATTR_FREQUENCY, ATTR_INSTANT_AVERAGE_VOLTAGE as ATTR_INSTANT_AVERAGE_VOLTAGE, ATTR_INSTANT_TOTAL_CURRENT as ATTR_INSTANT_TOTAL_CURRENT, ATTR_IS_ACTIVE as ATTR_IS_ACTIVE, DOMAIN as DOMAIN, POWERWALL_COORDINATOR as POWERWALL_COORDINATOR
from .entity import PowerWallEntity as PowerWallEntity
from .models import PowerwallData as PowerwallData, PowerwallRuntimeData as PowerwallRuntimeData
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ENERGY_KILO_WATT_HOUR as ENERGY_KILO_WATT_HOUR, PERCENTAGE as PERCENTAGE, POWER_KILO_WATT as POWER_KILO_WATT
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from tesla_powerwall import Meter as Meter, MeterType as MeterType
from typing import Any

_METER_DIRECTION_EXPORT: str
_METER_DIRECTION_IMPORT: str

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class PowerWallChargeSensor(PowerWallEntity, SensorEntity):
    _attr_name: str
    _attr_state_class: Any
    _attr_native_unit_of_measurement: Any
    _attr_device_class: Any
    @property
    def unique_id(self) -> str: ...
    @property
    def native_value(self) -> int: ...

class PowerWallEnergySensor(PowerWallEntity, SensorEntity):
    _attr_state_class: Any
    _attr_native_unit_of_measurement: Any
    _attr_device_class: Any
    _meter: Any
    _attr_name: Any
    _attr_unique_id: Any
    def __init__(self, powerwall_data: PowerwallRuntimeData, meter: MeterType) -> None: ...
    @property
    def native_value(self) -> float: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...

class PowerWallEnergyDirectionSensor(PowerWallEntity, SensorEntity):
    _attr_state_class: Any
    _attr_native_unit_of_measurement: Any
    _attr_device_class: Any
    _meter: Any
    _attr_name: Any
    _attr_unique_id: Any
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
