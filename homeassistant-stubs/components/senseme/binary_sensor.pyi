from .const import DOMAIN as DOMAIN
from .entity import SensemeEntity as SensemeEntity
from _typeshed import Incomplete
from aiosenseme import SensemeDevice as SensemeDevice
from homeassistant import config_entries as config_entries
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, entry: config_entries.ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class HASensemeOccupancySensor(SensemeEntity, BinarySensorEntity):
    _attr_unique_id: Incomplete
    _attr_device_class: Incomplete
    def __init__(self, device: SensemeDevice) -> None: ...
    _attr_is_on: Incomplete
    def _async_update_attrs(self) -> None: ...
