from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.util.hass_dict import HassKey as HassKey
from typing import Final

DOMAIN: Final[str]
OAUTH2_AUTHORIZE: Final[str]
OAUTH2_TOKEN: Final[str]
OAUTH_SCOPES: Final[Incomplete]
DATA_BACKUP_AGENT_LISTENERS: HassKey[list[Callable[[], None]]]
