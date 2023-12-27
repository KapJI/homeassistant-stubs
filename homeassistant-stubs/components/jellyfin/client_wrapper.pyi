from .const import CLIENT_VERSION as CLIENT_VERSION, ITEM_KEY_IMAGE_TAGS as ITEM_KEY_IMAGE_TAGS, USER_AGENT as USER_AGENT, USER_APP_NAME as USER_APP_NAME
from homeassistant import exceptions as exceptions
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_URL as CONF_URL, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from jellyfin_apiclient_python import JellyfinClient as JellyfinClient
from jellyfin_apiclient_python.api import API as API
from jellyfin_apiclient_python.connection_manager import ConnectionManager as ConnectionManager
from typing import Any

async def validate_input(hass: HomeAssistant, user_input: dict[str, Any], client: JellyfinClient) -> tuple[str, dict[str, Any]]: ...
def create_client(device_id: str, device_name: str | None = None) -> JellyfinClient: ...
def _connect(client: JellyfinClient, url: str, username: str, password: str) -> tuple[str, dict[str, Any]]: ...
def _connect_to_address(connection_manager: ConnectionManager, url: str) -> dict[str, Any]: ...
def _login(connection_manager: ConnectionManager, url: str, username: str, password: str) -> None: ...
def _get_user_id(api: API) -> str: ...
def get_artwork_url(client: JellyfinClient, item: dict[str, Any], max_width: int = 600) -> str | None: ...

class CannotConnect(exceptions.HomeAssistantError): ...
class InvalidAuth(exceptions.HomeAssistantError): ...
