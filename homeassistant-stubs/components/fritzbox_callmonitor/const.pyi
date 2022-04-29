from _typeshed import Incomplete
from homeassistant.backports.enum import StrEnum as StrEnum
from homeassistant.const import Platform as Platform
from typing import Final

class FritzState(StrEnum):
    RING: str
    CALL: str
    CONNECT: str
    DISCONNECT: str

ICON_PHONE: Final[str]
ATTR_PREFIXES: str
FRITZ_ACTION_GET_INFO: str
FRITZ_ATTR_NAME: str
FRITZ_ATTR_SERIAL_NUMBER: str
FRITZ_SERVICE_DEVICE_INFO: str
UNKNOWN_NAME: str
SERIAL_NUMBER: str
REGEX_NUMBER: str
CONF_PHONEBOOK: str
CONF_PHONEBOOK_NAME: str
CONF_PREFIXES: str
DEFAULT_HOST: str
DEFAULT_PORT: int
DEFAULT_USERNAME: str
DEFAULT_PHONEBOOK: int
DEFAULT_NAME: str
DOMAIN: Final[str]
MANUFACTURER: Final[str]
PLATFORMS: Incomplete
UNDO_UPDATE_LISTENER: Final[str]
FRITZBOX_PHONEBOOK: Final[str]
