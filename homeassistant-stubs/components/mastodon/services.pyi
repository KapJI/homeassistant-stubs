from .const import ATTR_CONFIG_ENTRY_ID as ATTR_CONFIG_ENTRY_ID, ATTR_CONTENT_WARNING as ATTR_CONTENT_WARNING, ATTR_MEDIA as ATTR_MEDIA, ATTR_MEDIA_DESCRIPTION as ATTR_MEDIA_DESCRIPTION, ATTR_MEDIA_WARNING as ATTR_MEDIA_WARNING, ATTR_STATUS as ATTR_STATUS, ATTR_VISIBILITY as ATTR_VISIBILITY, DOMAIN as DOMAIN
from .coordinator import MastodonConfigEntry as MastodonConfigEntry
from .utils import get_media_type as get_media_type
from _typeshed import Incomplete
from enum import StrEnum
from homeassistant.config_entries import ConfigEntryState as ConfigEntryState
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, ServiceResponse as ServiceResponse
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, ServiceValidationError as ServiceValidationError
from mastodon import Mastodon as Mastodon
from mastodon.Mastodon import MediaAttachment as MediaAttachment

class StatusVisibility(StrEnum):
    PUBLIC = 'public'
    UNLISTED = 'unlisted'
    PRIVATE = 'private'
    DIRECT = 'direct'

SERVICE_POST: str
SERVICE_POST_SCHEMA: Incomplete

def async_get_entry(hass: HomeAssistant, config_entry_id: str) -> MastodonConfigEntry: ...
def setup_services(hass: HomeAssistant) -> None: ...
