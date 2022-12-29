from .const import ATTR_OPTION as ATTR_OPTION, ATTR_OPTIONS as ATTR_OPTIONS, DOMAIN as DOMAIN, SERVICE_SELECT_OPTION as SERVICE_SELECT_OPTION
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall
from homeassistant.helpers.config_validation import PLATFORM_SCHEMA as PLATFORM_SCHEMA, PLATFORM_SCHEMA_BASE as PLATFORM_SCHEMA_BASE
from homeassistant.helpers.entity import Entity as Entity, EntityDescription as EntityDescription
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

SCAN_INTERVAL: Incomplete
ENTITY_ID_FORMAT: Incomplete
MIN_TIME_BETWEEN_SCANS: Incomplete
_LOGGER: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_select_option(entity: SelectEntity, service_call: ServiceCall) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class SelectEntityDescription(EntityDescription):
    options: Union[list[str], None]
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, options) -> None: ...

class SelectEntity(Entity):
    entity_description: SelectEntityDescription
    _attr_current_option: Union[str, None]
    _attr_options: list[str]
    _attr_state: None
    @property
    def capability_attributes(self) -> dict[str, Any]: ...
    @property
    def state(self) -> Union[str, None]: ...
    @property
    def options(self) -> list[str]: ...
    @property
    def current_option(self) -> Union[str, None]: ...
    def select_option(self, option: str) -> None: ...
    async def async_select_option(self, option: str) -> None: ...
