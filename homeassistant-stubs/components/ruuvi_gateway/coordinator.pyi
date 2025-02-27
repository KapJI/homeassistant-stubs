import logging
from .const import SCAN_INTERVAL as SCAN_INTERVAL
from _typeshed import Incomplete
from aioruuvigateway.models import TagData
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_TOKEN as CONF_TOKEN
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.httpx_client import get_async_client as get_async_client
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator

class RuuviGatewayUpdateCoordinator(DataUpdateCoordinator[list[TagData]]):
    config_entry: ConfigEntry
    host: Incomplete
    token: Incomplete
    last_tag_datas: dict[str, TagData]
    def __init__(self, hass: HomeAssistant, config_entry: ConfigEntry, logger: logging.Logger) -> None: ...
    async def _async_update_data(self) -> list[TagData]: ...
