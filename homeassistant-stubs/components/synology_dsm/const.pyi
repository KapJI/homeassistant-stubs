from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.const import Platform as Platform
from homeassistant.util.hass_dict import HassKey as HassKey
from synology_dsm.api.surveillance_station.const import SNAPSHOT_PROFILE_BALANCED

DOMAIN: str
DATA_BACKUP_AGENT_LISTENERS: HassKey[list[Callable[[], None]]]
ATTRIBUTION: str
PLATFORMS: Incomplete
EXCEPTION_DETAILS: str
EXCEPTION_UNKNOWN: str
ISSUE_MISSING_BACKUP_SETUP: str
CONF_SERIAL: str
CONF_VOLUMES: str
CONF_DEVICE_TOKEN: str
CONF_SNAPSHOT_QUALITY: str
CONF_BACKUP_SHARE: str
CONF_BACKUP_PATH: str
DEFAULT_USE_SSL: bool
DEFAULT_VERIFY_SSL: bool
DEFAULT_PORT: int
DEFAULT_PORT_SSL: int
DEFAULT_TIMEOUT: Incomplete
DEFAULT_SNAPSHOT_QUALITY = SNAPSHOT_PROFILE_BALANCED
DEFAULT_BACKUP_PATH: str
ENTITY_UNIT_LOAD: str
SHARED_SUFFIX: str
SIGNAL_CAMERA_SOURCE_CHANGED: str
SERVICE_REBOOT: str
SERVICE_SHUTDOWN: str
SERVICES: Incomplete
SYNOLOGY_AUTH_FAILED_EXCEPTIONS: Incomplete
SYNOLOGY_CONNECTION_EXCEPTIONS: Incomplete
