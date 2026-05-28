from . import VistapoolConfigEntry as VistapoolConfigEntry
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from aioaquarite import AquariteAuth as AquariteAuth, AquariteClient, ResilientPoolSubscription as ResilientPoolSubscription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import Any

_LOGGER: Incomplete

class VistapoolDataUpdateCoordinator(DataUpdateCoordinator[dict[str, Any]]):
    config_entry: VistapoolConfigEntry
    auth: Incomplete
    api: Incomplete
    pool_id: str
    pool_name: str
    subscription: ResilientPoolSubscription | None
    def __init__(self, hass: HomeAssistant, entry: VistapoolConfigEntry, auth: AquariteAuth, api: AquariteClient, pool_id: str, pool_name: str) -> None: ...
    async def _async_update_data(self) -> dict[str, Any]: ...
    async def subscribe(self) -> None: ...
    async def async_shutdown(self) -> None: ...
    def get_value(self, path: str, default: Any = None) -> Any: ...
