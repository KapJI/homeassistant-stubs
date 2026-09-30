from . import NotifyEntity as NotifyEntity
from _typeshed import Incomplete
from enum import IntFlag
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.util.hass_dict import HassKey as HassKey
from typing import Final

DOMAIN: Final[str]
DATA_COMPONENT: HassKey[EntityComponent[NotifyEntity]]
ATTR_DATA: str
ATTR_MESSAGE: str
ATTR_TARGET: str
ATTR_RECIPIENTS: str
ATTR_TITLE: str
LOGGER: Incomplete
SERVICE_NOTIFY: str
SERVICE_SEND_MESSAGE: str
SERVICE_PERSISTENT_NOTIFICATION: str
NOTIFY_SERVICE_SCHEMA: Incomplete

class NotifyEntityFeature(IntFlag):
    TITLE = 1
