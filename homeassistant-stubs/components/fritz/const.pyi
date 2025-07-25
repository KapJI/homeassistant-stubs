from _typeshed import Incomplete
from enum import StrEnum
from homeassistant.const import Platform as Platform
from typing import Literal

class MeshRoles(StrEnum):
    NONE = 'none'
    MASTER = 'master'
    SLAVE = 'slave'

DOMAIN: str
PLATFORMS: Incomplete
CONF_OLD_DISCOVERY: str
DEFAULT_CONF_OLD_DISCOVERY: bool
CONF_FEATURE_DEVICE_TRACKING: str
DEFAULT_CONF_FEATURE_DEVICE_TRACKING: bool
DSL_CONNECTION: Literal['dsl']
DEFAULT_DEVICE_NAME: str
DEFAULT_HOST: str
DEFAULT_HTTP_PORT: int
DEFAULT_HTTPS_PORT: int
DEFAULT_USERNAME: str
DEFAULT_SSL: bool
ERROR_AUTH_INVALID: str
ERROR_CANNOT_CONNECT: str
ERROR_UPNP_NOT_CONFIGURED: str
ERROR_UNKNOWN: str
SWITCH_TYPE_DEFLECTION: str
SWITCH_TYPE_PORTFORWARD: str
SWITCH_TYPE_PROFILE: str
SWITCH_TYPE_WIFINETWORK: str
BUTTON_TYPE_WOL: str
UPTIME_DEVIATION: int
FRITZ_EXCEPTIONS: Incomplete
FRITZ_AUTH_EXCEPTIONS: Incomplete
WIFI_STANDARD: Incomplete
CONNECTION_TYPE_LAN: str
