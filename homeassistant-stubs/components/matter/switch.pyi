from .entity import MatterEntity as MatterEntity, MatterEntityDescription as MatterEntityDescription
from .helpers import get_matter as get_matter
from .models import MatterDiscoverySchema as MatterDiscoverySchema
from _typeshed import Incomplete
from chip.clusters.Objects import ClusterCommand as ClusterCommand
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.switch import SwitchDeviceClass as SwitchDeviceClass, SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any

EVSE_SUPPLY_STATE_MAP: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class MatterSwitch(MatterEntity, SwitchEntity):
    _platform_translation_key: str
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    _attr_is_on: Incomplete
    @callback
    def _update_from_device(self) -> None: ...

class MatterGenericCommandSwitch(MatterSwitch):
    entity_description: MatterGenericCommandSwitchEntityDescription
    _platform_translation_key: str
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    _attr_is_on: Incomplete
    @callback
    def _update_from_device(self) -> None: ...
    async def send_device_command(self, command: ClusterCommand, command_timeout: int | None = None, **kwargs: Any) -> None: ...

@dataclass(frozen=True)
class MatterGenericCommandSwitchEntityDescription(SwitchEntityDescription, MatterEntityDescription):
    on_command: Callable[[], Any] | None = ...
    off_command: Callable[[], Any] | None = ...
    command_timeout: int | None = ...

@dataclass(frozen=True)
class MatterNumericSwitchEntityDescription(SwitchEntityDescription, MatterEntityDescription): ...

class MatterNumericSwitch(MatterSwitch):
    entity_description: MatterNumericSwitchEntityDescription
    async def _async_set_native_value(self, value: bool) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    _attr_is_on: Incomplete
    @callback
    def _update_from_device(self) -> None: ...

DISCOVERY_SCHEMAS: Incomplete
