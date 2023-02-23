from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from tplink_omada_client.omadaclient import OmadaClient as OmadaClient
from typing import TypeVar

_LOGGER: Incomplete
T = TypeVar('T')

class OmadaCoordinator(DataUpdateCoordinator[dict[str, T]]):
    omada_client: Incomplete
    _update_func: Incomplete
    def __init__(self, hass: HomeAssistant, omada_client: OmadaClient, update_func: Callable[[OmadaClient], Awaitable[dict[str, T]]]) -> None: ...
    async def _async_update_data(self) -> dict[str, T]: ...
