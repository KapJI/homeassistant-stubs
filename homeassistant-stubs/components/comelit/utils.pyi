from .const import DOMAIN as DOMAIN, _LOGGER as _LOGGER
from .coordinator import ComelitBaseCoordinator as ComelitBaseCoordinator
from .entity import ComelitBridgeBaseEntity as ComelitBridgeBaseEntity
from aiocomelit.api import ComelitSerialBridgeObject, ComelitVedoAreaObject, ComelitVedoZoneObject
from aiohttp import ClientSession as ClientSession
from collections.abc import Awaitable, Callable as Callable, Coroutine
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import aiohttp_client as aiohttp_client
from typing import Any, Concatenate

DeviceType = ComelitSerialBridgeObject | ComelitVedoAreaObject | ComelitVedoZoneObject

async def async_client_session(hass: HomeAssistant) -> ClientSession: ...
def load_api_data(device: ComelitSerialBridgeObject, domain: str) -> list[Any]: ...
async def cleanup_stale_entity(hass: HomeAssistant, config_entry: ConfigEntry, entry_unique_id: str, device: ComelitSerialBridgeObject) -> None: ...
def _async_remove_state_config_entry_from_devices(hass: HomeAssistant, identifiers: list[str], config_entry: ConfigEntry) -> None: ...
def bridge_api_call[_T: ComelitBridgeBaseEntity, **_P](func: Callable[Concatenate[_T, _P], Awaitable[None]]) -> Callable[Concatenate[_T, _P], Coroutine[Any, Any, None]]: ...
def new_device_listener(coordinator: ComelitBaseCoordinator, new_devices_callback: Callable[[list[ComelitSerialBridgeObject | ComelitVedoAreaObject | ComelitVedoZoneObject], str], None], data_type: str) -> Callable[[], None]: ...
