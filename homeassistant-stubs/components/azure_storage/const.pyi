from collections.abc import Callable as Callable
from homeassistant.util.hass_dict import HassKey as HassKey
from typing import Final

DOMAIN: Final[str]
CONF_STORAGE_ACCOUNT_KEY: Final[str]
CONF_ACCOUNT_NAME: Final[str]
CONF_CONTAINER_NAME: Final[str]
DATA_BACKUP_AGENT_LISTENERS: HassKey[list[Callable[[], None]]]
