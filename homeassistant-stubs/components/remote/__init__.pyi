from _typeshed import Incomplete
from collections.abc import Iterable
from enum import IntFlag
from functools import cached_property as cached_property
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_COMMAND as ATTR_COMMAND, SERVICE_TOGGLE as SERVICE_TOGGLE, SERVICE_TURN_OFF as SERVICE_TURN_OFF, SERVICE_TURN_ON as SERVICE_TURN_ON, STATE_ON as STATE_ON
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.deprecation import DeprecatedConstantEnum as DeprecatedConstantEnum, all_with_deprecated_constants as all_with_deprecated_constants, check_if_deprecated_constant as check_if_deprecated_constant, dir_with_deprecated_constants as dir_with_deprecated_constants
from homeassistant.helpers.entity import ToggleEntity as ToggleEntity, ToggleEntityDescription as ToggleEntityDescription
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.loader import bind_hass as bind_hass
from homeassistant.util.hass_dict import HassKey as HassKey
from typing import Any

_LOGGER: Incomplete
DOMAIN: str
DATA_COMPONENT: HassKey[EntityComponent[RemoteEntity]]
ENTITY_ID_FORMAT: Incomplete
PLATFORM_SCHEMA: Incomplete
PLATFORM_SCHEMA_BASE: Incomplete
SCAN_INTERVAL: Incomplete
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
MIN_TIME_BETWEEN_SCANS: Incomplete
SERVICE_SEND_COMMAND: str
SERVICE_LEARN_COMMAND: str
SERVICE_DELETE_COMMAND: str
SERVICE_SYNC: str
DEFAULT_NUM_REPEATS: int
DEFAULT_DELAY_SECS: float
DEFAULT_HOLD_SECS: int

class RemoteEntityFeature(IntFlag):
    LEARN_COMMAND = 1
    DELETE_COMMAND = 2
    ACTIVITY = 4

_DEPRECATED_SUPPORT_LEARN_COMMAND: Incomplete
_DEPRECATED_SUPPORT_DELETE_COMMAND: Incomplete
_DEPRECATED_SUPPORT_ACTIVITY: Incomplete
REMOTE_SERVICE_ACTIVITY_SCHEMA: Incomplete

def is_on(hass: HomeAssistant, entity_id: str) -> bool: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class RemoteEntityDescription(ToggleEntityDescription, frozen_or_thawed=True):
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=...) -> None: ...
    def __replace__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=...) -> None: ...

CACHED_PROPERTIES_WITH_ATTR_: Incomplete

class RemoteEntity(ToggleEntity, cached_properties=CACHED_PROPERTIES_WITH_ATTR_):
    entity_description: RemoteEntityDescription
    _attr_activity_list: list[str] | None
    _attr_current_activity: str | None
    _attr_supported_features: RemoteEntityFeature
    @cached_property
    def supported_features(self) -> RemoteEntityFeature: ...
    @property
    def supported_features_compat(self) -> RemoteEntityFeature: ...
    @cached_property
    def current_activity(self) -> str | None: ...
    @cached_property
    def activity_list(self) -> list[str] | None: ...
    @property
    def state_attributes(self) -> dict[str, Any] | None: ...
    def send_command(self, command: Iterable[str], **kwargs: Any) -> None: ...
    async def async_send_command(self, command: Iterable[str], **kwargs: Any) -> None: ...
    def learn_command(self, **kwargs: Any) -> None: ...
    async def async_learn_command(self, **kwargs: Any) -> None: ...
    def delete_command(self, **kwargs: Any) -> None: ...
    async def async_delete_command(self, **kwargs: Any) -> None: ...

__getattr__: Incomplete
__dir__: Incomplete
__all__: Incomplete
