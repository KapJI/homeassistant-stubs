from .const import DATA_COMPONENT as DATA_COMPONENT, DEVICE_CLASSES_SCHEMA as DEVICE_CLASSES_SCHEMA, DOMAIN as DOMAIN, SwitchDeviceClass as SwitchDeviceClass
from .services import async_setup_services as async_setup_services
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import SERVICE_TOGGLE as SERVICE_TOGGLE, SERVICE_TURN_OFF as SERVICE_TURN_OFF, SERVICE_TURN_ON as SERVICE_TURN_ON, STATE_ON as STATE_ON
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import ToggleEntity as ToggleEntity, ToggleEntityDescription as ToggleEntityDescription
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.typing import ConfigType as ConfigType
from propcache.api import cached_property
from typing import override

_LOGGER: Incomplete
ENTITY_ID_FORMAT: Incomplete
PLATFORM_SCHEMA: Incomplete
PLATFORM_SCHEMA_BASE: Incomplete
SCAN_INTERVAL: Incomplete
MIN_TIME_BETWEEN_SCANS: Incomplete
DEVICE_CLASSES: Incomplete

def is_on(hass: HomeAssistant, entity_id: str) -> bool: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class SwitchEntityDescription(ToggleEntityDescription, frozen_or_thawed=True):
    device_class: SwitchDeviceClass | None = ...

CACHED_PROPERTIES_WITH_ATTR_: Incomplete

class SwitchEntity(ToggleEntity, cached_properties=CACHED_PROPERTIES_WITH_ATTR_):
    entity_description: SwitchEntityDescription
    _attr_device_class: SwitchDeviceClass | None
    @cached_property
    @override
    def device_class(self) -> SwitchDeviceClass | None: ...
