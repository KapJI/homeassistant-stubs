from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from tplink_omada_client import OmadaSiteClient as OmadaSiteClient

_LOGGER: Incomplete

class OmadaCoordinator(DataUpdateCoordinator[dict[str, _T]]):
    omada_client: Incomplete
    def __init__(self, hass: HomeAssistant, omada_client: OmadaSiteClient, name: str, poll_delay: int = 300) -> None: ...
    async def _async_update_data(self) -> dict[str, _T]: ...
    async def poll_update(self) -> dict[str, _T]: ...
