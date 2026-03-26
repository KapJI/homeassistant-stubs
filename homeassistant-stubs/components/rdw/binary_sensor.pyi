from .const import DOMAIN as DOMAIN
from .coordinator import RDWDataUpdateCoordinator as RDWDataUpdateCoordinator
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from vehicle import Vehicle as Vehicle

@dataclass(frozen=True, kw_only=True)
class RDWBinarySensorEntityDescription(BinarySensorEntityDescription):
    is_on_fn: Callable[[Vehicle], bool | None]

BINARY_SENSORS: tuple[RDWBinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class RDWBinarySensorEntity(CoordinatorEntity[RDWDataUpdateCoordinator], BinarySensorEntity):
    entity_description: RDWBinarySensorEntityDescription
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, *, coordinator: RDWDataUpdateCoordinator, description: RDWBinarySensorEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool: ...
