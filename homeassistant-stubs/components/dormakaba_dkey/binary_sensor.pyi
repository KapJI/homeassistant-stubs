from .const import DOMAIN as DOMAIN
from .entity import DormakabaDkeyEntity as DormakabaDkeyEntity
from .models import DormakabaDkeyData as DormakabaDkeyData
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from py_dormakaba_dkey import DKEYLock as DKEYLock
from py_dormakaba_dkey.commands import Notifications as Notifications

class DormakabaDkeyBinarySensorDescriptionMixin:
    is_on: Callable[[Notifications], bool]
    def __init__(self, is_on) -> None: ...

class DormakabaDkeyBinarySensorDescription(BinarySensorEntityDescription, DormakabaDkeyBinarySensorDescriptionMixin):
    def __init__(self, is_on, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement) -> None: ...

BINARY_SENSOR_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DormakabaDkeyBinarySensor(DormakabaDkeyEntity, BinarySensorEntity):
    _attr_has_entity_name: bool
    entity_description: DormakabaDkeyBinarySensorDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: DataUpdateCoordinator[None], lock: DKEYLock, description: DormakabaDkeyBinarySensorDescription) -> None: ...
    _attr_is_on: Incomplete
    def _async_update_attrs(self) -> None: ...
