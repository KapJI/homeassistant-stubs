from .config_flow import CONF_SITE as CONF_SITE, create_omada_client as create_omada_client
from .const import DOMAIN as DOMAIN
from .controller import OmadaSiteController as OmadaSiteController
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from tplink_omada_client.devices import OmadaListDevice as OmadaListDevice

PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
def _remove_old_devices(hass: HomeAssistant, entry: ConfigEntry, omada_devices: dict[str, OmadaListDevice]) -> None: ...
