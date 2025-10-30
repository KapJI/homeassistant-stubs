from _typeshed import Incomplete
from bs4 import BeautifulSoup
from datetime import timedelta
from homeassistant.components.rest import CONF_PAYLOAD_TEMPLATE as CONF_PAYLOAD_TEMPLATE, RestData as RestData
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_RESOURCE_TEMPLATE as CONF_RESOURCE_TEMPLATE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import Any

_LOGGER: Incomplete

class ScrapeCoordinator(DataUpdateCoordinator[BeautifulSoup]):
    _rest: Incomplete
    _rest_config: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: ConfigEntry | None, rest: RestData, rest_config: dict[str, Any], update_interval: timedelta) -> None: ...
    async def _async_update_data(self) -> BeautifulSoup: ...
