from .const import CONF_REPOSITORIES as CONF_REPOSITORIES, DOMAIN as DOMAIN, LOGGER as LOGGER
from .coordinator import GitHubDataUpdateCoordinator as GitHubDataUpdateCoordinator, GithubConfigEntry as GithubConfigEntry
from homeassistant.const import CONF_ACCESS_TOKEN as CONF_ACCESS_TOKEN, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.aiohttp_client import SERVER_SOFTWARE as SERVER_SOFTWARE, async_get_clientsession as async_get_clientsession

PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, entry: GithubConfigEntry) -> bool: ...
@callback
def async_cleanup_device_registry(hass: HomeAssistant, entry: GithubConfigEntry) -> None: ...
async def async_unload_entry(hass: HomeAssistant, entry: GithubConfigEntry) -> bool: ...
