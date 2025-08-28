import datetime as dt
from .const import ATTR_DATETIME as ATTR_DATETIME, DOMAIN as DOMAIN, SERVICE_SET_DATE_TIME as SERVICE_SET_DATE_TIME
from .types import BoschAlarmConfigEntry as BoschAlarmConfigEntry
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntryState as ConfigEntryState
from homeassistant.const import ATTR_CONFIG_ENTRY_ID as ATTR_CONFIG_ENTRY_ID
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, ServiceValidationError as ServiceValidationError
from typing import Any

def validate_datetime(value: Any) -> dt.datetime: ...

SET_DATE_TIME_SCHEMA: Incomplete

async def async_set_panel_date(call: ServiceCall) -> None: ...
@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
