from .entity import MatterEntity as MatterEntity, MatterEntityDescription as MatterEntityDescription
from .helpers import MatterConfigEntry as MatterConfigEntry
from .models import MatterDiscoverySchema as MatterDiscoverySchema
from _typeshed import Incomplete
from asyncio import Lock
from chip.clusters.Objects import ClusterCommand as ClusterCommand
from collections.abc import Callable as Callable
from dataclasses import dataclass, field
from homeassistant.components.switch import SwitchDeviceClass as SwitchDeviceClass, SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.const import EntityCategory as EntityCategory, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from matter_server.client.models.node import MatterEndpoint as MatterEndpoint
from typing import Any, override
from weakref import WeakKeyDictionary

EVSE_SUPPLY_STATE_MAP: Incomplete
ALARM_MODE_VISUAL: Incomplete
ALARM_MODE_AUDIBLE: Incomplete
BOOLEAN_STATE_CONFIGURATION_FEATURE_VISUAL: Incomplete
BOOLEAN_STATE_CONFIGURATION_FEATURE_AUDIBLE: Incomplete

@dataclass
class _AlarmEnabledState:
    lock: Lock = field(default_factory=Lock)
    pending_alarms_enabled: int | None = ...

ALARM_ENABLED_STATES: WeakKeyDictionary[MatterEndpoint, _AlarmEnabledState]

async def async_setup_entry(hass: HomeAssistant, config_entry: MatterConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

@dataclass(frozen=True, kw_only=True)
class MatterSwitchEntityDescription(SwitchEntityDescription, MatterEntityDescription):
    inverted: bool = ...

class MatterSwitch(MatterEntity, SwitchEntity):
    entity_description: MatterSwitchEntityDescription
    _platform_translation_key: str
    def _get_command_for_value(self, value: bool) -> ClusterCommand: ...
    @override
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @override
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    _attr_is_on: Incomplete
    @callback
    @override
    def _update_from_device(self) -> None: ...

class MatterGenericCommandSwitch(MatterSwitch):
    entity_description: MatterGenericCommandSwitchEntityDescription
    _platform_translation_key: str
    @override
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @override
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    _attr_is_on: Incomplete
    @callback
    @override
    def _update_from_device(self) -> None: ...
    @override
    async def send_device_command(self, command: ClusterCommand, command_timeout: int | None = None, **kwargs: Any) -> None: ...

@dataclass(frozen=True, kw_only=True)
class MatterGenericCommandSwitchEntityDescription(MatterSwitchEntityDescription):
    on_command: Callable[[], Any] | None = ...
    off_command: Callable[[], Any] | None = ...
    command_timeout: int | None = ...

@dataclass(frozen=True, kw_only=True)
class MatterNumericSwitchEntityDescription(MatterSwitchEntityDescription): ...

class MatterNumericSwitch(MatterSwitch):
    entity_description: MatterNumericSwitchEntityDescription
    async def _async_set_native_value(self, value: bool) -> None: ...
    @override
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @override
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    _attr_is_on: Incomplete
    @callback
    @override
    def _update_from_device(self) -> None: ...

@dataclass(frozen=True, kw_only=True)
class MatterAlarmEnabledSwitchEntityDescription(MatterSwitchEntityDescription):
    alarm_mode: int

class MatterAlarmEnabledSwitch(MatterSwitch):
    entity_description: MatterAlarmEnabledSwitchEntityDescription
    async def _async_set_alarm_enabled(self, value: bool) -> None: ...
    @override
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @override
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    _attr_available: Incomplete
    _attr_is_on: Incomplete
    @callback
    @override
    def _update_from_device(self) -> None: ...

DISCOVERY_SCHEMAS: Incomplete
