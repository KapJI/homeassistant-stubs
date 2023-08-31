from .const import DOMAIN as DOMAIN
from .coordinator import WLEDDataUpdateCoordinator as WLEDDataUpdateCoordinator
from .models import WLEDEntity as WLEDEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, SIGNAL_STRENGTH_DECIBELS_MILLIWATT as SIGNAL_STRENGTH_DECIBELS_MILLIWATT, UnitOfElectricCurrent as UnitOfElectricCurrent, UnitOfInformation as UnitOfInformation
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.util.dt import utcnow as utcnow
from wled import Device as WLEDDevice

class WLEDSensorEntityDescriptionMixin:
    value_fn: Callable[[WLEDDevice], datetime | StateType]
    def __init__(self, value_fn) -> None: ...

class WLEDSensorEntityDescription(SensorEntityDescription, WLEDSensorEntityDescriptionMixin):
    exists_fn: Callable[[WLEDDevice], bool]
    def __init__(self, value_fn, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement, exists_fn) -> None: ...

SENSORS: tuple[WLEDSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class WLEDSensorEntity(WLEDEntity, SensorEntity):
    entity_description: WLEDSensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: WLEDDataUpdateCoordinator, description: WLEDSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> datetime | StateType: ...
