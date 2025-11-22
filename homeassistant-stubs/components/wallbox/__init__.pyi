from .const import CHARGER_JWT_REFRESH_TOKEN as CHARGER_JWT_REFRESH_TOKEN, CHARGER_JWT_REFRESH_TTL as CHARGER_JWT_REFRESH_TTL, CHARGER_JWT_TOKEN as CHARGER_JWT_TOKEN, CHARGER_JWT_TTL as CHARGER_JWT_TTL, UPDATE_INTERVAL as UPDATE_INTERVAL
from .coordinator import WallboxConfigEntry as WallboxConfigEntry, WallboxCoordinator as WallboxCoordinator, check_token_validity as check_token_validity
from _typeshed import Incomplete
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant

PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: WallboxConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: WallboxConfigEntry) -> bool: ...
