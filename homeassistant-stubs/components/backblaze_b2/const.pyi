from collections.abc import Callable as Callable
from homeassistant.util.hass_dict import HassKey as HassKey
from typing import Final

DOMAIN: Final[str]
CONF_KEY_ID: str
CONF_APPLICATION_KEY: str
CONF_BUCKET: str
CONF_PREFIX: str
DATA_BACKUP_AGENT_LISTENERS: HassKey[list[Callable[[], None]]]
METADATA_FILE_SUFFIX: str
METADATA_VERSION: str
BACKBLAZE_REALM: str
