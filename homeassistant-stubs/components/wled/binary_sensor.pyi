from .const import DOMAIN as DOMAIN
from .coordinator import WLEDDataUpdateCoordinator as WLEDDataUpdateCoordinator
from .models import WLEDEntity as WLEDEntity
from _typeshed import Incomplete
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class WLEDUpdateBinarySensor(WLEDEntity, BinarySensorEntity):
    _attr_entity_category: Incomplete
    _attr_device_class: Incomplete
    _attr_name: str
    _attr_entity_registry_enabled_default: bool
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: WLEDDataUpdateCoordinator) -> None: ...
    @property
    def is_on(self) -> bool: ...
