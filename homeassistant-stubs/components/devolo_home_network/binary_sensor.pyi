from . import DevoloHomeNetworkConfigEntry as DevoloHomeNetworkConfigEntry
from .const import CONNECTED_PLC_DEVICES as CONNECTED_PLC_DEVICES, CONNECTED_TO_ROUTER as CONNECTED_TO_ROUTER
from .entity import DevoloCoordinatorEntity as DevoloCoordinatorEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from devolo_plc_api.plcnet_api import LogicalNetwork
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator

def _is_connected_to_router(entity: DevoloBinarySensorEntity) -> bool: ...

@dataclass(frozen=True, kw_only=True)
class DevoloBinarySensorEntityDescription(BinarySensorEntityDescription):
    value_func: Callable[[DevoloBinarySensorEntity], bool]
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, value_func) -> None: ...

SENSOR_TYPES: dict[str, DevoloBinarySensorEntityDescription]

async def async_setup_entry(hass: HomeAssistant, entry: DevoloHomeNetworkConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DevoloBinarySensorEntity(DevoloCoordinatorEntity[LogicalNetwork], BinarySensorEntity):
    entity_description: Incomplete
    def __init__(self, entry: DevoloHomeNetworkConfigEntry, coordinator: DataUpdateCoordinator[LogicalNetwork], description: DevoloBinarySensorEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool: ...
