from .const import CONF_IMPORTED_BY as CONF_IMPORTED_BY
from .coordinator import PingConfigEntry as PingConfigEntry, PingUpdateCoordinator as PingUpdateCoordinator
from .entity import PingEntity as PingEntity
from _typeshed import Incomplete
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, entry: PingConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class PingBinarySensor(PingEntity, BinarySensorEntity):
    _attr_device_class: Incomplete
    _attr_available: bool
    _attr_name: Incomplete
    _attr_entity_registry_enabled_default: Incomplete
    def __init__(self, config_entry: PingConfigEntry, coordinator: PingUpdateCoordinator) -> None: ...
    @property
    def is_on(self) -> bool: ...
