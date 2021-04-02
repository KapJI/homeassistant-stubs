from homeassistant.const import SERVICE_TOGGLE as SERVICE_TOGGLE, SERVICE_TURN_OFF as SERVICE_TURN_OFF, SERVICE_TURN_ON as SERVICE_TURN_ON, STATE_ON as STATE_ON
from homeassistant.helpers.config_validation import PLATFORM_SCHEMA as PLATFORM_SCHEMA, PLATFORM_SCHEMA_BASE as PLATFORM_SCHEMA_BASE
from homeassistant.helpers.entity import ToggleEntity as ToggleEntity
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.loader import bind_hass as bind_hass
from typing import Any

DOMAIN: str
SCAN_INTERVAL: Any
ENTITY_ID_FORMAT: Any
ATTR_TODAY_ENERGY_KWH: str
ATTR_CURRENT_POWER_W: str
MIN_TIME_BETWEEN_SCANS: Any
PROP_TO_ATTR: Any
DEVICE_CLASS_OUTLET: str
DEVICE_CLASS_SWITCH: str
DEVICE_CLASSES: Any
DEVICE_CLASSES_SCHEMA: Any
_LOGGER: Any

def is_on(hass: Any, entity_id: Any): ...
async def async_setup(hass: Any, config: Any): ...
async def async_setup_entry(hass: Any, entry: Any): ...
async def async_unload_entry(hass: Any, entry: Any): ...

class SwitchEntity(ToggleEntity):
    @property
    def current_power_w(self) -> None: ...
    @property
    def today_energy_kwh(self) -> None: ...
    @property
    def is_standby(self) -> None: ...
    @property
    def state_attributes(self): ...
    @property
    def device_class(self) -> None: ...

class SwitchDevice(SwitchEntity):
    def __init_subclass__(cls, **kwargs: Any) -> None: ...
