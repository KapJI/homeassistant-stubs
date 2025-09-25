from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.util.hass_dict import HassKey as HassKey
from typing import Final

DOMAIN: Final[str]
LOGGER: Incomplete
CONF_HOST: Final[str]
CONF_PORT: Final[str]
CONF_USERNAME: Final[str]
CONF_PASSWORD: Final[str]
CONF_PRIVATE_KEY_FILE: Final[str]
CONF_BACKUP_LOCATION: Final[str]
BUF_SIZE: Incomplete
DATA_BACKUP_AGENT_LISTENERS: HassKey[list[Callable[[], None]]]
DEFAULT_PKEY_NAME: str
