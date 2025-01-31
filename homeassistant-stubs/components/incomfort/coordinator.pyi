from _typeshed import Incomplete
from dataclasses import dataclass, field
from homeassistant.const import CONF_HOST as CONF_HOST
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryError as ConfigEntryError
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from incomfortclient import Gateway as InComfortGateway, Heater as InComfortHeater
from typing import Any

_LOGGER: Incomplete
UPDATE_INTERVAL: int

@dataclass
class InComfortData:
    client: InComfortGateway
    heaters: list[InComfortHeater] = field(default_factory=list)

async def async_connect_gateway(hass: HomeAssistant, entry_data: dict[str, Any]) -> InComfortData: ...

class InComfortDataCoordinator(DataUpdateCoordinator[InComfortData]):
    unique_id: Incomplete
    incomfort_data: Incomplete
    def __init__(self, hass: HomeAssistant, incomfort_data: InComfortData, unique_id: str | None) -> None: ...
    async def _async_update_data(self) -> InComfortData: ...
