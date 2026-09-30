from .const import DOMAIN as DOMAIN
from .coordinator import SofarConfigEntry as SofarConfigEntry
from _typeshed import Incomplete
from collections.abc import Awaitable
from homeassistant.const import ATTR_CONFIG_ENTRY_ID as ATTR_CONFIG_ENTRY_ID, ATTR_MODE as ATTR_MODE
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, ServiceValidationError as ServiceValidationError
from homeassistant.helpers.service import async_get_config_entry as async_get_config_entry, async_register_admin_service as async_register_admin_service

SERVICE_SET_ACTIVE_POWER_LIMIT: str
SERVICE_SET_FEED_IN_LIMIT: str
SERVICE_SET_PASSIVE_MODE_POWER: str
SERVICE_SET_PASSIVE_MODE_TIMEOUT: str
ATTR_ACTION: str
ATTR_BATTERY_POWER_MAX: str
ATTR_BATTERY_POWER_MIN: str
ATTR_ENABLED: str
ATTR_GRID_POWER: str
ATTR_LIMIT: str
ATTR_MAX_POWER: str
ATTR_TIMEOUT: str
_ENTRY_SCHEMA: Incomplete
_POWER_RANGE: Incomplete
SET_FEED_IN_LIMIT_SCHEMA: Incomplete
SET_ACTIVE_POWER_LIMIT_SCHEMA: Incomplete
SET_PASSIVE_MODE_TIMEOUT_SCHEMA: Incomplete
SET_PASSIVE_MODE_POWER_SCHEMA: Incomplete

def _get_entry(hass: HomeAssistant, call: ServiceCall, component: str) -> SofarConfigEntry: ...
async def _write(entry: SofarConfigEntry, write: Awaitable[None]) -> None: ...
@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
