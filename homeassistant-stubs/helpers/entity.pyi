import asyncio
from abc import ABC
from collections.abc import Awaitable, Iterable, Mapping, MutableMapping
from datetime import datetime, timedelta
from homeassistant.config import DATA_CUSTOMIZE as DATA_CUSTOMIZE
from homeassistant.const import ATTR_ASSUMED_STATE as ATTR_ASSUMED_STATE, ATTR_DEVICE_CLASS as ATTR_DEVICE_CLASS, ATTR_ENTITY_PICTURE as ATTR_ENTITY_PICTURE, ATTR_FRIENDLY_NAME as ATTR_FRIENDLY_NAME, ATTR_ICON as ATTR_ICON, ATTR_SUPPORTED_FEATURES as ATTR_SUPPORTED_FEATURES, ATTR_UNIT_OF_MEASUREMENT as ATTR_UNIT_OF_MEASUREMENT, DEVICE_DEFAULT_NAME as DEVICE_DEFAULT_NAME, STATE_OFF as STATE_OFF, STATE_ON as STATE_ON, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN, TEMP_CELSIUS as TEMP_CELSIUS, TEMP_FAHRENHEIT as TEMP_FAHRENHEIT
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, Context as Context, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, NoEntitySpecifiedError as NoEntitySpecifiedError
from homeassistant.helpers.entity_platform import EntityPlatform as EntityPlatform
from homeassistant.helpers.entity_registry import RegistryEntry as RegistryEntry
from homeassistant.helpers.event import Event as Event, async_track_entity_registry_updated_event as async_track_entity_registry_updated_event
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.loader import bind_hass as bind_hass
from homeassistant.util import ensure_unique_string as ensure_unique_string, slugify as slugify
from typing import Any, TypedDict

_LOGGER: Any
SLOW_UPDATE_WARNING: int
DATA_ENTITY_SOURCE: str
SOURCE_CONFIG_ENTRY: str
SOURCE_PLATFORM_CONFIG: str
FLOAT_PRECISION: Any

def entity_sources(hass: HomeAssistant) -> dict[str, dict[str, str]]: ...
def generate_entity_id(entity_id_format: str, name: Union[str, None], current_ids: Union[list[str], None] = ..., hass: Union[HomeAssistant, None] = ...) -> str: ...
def async_generate_entity_id(entity_id_format: str, name: Union[str, None], current_ids: Union[Iterable[str], None] = ..., hass: Union[HomeAssistant, None] = ...) -> str: ...
def get_capability(hass: HomeAssistant, entity_id: str, capability: str) -> Union[Any, None]: ...
def get_device_class(hass: HomeAssistant, entity_id: str) -> Union[str, None]: ...
def get_supported_features(hass: HomeAssistant, entity_id: str) -> int: ...
def get_unit_of_measurement(hass: HomeAssistant, entity_id: str) -> Union[str, None]: ...

class DeviceInfo(TypedDict):
    name: Union[str, None]
    connections: set[tuple[str, str]]
    identifiers: set[tuple[str, str]]
    manufacturer: Union[str, None]
    model: Union[str, None]
    suggested_area: Union[str, None]
    sw_version: Union[str, None]
    via_device: tuple[str, str]
    entry_type: Union[str, None]
    default_name: str
    default_manufacturer: str
    default_model: str

class EntityDescription:
    key: str
    device_class: Union[str, None]
    entity_registry_enabled_default: bool
    force_update: bool
    icon: Union[str, None]
    name: Union[str, None]
    unit_of_measurement: Union[str, None]

