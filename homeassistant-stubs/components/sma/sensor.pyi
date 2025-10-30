from . import SMAConfigEntry as SMAConfigEntry
from .const import DOMAIN as DOMAIN
from .coordinator import SMADataUpdateCoordinator as SMADataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_SSL as CONF_SSL, EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, UnitOfApparentPower as UnitOfApparentPower, UnitOfElectricCurrent as UnitOfElectricCurrent, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfEnergy as UnitOfEnergy, UnitOfFrequency as UnitOfFrequency, UnitOfPower as UnitOfPower, UnitOfReactivePower as UnitOfReactivePower, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from pysma.sensor import Sensor as Sensor

SENSOR_ENTITIES: dict[str, SensorEntityDescription]

async def async_setup_entry(hass: HomeAssistant, entry: SMAConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class SMAsensor(CoordinatorEntity[SMADataUpdateCoordinator], SensorEntity):
    entity_description: Incomplete
    _attr_name: Incomplete
    _sensor: Incomplete
    _serial: Incomplete
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: SMADataUpdateCoordinator, description: SensorEntityDescription | None, pysma_sensor: Sensor, entry: SMAConfigEntry) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def available(self) -> bool: ...
    @property
    def native_value(self) -> StateType: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
