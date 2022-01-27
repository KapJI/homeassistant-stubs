from .const import ATTR_MAX as ATTR_MAX, ATTR_MIN as ATTR_MIN, ATTR_STEP as ATTR_STEP, ATTR_VALUE as ATTR_VALUE, DEFAULT_MAX_VALUE as DEFAULT_MAX_VALUE, DEFAULT_MIN_VALUE as DEFAULT_MIN_VALUE, DEFAULT_STEP as DEFAULT_STEP, DOMAIN as DOMAIN, SERVICE_SET_VALUE as SERVICE_SET_VALUE
from homeassistant.backports.enum import StrEnum as StrEnum
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_MODE as ATTR_MODE
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall
from homeassistant.helpers.config_validation import PLATFORM_SCHEMA as PLATFORM_SCHEMA, PLATFORM_SCHEMA_BASE as PLATFORM_SCHEMA_BASE
from homeassistant.helpers.entity import Entity as Entity, EntityDescription as EntityDescription
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

SCAN_INTERVAL: Any
ENTITY_ID_FORMAT: Any
MIN_TIME_BETWEEN_SCANS: Any
_LOGGER: Any

class NumberMode(StrEnum):
    AUTO: str
    BOX: str
    SLIDER: str

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_set_value(entity: NumberEntity, service_call: ServiceCall) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class NumberEntityDescription(EntityDescription):
    max_value: Union[float, None]
    min_value: Union[float, None]
    step: Union[float, None]
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, force_update, icon, name, unit_of_measurement, max_value, min_value, step) -> None: ...

class NumberEntity(Entity):
    entity_description: NumberEntityDescription
    _attr_max_value: float
    _attr_min_value: float
    _attr_state: None
    _attr_step: float
    _attr_mode: NumberMode
    _attr_value: float
    @property
    def capability_attributes(self) -> dict[str, Any]: ...
    @property
    def min_value(self) -> float: ...
    @property
    def max_value(self) -> float: ...
    @property
    def step(self) -> float: ...
    @property
    def mode(self) -> NumberMode: ...
    @property
    def state(self) -> Union[float, None]: ...
    @property
    def value(self) -> Union[float, None]: ...
    def set_value(self, value: float) -> None: ...
    async def async_set_value(self, value: float) -> None: ...
