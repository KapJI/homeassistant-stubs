from .const import DOMAIN as DOMAIN
from .coordinator import LunatoneConfigEntry as LunatoneConfigEntry, LunatoneSensorsDataUpdateCoordinator as LunatoneSensorsDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import CONCENTRATION_PARTS_PER_BILLION as CONCENTRATION_PARTS_PER_BILLION, CONCENTRATION_PARTS_PER_MILLION as CONCENTRATION_PARTS_PER_MILLION, LIGHT_LUX as LIGHT_LUX, PERCENTAGE as PERCENTAGE, UnitOfPressure as UnitOfPressure, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from lunatone_rest_api_client import Sensor as Sensor
from typing import Final, override

PARALLEL_UPDATES: int
SENSOR_TYPES: Final[dict[str, SensorEntityDescription]]

async def async_setup_entry(hass: HomeAssistant, config_entry: LunatoneConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LunatoneSensor(CoordinatorEntity[LunatoneSensorsDataUpdateCoordinator], SensorEntity):
    _attr_has_entity_name: bool
    entity_description: Incomplete
    _config_entry_unique_id: Incomplete
    _sensor_id: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: LunatoneSensorsDataUpdateCoordinator, description: SensorEntityDescription, sensor_id: int, config_entry_unique_id: str) -> None: ...
    @property
    def sensor(self) -> Sensor: ...
    @property
    @override
    def available(self) -> bool: ...
    @property
    @override
    def native_value(self) -> float | None: ...
