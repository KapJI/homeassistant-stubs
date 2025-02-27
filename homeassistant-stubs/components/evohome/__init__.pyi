import evohomeasync2 as ec2
from .const import ATTR_DURATION as ATTR_DURATION, ATTR_DURATION_UNTIL as ATTR_DURATION_UNTIL, ATTR_PERIOD as ATTR_PERIOD, ATTR_SETPOINT as ATTR_SETPOINT, CONF_LOCATION_IDX as CONF_LOCATION_IDX, DOMAIN as DOMAIN, EvoService as EvoService, SCAN_INTERVAL_DEFAULT as SCAN_INTERVAL_DEFAULT, SCAN_INTERVAL_MINIMUM as SCAN_INTERVAL_MINIMUM
from .coordinator import EvoDataUpdateCoordinator as EvoDataUpdateCoordinator
from .storage import TokenManager as TokenManager
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, ATTR_MODE as ATTR_MODE, CONF_PASSWORD as CONF_PASSWORD, CONF_SCAN_INTERVAL as CONF_SCAN_INTERVAL, CONF_USERNAME as CONF_USERNAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.discovery import async_load_platform as async_load_platform
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.service import verify_domain_control as verify_domain_control
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.util.hass_dict import HassKey as HassKey
from typing import Final

_LOGGER: Incomplete
CONFIG_SCHEMA: Final[Incomplete]
RESET_ZONE_OVERRIDE_SCHEMA: Final[Incomplete]
SET_ZONE_OVERRIDE_SCHEMA: Final[Incomplete]
EVOHOME_KEY: HassKey[EvoData]

@dataclass
class EvoData:
    coordinator: EvoDataUpdateCoordinator
    loc_idx: int
    tcs: ec2.ControlSystem

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
@callback
def setup_service_functions(hass: HomeAssistant, coordinator: EvoDataUpdateCoordinator) -> None: ...
