from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import STATE_OFF as STATE_OFF, STATE_ON as STATE_ON
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.config_validation import PLATFORM_SCHEMA as PLATFORM_SCHEMA, PLATFORM_SCHEMA_BASE as PLATFORM_SCHEMA_BASE
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.typing import ConfigType as ConfigType, StateType as StateType
from typing import Any

_LOGGER: Any
DOMAIN: str
SCAN_INTERVAL: Any
ENTITY_ID_FORMAT: Any
DEVICE_CLASS_BATTERY: str
DEVICE_CLASS_BATTERY_CHARGING: str
DEVICE_CLASS_COLD: str
DEVICE_CLASS_CONNECTIVITY: str
DEVICE_CLASS_DOOR: str
DEVICE_CLASS_GARAGE_DOOR: str
DEVICE_CLASS_GAS: str
DEVICE_CLASS_HEAT: str
DEVICE_CLASS_LIGHT: str
DEVICE_CLASS_LOCK: str
DEVICE_CLASS_MOISTURE: str
DEVICE_CLASS_MOTION: str
DEVICE_CLASS_MOVING: str
DEVICE_CLASS_OCCUPANCY: str
DEVICE_CLASS_OPENING: str
DEVICE_CLASS_PLUG: str
DEVICE_CLASS_POWER: str
DEVICE_CLASS_PRESENCE: str
DEVICE_CLASS_PROBLEM: str
DEVICE_CLASS_SAFETY: str
DEVICE_CLASS_SMOKE: str
DEVICE_CLASS_SOUND: str
DEVICE_CLASS_VIBRATION: str
DEVICE_CLASS_WINDOW: str
DEVICE_CLASSES: Any
DEVICE_CLASSES_SCHEMA: Any

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class BinarySensorEntity(Entity):
    _attr_is_on: Union[bool, None]
    _attr_state: None
    @property
    def is_on(self) -> Union[bool, None]: ...
    @property
    def state(self) -> StateType: ...

class BinarySensorDevice(BinarySensorEntity):
    def __init_subclass__(cls, **kwargs: Any): ...
