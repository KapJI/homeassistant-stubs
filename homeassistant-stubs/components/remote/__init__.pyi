from _typeshed import Incomplete
from collections.abc import Iterable
from dataclasses import dataclass
from enum import IntFlag
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_COMMAND as ATTR_COMMAND, SERVICE_TOGGLE as SERVICE_TOGGLE, SERVICE_TURN_OFF as SERVICE_TURN_OFF, SERVICE_TURN_ON as SERVICE_TURN_ON, STATE_ON as STATE_ON
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.config_validation import PLATFORM_SCHEMA as PLATFORM_SCHEMA, PLATFORM_SCHEMA_BASE as PLATFORM_SCHEMA_BASE, make_entity_service_schema as make_entity_service_schema
from homeassistant.helpers.entity import ToggleEntity as ToggleEntity, ToggleEntityDescription as ToggleEntityDescription
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.loader import bind_hass as bind_hass
from typing import Any

_LOGGER: Incomplete
ATTR_ACTIVITY: str
ATTR_ACTIVITY_LIST: str
ATTR_CURRENT_ACTIVITY: str
ATTR_COMMAND_TYPE: str
ATTR_DEVICE: str
ATTR_NUM_REPEATS: str
ATTR_DELAY_SECS: str
ATTR_HOLD_SECS: str
ATTR_ALTERNATIVE: str
ATTR_TIMEOUT: str
DOMAIN: str
SCAN_INTERVAL: Incomplete
ENTITY_ID_FORMAT: Incomplete
MIN_TIME_BETWEEN_SCANS: Incomplete
SERVICE_SEND_COMMAND: str
SERVICE_LEARN_COMMAND: str
SERVICE_DELETE_COMMAND: str
SERVICE_SYNC: str
DEFAULT_NUM_REPEATS: int
DEFAULT_DELAY_SECS: float
DEFAULT_HOLD_SECS: int

class RemoteEntityFeature(IntFlag):
    LEARN_COMMAND: int
    DELETE_COMMAND: int
    ACTIVITY: int

SUPPORT_LEARN_COMMAND: int
SUPPORT_DELETE_COMMAND: int
SUPPORT_ACTIVITY: int
REMOTE_SERVICE_ACTIVITY_SCHEMA: Incomplete

def is_on(hass: HomeAssistant, entity_id: str) -> bool: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

@dataclass
class RemoteEntityDescription(ToggleEntityDescription):
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement) -> None: ...

class RemoteEntity(ToggleEntity):
    entity_description: RemoteEntityDescription
    _attr_activity_list: list[str] | None
    _attr_current_activity: str | None
    _attr_supported_features: RemoteEntityFeature
    @property
    def supported_features(self) -> RemoteEntityFeature: ...
    @property
    def current_activity(self) -> str | None: ...
    @property
    def activity_list(self) -> list[str] | None: ...
    @property
    def state_attributes(self) -> dict[str, Any] | None: ...
    def send_command(self, command: Iterable[str], **kwargs: Any) -> None: ...
    async def async_send_command(self, command: Iterable[str], **kwargs: Any) -> None: ...
    def learn_command(self, **kwargs: Any) -> None: ...
    async def async_learn_command(self, **kwargs: Any) -> None: ...
    def delete_command(self, **kwargs: Any) -> None: ...
    async def async_delete_command(self, **kwargs: Any) -> None: ...
