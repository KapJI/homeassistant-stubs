from .const import CONF_MEDIA as CONF_MEDIA, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.media_player import BrowseError as BrowseError, MediaClass as MediaClass
from homeassistant.components.media_source import URI_SCHEME as URI_SCHEME, async_browse_media as async_browse_media
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.selector import MediaSelector as MediaSelector
from typing import Any, override

IMAGE_MEDIA_URI: Incomplete
STEP_USER_DATA_SCHEMA: Incomplete

async def _async_validate_media(hass: HomeAssistant, user_input: dict[str, Any]) -> tuple[str | None, dict[str, str], dict[str, str]]: ...

class CollectionImageConfigFlow(ConfigFlow, domain=DOMAIN):
    async def async_step_reconfigure(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    @override
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
