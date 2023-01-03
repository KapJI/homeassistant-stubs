from .const import DOMAIN as DOMAIN, DeviceResponseEntry as DeviceResponseEntry
from .coordinator import HWEnergyDeviceUpdateCoordinator as HWEnergyDeviceUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ENERGY_KILO_WATT_HOUR as ENERGY_KILO_WATT_HOUR, PERCENTAGE as PERCENTAGE, POWER_WATT as POWER_WATT, VOLUME_CUBIC_METERS as VOLUME_CUBIC_METERS
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Final

_LOGGER: Incomplete
SENSORS: Final[tuple[SensorEntityDescription, ...]]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class HWEnergySensor(CoordinatorEntity[HWEnergyDeviceUpdateCoordinator], SensorEntity):
    _attr_has_entity_name: bool
    entity_description: Incomplete
    entry: Incomplete
    data_type: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    _attr_entity_registry_enabled_default: bool
    def __init__(self, coordinator: HWEnergyDeviceUpdateCoordinator, entry: ConfigEntry, description: SensorEntityDescription) -> None: ...
    @property
    def data(self) -> DeviceResponseEntry: ...
    @property
    def native_value(self) -> StateType: ...
    @property
    def available(self) -> bool: ...
