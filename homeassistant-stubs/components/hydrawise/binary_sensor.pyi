from .const import DOMAIN as DOMAIN
from .coordinator import HydrawiseDataUpdateCoordinator as HydrawiseDataUpdateCoordinator
from .entity import HydrawiseEntity as HydrawiseEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

@dataclass(frozen=True, kw_only=True)
class HydrawiseBinarySensorEntityDescription(BinarySensorEntityDescription):
    value_fn: Callable[[HydrawiseBinarySensor], bool | None]
    always_available: bool = ...
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, value_fn, always_available) -> None: ...

CONTROLLER_BINARY_SENSORS: tuple[HydrawiseBinarySensorEntityDescription, ...]
RAIN_SENSOR_BINARY_SENSOR: tuple[HydrawiseBinarySensorEntityDescription, ...]
ZONE_BINARY_SENSORS: tuple[HydrawiseBinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class HydrawiseBinarySensor(HydrawiseEntity, BinarySensorEntity):
    entity_description: HydrawiseBinarySensorEntityDescription
    _attr_is_on: Incomplete
    def _update_attrs(self) -> None: ...
    @property
    def available(self) -> bool: ...
