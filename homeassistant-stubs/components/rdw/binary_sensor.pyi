from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator
from vehicle import Vehicle as Vehicle

class RDWBinarySensorEntityDescriptionMixin:
    is_on_fn: Callable[[Vehicle], Union[bool, None]]
    def __init__(self, is_on_fn) -> None: ...

class RDWBinarySensorEntityDescription(BinarySensorEntityDescription, RDWBinarySensorEntityDescriptionMixin):
    def __init__(self, is_on_fn, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, unit_of_measurement) -> None: ...

BINARY_SENSORS: tuple[RDWBinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RDWBinarySensorEntity(CoordinatorEntity, BinarySensorEntity):
    entity_description: RDWBinarySensorEntityDescription
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, *, coordinator: DataUpdateCoordinator, description: RDWBinarySensorEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool: ...
