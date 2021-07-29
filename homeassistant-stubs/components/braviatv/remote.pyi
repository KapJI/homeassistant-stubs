from . import BraviaTVCoordinator as BraviaTVCoordinator
from .const import ATTR_MANUFACTURER as ATTR_MANUFACTURER, DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN
from collections.abc import Iterable
from homeassistant.components.remote import ATTR_NUM_REPEATS as ATTR_NUM_REPEATS, RemoteEntity as RemoteEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class BraviaTVRemote(CoordinatorEntity, RemoteEntity):
    coordinator: BraviaTVCoordinator
    _attr_device_info: Any
    _attr_name: Any
    _attr_unique_id: Any
    def __init__(self, coordinator: BraviaTVCoordinator, name: str, unique_id: str, device_info: DeviceInfo) -> None: ...
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_send_command(self, command: Iterable[str], **kwargs: Any) -> None: ...
