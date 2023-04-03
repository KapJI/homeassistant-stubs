from . import PureEnergieData as PureEnergieData, PureEnergieDataUpdateCoordinator as PureEnergieDataUpdateCoordinator
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, UnitOfEnergy as UnitOfEnergy, UnitOfPower as UnitOfPower
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class PureEnergieSensorEntityDescriptionMixin:
    value_fn: Callable[[PureEnergieData], int | float]
    def __init__(self, value_fn) -> None: ...

class PureEnergieSensorEntityDescription(SensorEntityDescription, PureEnergieSensorEntityDescriptionMixin):
    def __init__(self, value_fn, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement) -> None: ...

SENSORS: tuple[PureEnergieSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class PureEnergieSensorEntity(CoordinatorEntity[PureEnergieDataUpdateCoordinator], SensorEntity):
    entity_description: PureEnergieSensorEntityDescription
    entity_id: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, *, coordinator: PureEnergieDataUpdateCoordinator, description: PureEnergieSensorEntityDescription, entry: ConfigEntry) -> None: ...
    @property
    def native_value(self) -> int | float: ...
