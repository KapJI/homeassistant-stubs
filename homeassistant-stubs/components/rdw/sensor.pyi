from .const import CONF_LICENSE_PLATE as CONF_LICENSE_PLATE, DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from datetime import date
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator
from vehicle import Vehicle as Vehicle

class RDWSensorEntityDescriptionMixin:
    value_fn: Callable[[Vehicle], Union[date, str, float, None]]
    def __init__(self, value_fn) -> None: ...

class RDWSensorEntityDescription(SensorEntityDescription, RDWSensorEntityDescriptionMixin):
    def __init__(self, value_fn, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, unit_of_measurement, suggested_unit_of_measurement, last_reset, native_unit_of_measurement, state_class) -> None: ...

SENSORS: tuple[RDWSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RDWSensorEntity(CoordinatorEntity, SensorEntity):
    entity_description: RDWSensorEntityDescription
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, *, coordinator: DataUpdateCoordinator, license_plate: str, description: RDWSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> Union[date, str, float, None]: ...
