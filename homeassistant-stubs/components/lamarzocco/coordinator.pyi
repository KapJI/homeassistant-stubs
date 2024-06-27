from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_MODEL as CONF_MODEL, CONF_NAME as CONF_NAME, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from lmcloud.client_bluetooth import LaMarzoccoBluetoothClient as LaMarzoccoBluetoothClient
from lmcloud.client_cloud import LaMarzoccoCloudClient as LaMarzoccoCloudClient
from lmcloud.client_local import LaMarzoccoLocalClient as LaMarzoccoLocalClient

SCAN_INTERVAL: Incomplete
FIRMWARE_UPDATE_INTERVAL: int
STATISTICS_UPDATE_INTERVAL: int
_LOGGER: Incomplete

class LaMarzoccoUpdateCoordinator(DataUpdateCoordinator[None]):
    config_entry: ConfigEntry
    local_connection_configured: Incomplete
    device: Incomplete
    _last_firmware_data_update: Incomplete
    _last_statistics_data_update: Incomplete
    _local_client: Incomplete
    def __init__(self, hass: HomeAssistant, cloud_client: LaMarzoccoCloudClient, local_client: LaMarzoccoLocalClient | None, bluetooth_client: LaMarzoccoBluetoothClient | None) -> None: ...
    async def async_setup(self) -> None: ...
    async def _async_update_data(self) -> None: ...
    async def _async_handle_request(self, func: Callable[_P, Coroutine[None, None, None]], *args: _P.args, **kwargs: _P.kwargs) -> None: ...
