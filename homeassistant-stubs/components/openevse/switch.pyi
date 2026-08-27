from .const import DOMAIN as DOMAIN
from .coordinator import OpenEVSEConfigEntry as OpenEVSEConfigEntry, OpenEVSEDataUpdateCoordinator as OpenEVSEDataUpdateCoordinator
from .helpers import openevse_exception_handler as openevse_exception_handler
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.const import ATTR_CONNECTIONS as ATTR_CONNECTIONS, ATTR_SERIAL_NUMBER as ATTR_SERIAL_NUMBER
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from openevsehttp import OpenEVSE as OpenEVSE
from typing import Any, override

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class OpenEVSESwitchDescription(SwitchEntityDescription):
    is_on_fn: Callable[[OpenEVSE], bool | None]
    turn_on_fn: Callable[[OpenEVSE], Awaitable[Any]]
    turn_off_fn: Callable[[OpenEVSE], Awaitable[Any]]

SWITCH_TYPES: tuple[OpenEVSESwitchDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: OpenEVSEConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class OpenEVSESwitch(CoordinatorEntity[OpenEVSEDataUpdateCoordinator], SwitchEntity):
    _attr_has_entity_name: bool
    entity_description: OpenEVSESwitchDescription
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: OpenEVSEDataUpdateCoordinator, description: OpenEVSESwitchDescription, identifier: str, unique_id: str | None) -> None: ...
    @property
    @override
    def available(self) -> bool: ...
    @property
    @override
    def is_on(self) -> bool | None: ...
    @override
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @override
    async def async_turn_off(self, **kwargs: Any) -> None: ...
