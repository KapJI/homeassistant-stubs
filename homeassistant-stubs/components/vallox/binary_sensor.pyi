from . import ValloxDataUpdateCoordinator as ValloxDataUpdateCoordinator
from .const import DOMAIN as DOMAIN
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

class ValloxBinarySensor(CoordinatorEntity[ValloxDataUpdateCoordinator], BinarySensorEntity):
    entity_description: ValloxBinarySensorEntityDescription
    _attr_name: Any
    _attr_unique_id: Any
    def __init__(self, name: str, coordinator: ValloxDataUpdateCoordinator, description: ValloxBinarySensorEntityDescription) -> None: ...
    @property
    def is_on(self) -> Union[bool, None]: ...

class ValloxMetricKeyMixin:
    metric_key: str
    def __init__(self, metric_key) -> None: ...

class ValloxBinarySensorEntityDescription(BinarySensorEntityDescription, ValloxMetricKeyMixin):
    def __init__(self, metric_key, key, device_class, entity_category, entity_registry_enabled_default, force_update, icon, name, unit_of_measurement) -> None: ...

SENSORS: tuple[ValloxBinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
