from . import BSBLanConfigEntry as BSBLanConfigEntry
from .const import DOMAIN as DOMAIN
from .helpers import async_sync_device_time as async_sync_device_time
from _typeshed import Incomplete
from bsblan import DaySchedule
from datetime import time
from homeassistant.config_entries import ConfigEntryState as ConfigEntryState
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, ServiceValidationError as ServiceValidationError

LOGGER: Incomplete
ATTR_DEVICE_ID: str
ATTR_MONDAY_SLOTS: str
ATTR_TUESDAY_SLOTS: str
ATTR_WEDNESDAY_SLOTS: str
ATTR_THURSDAY_SLOTS: str
ATTR_FRIDAY_SLOTS: str
ATTR_SATURDAY_SLOTS: str
ATTR_SUNDAY_SLOTS: str
_SLOT_SCHEMA: Incomplete
SERVICE_SET_HOT_WATER_SCHEDULE_SCHEMA: Incomplete

def _convert_time_slots_to_day_schedule(slots: list[dict[str, time]] | None) -> DaySchedule | None: ...
async def set_hot_water_schedule(service_call: ServiceCall) -> None: ...
async def async_sync_time(service_call: ServiceCall) -> None: ...

SYNC_TIME_SCHEMA: Incomplete

@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
