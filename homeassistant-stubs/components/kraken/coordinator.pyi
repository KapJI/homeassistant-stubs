from .const import CONF_TRACKED_ASSET_PAIRS as CONF_TRACKED_ASSET_PAIRS, DEFAULT_SCAN_INTERVAL as DEFAULT_SCAN_INTERVAL, DEFAULT_TRACKED_ASSET_PAIR as DEFAULT_TRACKED_ASSET_PAIR, DOMAIN as DOMAIN, KrakenResponse as KrakenResponse
from .utils import get_tradable_asset_pairs as get_tradable_asset_pairs
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_SCAN_INTERVAL as CONF_SCAN_INTERVAL
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

CALL_RATE_LIMIT_SLEEP: int
_LOGGER: Incomplete
type KrakenConfigEntry = ConfigEntry[KrakenData]

class KrakenData:
    _hass: Incomplete
    _config_entry: Incomplete
    _api: Incomplete
    tradable_asset_pairs: dict[str, str]
    coordinator: DataUpdateCoordinator[KrakenResponse | None] | None
    def __init__(self, hass: HomeAssistant, config_entry: KrakenConfigEntry) -> None: ...
    async def async_update(self) -> KrakenResponse | None: ...
    def _get_kraken_data(self) -> KrakenResponse: ...
    async def _async_refresh_tradable_asset_pairs(self) -> None: ...
    async def async_setup(self) -> None: ...
    def _get_websocket_name_asset_pairs(self) -> str: ...
    def set_update_interval(self, update_interval: int) -> None: ...
