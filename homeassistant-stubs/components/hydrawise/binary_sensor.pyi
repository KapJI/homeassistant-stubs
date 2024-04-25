from .const import DOMAIN as DOMAIN
from .coordinator import HydrawiseDataUpdateCoordinator as HydrawiseDataUpdateCoordinator
from .entity import HydrawiseEntity as HydrawiseEntity
from _typeshed import Incomplete
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pydrawise.schema import Zone as Zone

BINARY_SENSOR_STATUS: Incomplete
BINARY_SENSOR_TYPES: tuple[BinarySensorEntityDescription, ...]
BINARY_SENSOR_KEYS: list[str]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class HydrawiseBinarySensor(HydrawiseEntity, BinarySensorEntity):
    _attr_is_on: Incomplete
    def _update_attrs(self) -> None: ...
