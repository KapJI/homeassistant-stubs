from .b2_client import B2Api as B2Api, InMemoryAccountInfo as InMemoryAccountInfo
from .const import BACKBLAZE_REALM as BACKBLAZE_REALM, CONF_APPLICATION_KEY as CONF_APPLICATION_KEY, CONF_BUCKET as CONF_BUCKET, CONF_KEY_ID as CONF_KEY_ID, DATA_BACKUP_AGENT_LISTENERS as DATA_BACKUP_AGENT_LISTENERS, DOMAIN as DOMAIN
from .repairs import async_check_for_repair_issues as async_check_for_repair_issues, create_bucket_access_restricted_issue as create_bucket_access_restricted_issue, create_bucket_not_found_issue as create_bucket_not_found_issue
from _typeshed import Incomplete
from b2sdk.v2 import Bucket
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.event import async_track_time_interval as async_track_time_interval

_LOGGER: Incomplete
type BackblazeConfigEntry = ConfigEntry[Bucket]

async def async_setup_entry(hass: HomeAssistant, entry: BackblazeConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: BackblazeConfigEntry) -> bool: ...
