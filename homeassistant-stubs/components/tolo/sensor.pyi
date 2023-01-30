from . import ToloSaunaCoordinatorEntity as ToloSaunaCoordinatorEntity, ToloSaunaUpdateCoordinator as ToloSaunaUpdateCoordinator
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import PERCENTAGE as PERCENTAGE, UnitOfTemperature as UnitOfTemperature, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from tololib.message_info import SettingsInfo as SettingsInfo, StatusInfo as StatusInfo

class ToloSensorEntityDescriptionBase:
    getter: Callable[[StatusInfo], Union[int, None]]
    availability_checker: Union[Callable[[SettingsInfo, StatusInfo], bool], None]
    def __init__(self, getter, availability_checker) -> None: ...

class ToloSensorEntityDescription(SensorEntityDescription, ToloSensorEntityDescriptionBase):
    state_class: Incomplete
    def __init__(self, getter, availability_checker, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, last_reset, native_precision, native_unit_of_measurement, options, state_class, suggested_unit_of_measurement) -> None: ...

SENSORS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ToloSensorEntity(ToloSaunaCoordinatorEntity, SensorEntity):
    entity_description: ToloSensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: ToloSaunaUpdateCoordinator, entry: ConfigEntry, entity_description: ToloSensorEntityDescription) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def native_value(self) -> Union[int, None]: ...
