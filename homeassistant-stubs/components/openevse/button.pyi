from .const import DOMAIN as DOMAIN
from .coordinator import OpenEVSEConfigEntry as OpenEVSEConfigEntry, OpenEVSEDataUpdateCoordinator as OpenEVSEDataUpdateCoordinator
from .helpers import openevse_exception_handler as openevse_exception_handler
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.const import ATTR_CONNECTIONS as ATTR_CONNECTIONS, ATTR_SERIAL_NUMBER as ATTR_SERIAL_NUMBER, EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from openevsehttp.__main__ import OpenEVSE as OpenEVSE
from typing import Any, override

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class OpenEVSEButtonDescription(ButtonEntityDescription):
    press_fn: Callable[[OpenEVSE], Awaitable[Any]]

BUTTON_TYPES: tuple[OpenEVSEButtonDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: OpenEVSEConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class OpenEVSEButton(CoordinatorEntity[OpenEVSEDataUpdateCoordinator], ButtonEntity):
    _attr_has_entity_name: bool
    entity_description: OpenEVSEButtonDescription
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: OpenEVSEDataUpdateCoordinator, description: OpenEVSEButtonDescription, identifier: str, unique_id: str | None) -> None: ...
    @override
    async def async_press(self) -> None: ...
