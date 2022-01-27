from homeassistant.backports.enum import StrEnum as StrEnum
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import SERVICE_TOGGLE as SERVICE_TOGGLE, SERVICE_TURN_OFF as SERVICE_TURN_OFF, SERVICE_TURN_ON as SERVICE_TURN_ON, STATE_ON as STATE_ON
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.config_validation import PLATFORM_SCHEMA as PLATFORM_SCHEMA, PLATFORM_SCHEMA_BASE as PLATFORM_SCHEMA_BASE
from homeassistant.helpers.entity import ToggleEntity as ToggleEntity, ToggleEntityDescription as ToggleEntityDescription
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.loader import bind_hass as bind_hass
from typing import Any

DOMAIN: str
SCAN_INTERVAL: Any
ENTITY_ID_FORMAT: Any
ATTR_TODAY_ENERGY_KWH: str
ATTR_CURRENT_POWER_W: str
MIN_TIME_BETWEEN_SCANS: Any
PROP_TO_ATTR: Any
_LOGGER: Any

class SwitchDeviceClass(StrEnum):
    OUTLET: str
    SWITCH: str

DEVICE_CLASSES_SCHEMA: Any
DEVICE_CLASSES: Any
DEVICE_CLASS_OUTLET: Any
DEVICE_CLASS_SWITCH: Any

def is_on(hass: HomeAssistant, entity_id: str) -> bool: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class SwitchEntityDescription(ToggleEntityDescription):
    device_class: Union[SwitchDeviceClass, str, None]
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, force_update, icon, name, unit_of_measurement) -> None: ...

class SwitchEntity(ToggleEntity):
    entity_description: SwitchEntityDescription
    _attr_current_power_w: Union[float, None]
    _attr_device_class: Union[SwitchDeviceClass, str, None]
    _attr_today_energy_kwh: Union[float, None]
    @property
    def current_power_w(self) -> Union[float, None]: ...
    @property
    def device_class(self) -> Union[SwitchDeviceClass, str, None]: ...
    @property
    def today_energy_kwh(self) -> Union[float, None]: ...
    @property
    def state_attributes(self) -> Union[dict[str, Any], None]: ...
