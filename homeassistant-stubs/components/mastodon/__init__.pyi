from .const import CONF_BASE_URL as CONF_BASE_URL, DOMAIN as DOMAIN, LOGGER as LOGGER
from .coordinator import MastodonConfigEntry as MastodonConfigEntry, MastodonCoordinator as MastodonCoordinator, MastodonData as MastodonData
from .services import setup_services as setup_services
from .utils import construct_mastodon_username as construct_mastodon_username, create_mastodon_client as create_mastodon_client
from _typeshed import Incomplete
from homeassistant.const import CONF_ACCESS_TOKEN as CONF_ACCESS_TOKEN, CONF_CLIENT_ID as CONF_CLIENT_ID, CONF_CLIENT_SECRET as CONF_CLIENT_SECRET, CONF_NAME as CONF_NAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import discovery as discovery
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.util import slugify as slugify
from mastodon.Mastodon import Account as Account, Instance as Instance, InstanceV2 as InstanceV2, Mastodon as Mastodon

PLATFORMS: list[Platform]
CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: MastodonConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: MastodonConfigEntry) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, entry: MastodonConfigEntry) -> bool: ...
def setup_mastodon(entry: MastodonConfigEntry) -> tuple[Mastodon, InstanceV2 | Instance, Account]: ...
