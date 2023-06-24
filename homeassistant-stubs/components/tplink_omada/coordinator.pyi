from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from tplink_omada_client.omadaclient import OmadaSiteClient as OmadaSiteClient
from typing import Generic, TypeVar

_LOGGER: Incomplete
T = TypeVar('T')

class OmadaCoordinator(DataUpdateCoordinator[dict[str, T]], Generic[T]):
    omada_client: Incomplete
    def __init__(self, hass: HomeAssistant, omada_client: OmadaSiteClient, name: str, poll_delay: int = ...) -> None: ...
    async def _async_update_data(self) -> dict[str, T]: ...
    async def poll_update(self) -> dict[str, T]: ...
