from .const import DOMAIN as DOMAIN, SCAN_INTERVAL as SCAN_INTERVAL
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from switchbot_api import Device as Device, Remote, SwitchBotAPI as SwitchBotAPI

_LOGGER: Incomplete
Status: Incomplete

class SwitchBotCoordinator(DataUpdateCoordinator[Status]):
    _api: SwitchBotAPI
    _device_id: str
    _should_poll: bool
    def __init__(self, hass: HomeAssistant, api: SwitchBotAPI, device: Device | Remote) -> None: ...
    async def _async_update_data(self) -> Status: ...