class Entity(ABC):
    entity_id: str
    hass: HomeAssistant
    platform: Union[EntityPlatform, None]
    entity_description: EntityDescription
    _slow_reported: bool
    _disabled_reported: bool
    _update_staged: bool
    parallel_updates: Union[asyncio.Semaphore, None]
    registry_entry: Union[RegistryEntry, None]
    _on_remove: Union[list[CALLBACK_TYPE], None]
    _context: Union[Context, None]
    _context_set: Union[datetime, None]
    _added: bool
    _attr_assumed_state: bool
    _attr_available: bool
    _attr_context_recent_time: timedelta
    _attr_device_class: Union[str, None]
    _attr_device_info: Union[DeviceInfo, None]
    _attr_entity_picture: Union[str, None]
    _attr_entity_registry_enabled_default: bool
    _attr_extra_state_attributes: MutableMapping[str, Any]
    _attr_force_update: bool
    _attr_icon: Union[str, None]
    _attr_name: Union[str, None]
    _attr_should_poll: bool
    _attr_state: StateType
    _attr_supported_features: Union[int, None]
    _attr_unique_id: Union[str, None]
    _attr_unit_of_measurement: Union[str, None]
    @property
    def should_poll(self) -> bool: ...
    @property
    def unique_id(self) -> Union[str, None]: ...
    @property
    def name(self) -> Union[str, None]: ...
    @property
    def state(self) -> StateType: ...
    @property
    def capability_attributes(self) -> Union[Mapping[str, Any], None]: ...
    @property
    def state_attributes(self) -> Union[dict[str, Any], None]: ...
    @property
    def device_state_attributes(self) -> Union[Mapping[str, Any], None]: ...
    @property
    def extra_state_attributes(self) -> Union[Mapping[str, Any], None]: ...
    @property
    def device_info(self) -> Union[DeviceInfo, None]: ...
    @property
    def device_class(self) -> Union[str, None]: ...
    @property
    def unit_of_measurement(self) -> Union[str, None]: ...
    @property
    def icon(self) -> Union[str, None]: ...
    @property
    def entity_picture(self) -> Union[str, None]: ...
    @property
    def available(self) -> bool: ...
    @property
    def assumed_state(self) -> bool: ...
    @property
    def force_update(self) -> bool: ...
    @property
    def supported_features(self) -> Union[int, None]: ...
    @property
    def context_recent_time(self) -> timedelta: ...
    @property
    def entity_registry_enabled_default(self) -> bool: ...
    @property
    def enabled(self) -> bool: ...
    def async_set_context(self, context: Context) -> None: ...
    async def async_update_ha_state(self, force_refresh: bool = ...) -> None: ...
    def async_write_ha_state(self) -> None: ...
    def _stringify_state(self) -> str: ...
    def _async_write_ha_state(self) -> None: ...
    def schedule_update_ha_state(self, force_refresh: bool = ...) -> None: ...
    def async_schedule_update_ha_state(self, force_refresh: bool = ...) -> None: ...
    async def async_device_update(self, warning: bool = ...) -> None: ...
    def async_on_remove(self, func: CALLBACK_TYPE) -> None: ...
    async def async_removed_from_registry(self) -> None: ...
    def add_to_platform_start(self, hass: HomeAssistant, platform: EntityPlatform, parallel_updates: Union[asyncio.Semaphore, None]) -> None: ...
    def add_to_platform_abort(self) -> None: ...
    async def add_to_platform_finish(self) -> None: ...
    async def async_remove(self, *, force_remove: bool = ...) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    async def async_internal_added_to_hass(self) -> None: ...
    async def async_internal_will_remove_from_hass(self) -> None: ...
    async def _async_registry_updated(self, event: Event) -> None: ...
    def __eq__(self, other: Any) -> bool: ...
    def __repr__(self) -> str: ...
    async def async_request_call(self, coro: Awaitable) -> None: ...
    def _suggest_report_issue(self) -> str: ...

class ToggleEntityDescription(EntityDescription): ...

class ToggleEntity(Entity):
    entity_description: ToggleEntityDescription
    _attr_is_on: bool
    _attr_state: None
    @property
    def state(self) -> Union[str, None]: ...
    @property
    def is_on(self) -> bool: ...
    def turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    def turn_off(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    def toggle(self, **kwargs: Any) -> None: ...
    async def async_toggle(self, **kwargs: Any) -> None: ...
