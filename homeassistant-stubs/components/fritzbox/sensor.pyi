from . import FritzBoxEntity as FritzBoxEntity
from .const import ATTR_STATE_DEVICE_LOCKED as ATTR_STATE_DEVICE_LOCKED, ATTR_STATE_LOCKED as ATTR_STATE_LOCKED, CONF_COORDINATOR as CONF_COORDINATOR
from .model import SensorExtraAttributes as SensorExtraAttributes
from homeassistant.components.sensor import SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_DEVICE_CLASS as ATTR_DEVICE_CLASS, ATTR_ENTITY_ID as ATTR_ENTITY_ID, ATTR_NAME as ATTR_NAME, ATTR_UNIT_OF_MEASUREMENT as ATTR_UNIT_OF_MEASUREMENT, DEVICE_CLASS_BATTERY as DEVICE_CLASS_BATTERY, PERCENTAGE as PERCENTAGE, TEMP_CELSIUS as TEMP_CELSIUS
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class FritzBoxBatterySensor(FritzBoxEntity, SensorEntity):
    @property
    def state(self) -> Union[int, None]: ...

class FritzBoxTempSensor(FritzBoxEntity, SensorEntity):
    @property
    def state(self) -> Union[float, None]: ...
    @property
    def extra_state_attributes(self) -> SensorExtraAttributes: ...
