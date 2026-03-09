from .const import ATTR_ACCOUNT_NAME as ATTR_ACCOUNT_NAME, ATTR_CONTENT_WARNING as ATTR_CONTENT_WARNING, ATTR_DURATION as ATTR_DURATION, ATTR_HIDE_NOTIFICATIONS as ATTR_HIDE_NOTIFICATIONS, ATTR_IDEMPOTENCY_KEY as ATTR_IDEMPOTENCY_KEY, ATTR_LANGUAGE as ATTR_LANGUAGE, ATTR_MEDIA as ATTR_MEDIA, ATTR_MEDIA_DESCRIPTION as ATTR_MEDIA_DESCRIPTION, ATTR_MEDIA_WARNING as ATTR_MEDIA_WARNING, ATTR_STATUS as ATTR_STATUS, ATTR_VISIBILITY as ATTR_VISIBILITY, DOMAIN as DOMAIN
from .coordinator import MastodonConfigEntry as MastodonConfigEntry
from .utils import get_media_type as get_media_type
from _typeshed import Incomplete
from enum import StrEnum
from homeassistant.const import ATTR_CONFIG_ENTRY_ID as ATTR_CONFIG_ENTRY_ID
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, ServiceResponse as ServiceResponse, SupportsResponse as SupportsResponse, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, ServiceValidationError as ServiceValidationError
from homeassistant.helpers import service as service
from mastodon import Mastodon as Mastodon
from mastodon.Mastodon import Account as Account, MediaAttachment as MediaAttachment
from typing import Any

MAX_DURATION_SECONDS: int

class StatusVisibility(StrEnum):
    PUBLIC = 'public'
    UNLISTED = 'unlisted'
    PRIVATE = 'private'
    DIRECT = 'direct'

SERVICE_GET_ACCOUNT: str
SERVICE_GET_ACCOUNT_SCHEMA: Incomplete
SERVICE_MUTE_ACCOUNT: str
SERVICE_MUTE_ACCOUNT_SCHEMA: Incomplete
SERVICE_UNMUTE_ACCOUNT: str
SERVICE_UNMUTE_ACCOUNT_SCHEMA: Incomplete
SERVICE_POST: str
SERVICE_POST_SCHEMA: Incomplete

@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
async def _async_account_lookup(hass: HomeAssistant, client: Mastodon, account_name: str) -> Account: ...
async def _async_get_account(call: ServiceCall) -> ServiceResponse: ...
async def _async_mute_account(call: ServiceCall) -> ServiceResponse: ...
async def _async_unmute_account(call: ServiceCall) -> ServiceResponse: ...
async def _async_post(call: ServiceCall) -> ServiceResponse: ...
def _post(hass: HomeAssistant, client: Mastodon, **kwargs: Any) -> None: ...
