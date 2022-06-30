from .const import CONNECTED_PLC_DEVICES as CONNECTED_PLC_DEVICES, CONNECTED_TO_ROUTER as CONNECTED_TO_ROUTER, DOMAIN as DOMAIN
from .entity import DevoloEntity as DevoloEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from devolo_plc_api.device import Device as Device
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription, DEVICE_CLASS_PLUG as DEVICE_CLASS_PLUG
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator

def _is_connected_to_router(entity: DevoloBinarySensorEntity) -> bool: ...

class DevoloBinarySensorRequiredKeysMixin:
    value_func: Callable[[DevoloBinarySensorEntity], bool]
    def __init__(self, value_func) -> None: ...

class DevoloBinarySensorEntityDescription(BinarySensorEntityDescription, DevoloBinarySensorRequiredKeysMixin):
    def __init__(self, value_func, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, unit_of_measurement) -> None: ...

SENSOR_TYPES: dict[str, DevoloBinarySensorEntityDescription]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DevoloBinarySensorEntity(DevoloEntity, BinarySensorEntity):
    entity_description: Incomplete
    def __init__(self, coordinator: DataUpdateCoordinator, description: DevoloBinarySensorEntityDescription, device: Device, device_name: str) -> None: ...
    @property
    def is_on(self) -> bool: ...
