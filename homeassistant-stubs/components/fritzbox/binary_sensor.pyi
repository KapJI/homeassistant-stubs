from . import FritzBoxEntity as FritzBoxEntity
from .const import CONF_COORDINATOR as CONF_COORDINATOR
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity, DEVICE_CLASS_WINDOW as DEVICE_CLASS_WINDOW
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_DEVICE_CLASS as ATTR_DEVICE_CLASS, ATTR_ENTITY_ID as ATTR_ENTITY_ID, ATTR_NAME as ATTR_NAME, ATTR_UNIT_OF_MEASUREMENT as ATTR_UNIT_OF_MEASUREMENT
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class FritzboxBinarySensor(FritzBoxEntity, BinarySensorEntity):
    @property
    def is_on(self) -> bool: ...
