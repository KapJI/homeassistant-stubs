from .config import async_get_and_load_store as async_get_and_load_store, async_load_config as async_load_config
from .const import CONF_BASE_URL as CONF_BASE_URL, CONF_CORS_ORIGINS as CONF_CORS_ORIGINS, CONF_IP_BAN_ENABLED as CONF_IP_BAN_ENABLED, CONF_LOGIN_ATTEMPTS_THRESHOLD as CONF_LOGIN_ATTEMPTS_THRESHOLD, CONF_SERVER_HOST as CONF_SERVER_HOST, CONF_SERVER_PORT as CONF_SERVER_PORT, CONF_SSL_CERTIFICATE as CONF_SSL_CERTIFICATE, CONF_SSL_KEY as CONF_SSL_KEY, CONF_SSL_PEER_CERTIFICATE as CONF_SSL_PEER_CERTIFICATE, CONF_SSL_PROFILE as CONF_SSL_PROFILE, CONF_TRUSTED_PROXIES as CONF_TRUSTED_PROXIES, CONF_USE_X_FORWARDED_FOR as CONF_USE_X_FORWARDED_FOR, CONF_USE_X_FRAME_OPTIONS as CONF_USE_X_FRAME_OPTIONS, DEFAULT_CORS as DEFAULT_CORS, DOMAIN as DOMAIN, KEY_HASS_REFRESH_TOKEN_ID as KEY_HASS_REFRESH_TOKEN_ID, KEY_HASS_USER as KEY_HASS_USER, NO_LOGIN_ATTEMPT_THRESHOLD as NO_LOGIN_ATTEMPT_THRESHOLD, SSL_INTERMEDIATE as SSL_INTERMEDIATE, SSL_MODERN as SSL_MODERN
from .decorators import require_admin as require_admin
from .server import DEFAULT_BIND as DEFAULT_BIND, HassioHTTPConfigView as HassioHTTPConfigView, HomeAssistantHTTP as HomeAssistantHTTP, HomeAssistantRequest as HomeAssistantRequest, StaticPathConfig as StaticPathConfig, make_server as make_server
from _typeshed import Incomplete
from homeassistant.components.network import async_get_source_ip as async_get_source_ip
from homeassistant.const import EVENT_HOMEASSISTANT_START as EVENT_HOMEASSISTANT_START, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, HASSIO_USER_NAME as HASSIO_USER_NAME
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.http import HomeAssistantView as HomeAssistantView, KEY_ALLOW_CONFIGURED_CORS as KEY_ALLOW_CONFIGURED_CORS, KEY_AUTHENTICATED as KEY_AUTHENTICATED, KEY_HASS as KEY_HASS, current_request as current_request
from homeassistant.helpers.importlib import async_import_module as async_import_module
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.setup import SetupPhases as SetupPhases, async_start_setup as async_start_setup, async_when_setup_or_start as async_when_setup_or_start
from homeassistant.util.async_ import create_eager_task as create_eager_task
from typing import Final

_LOGGER: Final[Incomplete]
DEFAULT_DEVELOPMENT: Final[str]
HTTP_SCHEMA: Final[Incomplete]
CONFIG_SCHEMA: Final[Incomplete]

class ApiConfig:
    local_ip: Incomplete
    host: Incomplete
    port: Incomplete
    use_ssl: Incomplete
    def __init__(self, local_ip: str, host: str, port: int, use_ssl: bool) -> None: ...

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
