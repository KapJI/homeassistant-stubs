import evohomeasync2 as ec2
from .const import CONF_LOCATION_IDX as CONF_LOCATION_IDX, DOMAIN as DOMAIN, EVOHOME_DATA as EVOHOME_DATA, SCAN_INTERVAL_DEFAULT as SCAN_INTERVAL_DEFAULT, SCAN_INTERVAL_MINIMUM as SCAN_INTERVAL_MINIMUM
from .coordinator import EvoDataUpdateCoordinator as EvoDataUpdateCoordinator
from .services import setup_service_functions as setup_service_functions
from .storage import TokenManager as TokenManager
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_SCAN_INTERVAL as CONF_SCAN_INTERVAL, CONF_USERNAME as CONF_USERNAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.discovery import async_load_platform as async_load_platform
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Final

_LOGGER: Incomplete
CONFIG_SCHEMA: Final[Incomplete]

@dataclass
class EvoData:
    coordinator: EvoDataUpdateCoordinator
    loc_idx: int
    tcs: ec2.ControlSystem

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
