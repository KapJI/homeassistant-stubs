from . import PureEnergieData as PureEnergieData, PureEnergieDataUpdateCoordinator as PureEnergieDataUpdateCoordinator
from .const import DOMAIN as DOMAIN
from collections.abc import Callable as Callable
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, ENERGY_KILO_WATT_HOUR as ENERGY_KILO_WATT_HOUR, POWER_WATT as POWER_WATT
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

class PureEnergieSensorEntityDescriptionMixin:
    value_fn: Callable[[PureEnergieData], Union[int, float]]
    def __init__(self, value_fn) -> None: ...

class PureEnergieSensorEntityDescription(SensorEntityDescription, PureEnergieSensorEntityDescriptionMixin):
    def __init__(self, value_fn, key, device_class, entity_category, entity_registry_enabled_default, force_update, icon, name, unit_of_measurement, last_reset, native_unit_of_measurement, state_class) -> None: ...

SENSORS: tuple[PureEnergieSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class PureEnergieSensorEntity(CoordinatorEntity[PureEnergieData], SensorEntity):
    coordinator: PureEnergieDataUpdateCoordinator
    entity_description: PureEnergieSensorEntityDescription
    entity_id: Any
    _attr_unique_id: Any
    _attr_device_info: Any
    def __init__(self, coordinator: PureEnergieDataUpdateCoordinator, description: PureEnergieSensorEntityDescription, entry: ConfigEntry) -> None: ...
    @property
    def native_value(self) -> Union[int, float]: ...
