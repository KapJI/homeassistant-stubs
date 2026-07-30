from aiohttp.web import Request as Request
from homeassistant.helpers.http import KEY_AUTHENTICATED as KEY_AUTHENTICATED, KEY_HASS as KEY_HASS
from typing import Final

DOMAIN: Final[str]
KEY_HASS_USER: Final[str]
KEY_HASS_REFRESH_TOKEN_ID: Final[str]
KEY_SUPERVISOR_UNIX_SOCKET: Final[str]
CONF_SERVER_HOST: Final[str]
CONF_SERVER_PORT: Final[str]
CONF_BASE_URL: Final[str]
CONF_SSL_CERTIFICATE: Final[str]
CONF_SSL_PEER_CERTIFICATE: Final[str]
CONF_SSL_KEY: Final[str]
CONF_CORS_ORIGINS: Final[str]
CONF_USE_X_FORWARDED_FOR: Final[str]
CONF_USE_X_FRAME_OPTIONS: Final[str]
CONF_TRUSTED_PROXIES: Final[str]
CONF_LOGIN_ATTEMPTS_THRESHOLD: Final[str]
CONF_IP_BAN_ENABLED: Final[str]
CONF_SSL_PROFILE: Final[str]
SSL_MODERN: Final[str]
SSL_INTERMEDIATE: Final[str]
ENV_SETUP_PORT: Final[str]
ENV_SUPERVISOR: Final[str]
SUPERVISOR_DEFAULT_PORT: Final[int]
DEFAULT_CORS: Final[list[str]]
NO_LOGIN_ATTEMPT_THRESHOLD: Final[int]
ATTR_CONFIG: str

def is_supervisor_unix_socket_request(request: Request) -> bool: ...
