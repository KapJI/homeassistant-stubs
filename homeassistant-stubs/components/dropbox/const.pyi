from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.util.hass_dict import HassKey as HassKey

DOMAIN: str
OAUTH2_AUTHORIZE: str
OAUTH2_TOKEN: str
OAUTH2_SCOPES: Incomplete
DATA_BACKUP_AGENT_LISTENERS: HassKey[list[Callable[[], None]]]
