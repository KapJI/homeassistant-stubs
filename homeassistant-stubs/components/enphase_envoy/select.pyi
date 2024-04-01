from .const import DOMAIN as DOMAIN
from .coordinator import EnphaseUpdateCoordinator as EnphaseUpdateCoordinator
from .entity import EnvoyBaseEntity as EnvoyBaseEntity
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pyenphase import Envoy as Envoy, EnvoyDryContactSettings as EnvoyDryContactSettings
from pyenphase.models.tariff import EnvoyStorageSettings as EnvoyStorageSettings
from typing import Any

@dataclass(frozen=True, kw_only=True)
class EnvoyRelaySelectEntityDescription(SelectEntityDescription):
    value_fn: Callable[[EnvoyDryContactSettings], str]
    update_fn: Callable[[Envoy, EnvoyDryContactSettings, str], Coroutine[Any, Any, dict[str, Any]]]
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, options, value_fn, update_fn) -> None: ...

@dataclass(frozen=True, kw_only=True)
class EnvoyStorageSettingsSelectEntityDescription(SelectEntityDescription):
    value_fn: Callable[[EnvoyStorageSettings], str]
    update_fn: Callable[[Envoy, str], Awaitable[dict[str, Any]]]
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, options, value_fn, update_fn) -> None: ...

RELAY_MODE_MAP: Incomplete
REVERSE_RELAY_MODE_MAP: Incomplete
RELAY_ACTION_MAP: Incomplete
REVERSE_RELAY_ACTION_MAP: Incomplete
MODE_OPTIONS: Incomplete
ACTION_OPTIONS: Incomplete
STORAGE_MODE_MAP: Incomplete
REVERSE_STORAGE_MODE_MAP: Incomplete
STORAGE_MODE_OPTIONS: Incomplete
RELAY_ENTITIES: Incomplete
STORAGE_MODE_ENTITY: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class EnvoyRelaySelectEntity(EnvoyBaseEntity, SelectEntity):
    entity_description: EnvoyRelaySelectEntityDescription
    envoy: Incomplete
    _relay_id: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: EnphaseUpdateCoordinator, description: EnvoyRelaySelectEntityDescription, relay_id: str) -> None: ...
    @property
    def relay(self) -> EnvoyDryContactSettings: ...
    @property
    def current_option(self) -> str: ...
    async def async_select_option(self, option: str) -> None: ...

class EnvoyStorageSettingsSelectEntity(EnvoyBaseEntity, SelectEntity):
    entity_description: EnvoyStorageSettingsSelectEntityDescription
    envoy: Incomplete
    _serial_number: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: EnphaseUpdateCoordinator, description: EnvoyStorageSettingsSelectEntityDescription) -> None: ...
    @property
    def current_option(self) -> str: ...
    async def async_select_option(self, option: str) -> None: ...
