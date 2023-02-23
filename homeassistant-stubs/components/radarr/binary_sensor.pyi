from . import RadarrEntity as RadarrEntity
from .const import DOMAIN as DOMAIN, HEALTH_ISSUES as HEALTH_ISSUES
from _typeshed import Incomplete
from aiopyarr import Health
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

BINARY_SENSOR_TYPE: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RadarrBinarySensor(RadarrEntity[list[Health]], BinarySensorEntity):
    @property
    def is_on(self) -> bool: ...
