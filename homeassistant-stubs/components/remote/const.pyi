from . import RemoteEntity as RemoteEntity
from enum import IntFlag, StrEnum
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.util.hass_dict import HassKey as HassKey
from typing import Final

DOMAIN: Final[str]
DATA_COMPONENT: HassKey[EntityComponent[RemoteEntity]]
ATTR_ACTIVITY: str
ATTR_ACTIVITY_LIST: str
ATTR_CURRENT_ACTIVITY: str
ATTR_COMMAND_TYPE: str
ATTR_DEVICE: str
ATTR_NUM_REPEATS: str
ATTR_DELAY_SECS: str
ATTR_HOLD_SECS: str
ATTR_ALTERNATIVE: str
ATTR_TIMEOUT: str
SERVICE_SEND_COMMAND: str
SERVICE_LEARN_COMMAND: str
SERVICE_DELETE_COMMAND: str
SERVICE_SYNC: str
DEFAULT_NUM_REPEATS: int
DEFAULT_DELAY_SECS: float
DEFAULT_HOLD_SECS: int

class RemoteEntityStateAttribute(StrEnum):
    ACTIVITY_LIST = 'activity_list'
    CURRENT_ACTIVITY = 'current_activity'

class RemoteEntityFeature(IntFlag):
    LEARN_COMMAND = 1
    DELETE_COMMAND = 2
    ACTIVITY = 4
