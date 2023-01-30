import python_otbr_api
from . import websocket_api as websocket_api
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any, Concatenate, TypeVar

_R = TypeVar('_R')
_P: Incomplete

def _handle_otbr_error(func: Callable[Concatenate[OTBRData, _P], Coroutine[Any, Any, _R]]) -> Callable[Concatenate[OTBRData, _P], Coroutine[Any, Any, _R]]: ...

class OTBRData:
    url: str
    api: python_otbr_api.OTBR
    async def get_active_dataset_tlvs(self) -> Union[bytes, None]: ...
    def __init__(self, url, api) -> None: ...

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_get_active_dataset_tlvs(hass: HomeAssistant) -> Union[bytes, None]: ...
