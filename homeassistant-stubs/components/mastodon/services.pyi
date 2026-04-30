from .const import ATTR_ACCOUNT_NAME as ATTR_ACCOUNT_NAME, ATTR_ATTRIBUTION_DOMAINS as ATTR_ATTRIBUTION_DOMAINS, ATTR_AVATAR as ATTR_AVATAR, ATTR_AVATAR_MIME_TYPE as ATTR_AVATAR_MIME_TYPE, ATTR_BOT as ATTR_BOT, ATTR_CONTENT_WARNING as ATTR_CONTENT_WARNING, ATTR_DISCOVERABLE as ATTR_DISCOVERABLE, ATTR_DISPLAY_NAME as ATTR_DISPLAY_NAME, ATTR_DURATION as ATTR_DURATION, ATTR_FIELDS as ATTR_FIELDS, ATTR_HEADER as ATTR_HEADER, ATTR_HEADER_MIME_TYPE as ATTR_HEADER_MIME_TYPE, ATTR_HIDE_NOTIFICATIONS as ATTR_HIDE_NOTIFICATIONS, ATTR_IDEMPOTENCY_KEY as ATTR_IDEMPOTENCY_KEY, ATTR_LANGUAGE as ATTR_LANGUAGE, ATTR_LOCKED as ATTR_LOCKED, ATTR_MEDIA as ATTR_MEDIA, ATTR_MEDIA_DESCRIPTION as ATTR_MEDIA_DESCRIPTION, ATTR_MEDIA_WARNING as ATTR_MEDIA_WARNING, ATTR_NOTE as ATTR_NOTE, ATTR_QUOTE_APPROVAL_POLICY as ATTR_QUOTE_APPROVAL_POLICY, ATTR_STATUS as ATTR_STATUS, ATTR_VALUE as ATTR_VALUE, ATTR_VISIBILITY as ATTR_VISIBILITY, DOMAIN as DOMAIN, LOGGER as LOGGER
from .coordinator import MastodonConfigEntry as MastodonConfigEntry
from .utils import get_media_type as get_media_type
from _typeshed import Incomplete
from enum import StrEnum
from homeassistant.components import camera as camera, image as image
from homeassistant.components.media_source import async_resolve_media as async_resolve_media
from homeassistant.const import ATTR_CONFIG_ENTRY_ID as ATTR_CONFIG_ENTRY_ID, ATTR_NAME as ATTR_NAME
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, ServiceResponse as ServiceResponse, SupportsResponse as SupportsResponse, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, ServiceValidationError as ServiceValidationError
from homeassistant.helpers import service as service
from homeassistant.helpers.selector import MediaSelector as MediaSelector
from mastodon import Mastodon as Mastodon
from mastodon.Mastodon import Account as Account, MediaAttachment as MediaAttachment
from pathlib import Path
from typing import Any

MAX_DURATION_SECONDS: int

class StatusVisibility(StrEnum):
    PUBLIC = 'public'
    UNLISTED = 'unlisted'
    PRIVATE = 'private'
    DIRECT = 'direct'

class QuoteApprovalPolicy(StrEnum):
    PUBLIC = 'public'
    FOLLOWERS = 'followers'
    NOBODY = 'nobody'

SERVICE_GET_ACCOUNT: str
SERVICE_GET_ACCOUNT_SCHEMA: Incomplete
SERVICE_MUTE_ACCOUNT: str
SERVICE_MUTE_ACCOUNT_SCHEMA: Incomplete
SERVICE_UNMUTE_ACCOUNT: str
SERVICE_UNMUTE_ACCOUNT_SCHEMA: Incomplete
SERVICE_POST: str
SERVICE_POST_SCHEMA: Incomplete
SERVICE_UPDATE_PROFILE: str
SERVICE_UPDATE_PROFILE_SCHEMA: Incomplete

@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
async def _async_account_lookup(hass: HomeAssistant, client: Mastodon, account_name: str) -> Account: ...
async def _async_get_account(call: ServiceCall) -> ServiceResponse: ...
async def _async_mute_account(call: ServiceCall) -> ServiceResponse: ...
async def _async_unmute_account(call: ServiceCall) -> ServiceResponse: ...
async def _async_post(call: ServiceCall) -> ServiceResponse: ...
def _post(hass: HomeAssistant, client: Mastodon, **kwargs: Any) -> None: ...
async def _async_update_profile(call: ServiceCall) -> ServiceResponse: ...
async def _resolve_media(hass: HomeAssistant, media_source: dict[str, str]) -> tuple[bytes | Path, str | None]: ...
