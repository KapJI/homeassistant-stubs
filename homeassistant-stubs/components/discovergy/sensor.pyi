from . import DiscovergyData as DiscovergyData, DiscovergyUpdateCoordinator as DiscovergyUpdateCoordinator
from .const import DOMAIN as DOMAIN, MANUFACTURER as MANUFACTURER
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfEnergy as UnitOfEnergy, UnitOfPower as UnitOfPower, UnitOfVolume as UnitOfVolume
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from pydiscovergy.models import Meter as Meter, Reading as Reading

PARALLEL_UPDATES: int

class DiscovergyMixin:
    value_fn: Callable[[Reading, str, int], datetime | float | None]
    alternative_keys: list[str]
    scale: int
    def __init__(self, value_fn, alternative_keys, scale) -> None: ...

class DiscovergySensorEntityDescription(DiscovergyMixin, SensorEntityDescription):
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement, value_fn, alternative_keys, scale) -> None: ...

GAS_SENSORS: tuple[DiscovergySensorEntityDescription, ...]
ELECTRICITY_SENSORS: tuple[DiscovergySensorEntityDescription, ...]
ADDITIONAL_SENSORS: tuple[DiscovergySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DiscovergySensor(CoordinatorEntity[DiscovergyUpdateCoordinator], SensorEntity):
    entity_description: DiscovergySensorEntityDescription
    data_key: str
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, data_key: str, description: DiscovergySensorEntityDescription, meter: Meter, coordinator: DiscovergyUpdateCoordinator) -> None: ...
    @property
    def native_value(self) -> datetime | float | None: ...
