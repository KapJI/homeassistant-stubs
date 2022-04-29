from .const import DOMAIN as DOMAIN
from .entity import OncueEntity as OncueEntity
from _typeshed import Incomplete
from aiooncue import OncueDevice as OncueDevice
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator

SENSOR_TYPES: tuple[BinarySensorEntityDescription, ...]
SENSOR_MAP: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class OncueBinarySensorEntity(OncueEntity, BinarySensorEntity):
    @property
    def is_on(self) -> bool: ...
