from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.backports.enum import StrEnum as StrEnum
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import SERVICE_TOGGLE as SERVICE_TOGGLE, SERVICE_TURN_OFF as SERVICE_TURN_OFF, SERVICE_TURN_ON as SERVICE_TURN_ON, STATE_ON as STATE_ON
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.config_validation import PLATFORM_SCHEMA as PLATFORM_SCHEMA, PLATFORM_SCHEMA_BASE as PLATFORM_SCHEMA_BASE
from homeassistant.helpers.entity import ToggleEntity as ToggleEntity, ToggleEntityDescription as ToggleEntityDescription
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.loader import bind_hass as bind_hass

SCAN_INTERVAL: Incomplete
ENTITY_ID_FORMAT: Incomplete
MIN_TIME_BETWEEN_SCANS: Incomplete
_LOGGER: Incomplete

class SwitchDeviceClass(StrEnum):
    OUTLET: str
    SWITCH: str

DEVICE_CLASSES_SCHEMA: Incomplete
DEVICE_CLASSES: Incomplete
DEVICE_CLASS_OUTLET: Incomplete
DEVICE_CLASS_SWITCH: Incomplete

def is_on(hass: HomeAssistant, entity_id: str) -> bool: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class SwitchEntityDescription(ToggleEntityDescription):
    device_class: Union[SwitchDeviceClass, None]
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement) -> None: ...

class SwitchEntity(ToggleEntity):
    entity_description: SwitchEntityDescription
    _attr_device_class: Union[SwitchDeviceClass, None]
    @property
    def device_class(self) -> Union[SwitchDeviceClass, None]: ...
