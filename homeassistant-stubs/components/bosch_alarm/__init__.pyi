from .const import CONF_INSTALLER_CODE as CONF_INSTALLER_CODE, CONF_USER_CODE as CONF_USER_CODE, DOMAIN as DOMAIN
from bosch_alarm_mode2 import Panel
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady

PLATFORMS: list[Platform]
type BoschAlarmConfigEntry = ConfigEntry[Panel]

async def async_setup_entry(hass: HomeAssistant, entry: BoschAlarmConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: BoschAlarmConfigEntry) -> bool: ...
