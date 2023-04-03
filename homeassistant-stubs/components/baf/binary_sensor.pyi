from .const import DOMAIN as DOMAIN
from .entity import BAFEntity as BAFEntity
from .models import BAFData as BAFData
from _typeshed import Incomplete
from aiobafi6 import Device as Device
from collections.abc import Callable as Callable
from homeassistant import config_entries as config_entries
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

class BAFBinarySensorDescriptionMixin:
    value_fn: Callable[[Device], bool | None]
    def __init__(self, value_fn) -> None: ...

class BAFBinarySensorDescription(BinarySensorEntityDescription, BAFBinarySensorDescriptionMixin):
    def __init__(self, value_fn, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement) -> None: ...

OCCUPANCY_SENSORS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: config_entries.ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class BAFBinarySensor(BAFEntity, BinarySensorEntity):
    entity_description: BAFBinarySensorDescription
    _attr_unique_id: Incomplete
    def __init__(self, device: Device, description: BAFBinarySensorDescription) -> None: ...
    _attr_is_on: Incomplete
    def _async_update_attrs(self) -> None: ...
