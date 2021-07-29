from . import FritzBoxEntity as FritzBoxEntity
from .const import ATTR_STATE_DEVICE_LOCKED as ATTR_STATE_DEVICE_LOCKED, ATTR_STATE_LOCKED as ATTR_STATE_LOCKED, CONF_COORDINATOR as CONF_COORDINATOR
from .model import SensorExtraAttributes as SensorExtraAttributes
from datetime import datetime
from homeassistant.components.sensor import ATTR_STATE_CLASS as ATTR_STATE_CLASS, STATE_CLASS_MEASUREMENT as STATE_CLASS_MEASUREMENT, SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_DEVICE_CLASS as ATTR_DEVICE_CLASS, ATTR_ENTITY_ID as ATTR_ENTITY_ID, ATTR_NAME as ATTR_NAME, ATTR_UNIT_OF_MEASUREMENT as ATTR_UNIT_OF_MEASUREMENT, DEVICE_CLASS_BATTERY as DEVICE_CLASS_BATTERY, DEVICE_CLASS_ENERGY as DEVICE_CLASS_ENERGY, DEVICE_CLASS_POWER as DEVICE_CLASS_POWER, DEVICE_CLASS_TEMPERATURE as DEVICE_CLASS_TEMPERATURE, ENERGY_KILO_WATT_HOUR as ENERGY_KILO_WATT_HOUR, PERCENTAGE as PERCENTAGE, POWER_WATT as POWER_WATT, TEMP_CELSIUS as TEMP_CELSIUS
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.util.dt import utc_from_timestamp as utc_from_timestamp

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class FritzBoxBatterySensor(FritzBoxEntity, SensorEntity):
    @property
    def state(self) -> Union[int, None]: ...

class FritzBoxPowerSensor(FritzBoxEntity, SensorEntity):
    @property
    def state(self) -> Union[float, None]: ...

class FritzBoxEnergySensor(FritzBoxEntity, SensorEntity):
    @property
    def state(self) -> Union[float, None]: ...
    @property
    def last_reset(self) -> datetime: ...

class FritzBoxTempSensor(FritzBoxEntity, SensorEntity):
    @property
    def state(self) -> Union[float, None]: ...
    @property
    def extra_state_attributes(self) -> SensorExtraAttributes: ...
