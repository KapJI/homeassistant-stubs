from . import AsekoDataUpdateCoordinator as AsekoDataUpdateCoordinator
from .const import DOMAIN as DOMAIN
from .entity import AsekoEntity as AsekoEntity
from aioaseko import Unit as Unit
from collections.abc import Callable as Callable
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

class AsekoBinarySensorDescriptionMixin:
    value_fn: Callable[[Unit], bool]
    def __init__(self, value_fn) -> None: ...

class AsekoBinarySensorEntityDescription(BinarySensorEntityDescription, AsekoBinarySensorDescriptionMixin):
    def __init__(self, value_fn, key, device_class, entity_category, entity_registry_enabled_default, force_update, icon, name, unit_of_measurement) -> None: ...

UNIT_BINARY_SENSORS: tuple[AsekoBinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AsekoUnitBinarySensorEntity(AsekoEntity, BinarySensorEntity):
    entity_description: AsekoBinarySensorEntityDescription
    _attr_name: Any
    _attr_unique_id: Any
    def __init__(self, unit: Unit, coordinator: AsekoDataUpdateCoordinator, entity_description: AsekoBinarySensorEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool: ...
