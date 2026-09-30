from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from .device_catalog import MIDEA_DEVICE_NAMES as MIDEA_DEVICE_NAMES
from _typeshed import Incomplete
from collections.abc import Generator
from contextlib import contextmanager
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import Entity as Entity, EntityDescription as EntityDescription
from midealocal.device import MideaDevice
from typing import Any, override

type MideaConfigEntry = ConfigEntry[MideaDevice]
@contextmanager
def midea_api_call() -> Generator[None]: ...

class MideaEntity(Entity):
    _attr_has_entity_name: bool
    _attr_should_poll: bool
    _device: Incomplete
    _unique_id: Incomplete
    _device_name: Incomplete
    entity_description: Incomplete
    def __init__(self, device: MideaDevice, entity_description: EntityDescription) -> None: ...
    @override
    async def async_added_to_hass(self) -> None: ...
    @override
    async def async_will_remove_from_hass(self) -> None: ...
    @property
    @override
    def device_info(self) -> DeviceInfo: ...
    @property
    @override
    def unique_id(self) -> str: ...
    @property
    @override
    def available(self) -> bool: ...
    def update_state(self, status: Any) -> None: ...
