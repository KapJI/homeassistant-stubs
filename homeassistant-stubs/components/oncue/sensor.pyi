from .const import DOMAIN as DOMAIN
from .entity import OncueEntity as OncueEntity
from aiooncue import OncueDevice as OncueDevice, OncueSensor as OncueSensor
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ELECTRIC_CURRENT_AMPERE as ELECTRIC_CURRENT_AMPERE, ELECTRIC_POTENTIAL_VOLT as ELECTRIC_POTENTIAL_VOLT, ENERGY_KILO_WATT_HOUR as ENERGY_KILO_WATT_HOUR, FREQUENCY_HERTZ as FREQUENCY_HERTZ, PERCENTAGE as PERCENTAGE, POWER_WATT as POWER_WATT, PRESSURE_PSI as PRESSURE_PSI, TEMP_CELSIUS as TEMP_CELSIUS, TEMP_FAHRENHEIT as TEMP_FAHRENHEIT
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from typing import Any

SENSOR_TYPES: tuple[SensorEntityDescription, ...]
SENSOR_MAP: Any
UNIT_MAPPINGS: Any

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class OncueSensorEntity(OncueEntity, SensorEntity):
    _attr_native_unit_of_measurement: Any
    def __init__(self, coordinator: DataUpdateCoordinator, device_id: str, device: OncueDevice, sensor: OncueSensor, description: SensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> str: ...
