from .const import DOMAIN as DOMAIN, PLATFORMS as PLATFORMS
from .coordinator import HWEnergyDeviceUpdateCoordinator as HWEnergyDeviceUpdateCoordinator, HomeWizardConfigEntry as HomeWizardConfigEntry
from homeassistant.config_entries import SOURCE_REAUTH as SOURCE_REAUTH
from homeassistant.const import CONF_IP_ADDRESS as CONF_IP_ADDRESS, CONF_TOKEN as CONF_TOKEN
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue
from homewizard_energy import HomeWizardEnergy as HomeWizardEnergy

async def async_setup_entry(hass: HomeAssistant, entry: HomeWizardConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: HomeWizardConfigEntry) -> bool: ...
async def async_check_v2_support_and_create_issue(hass: HomeAssistant, entry: HomeWizardConfigEntry) -> None: ...
