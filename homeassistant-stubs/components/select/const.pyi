from . import SelectEntity as SelectEntity
from enum import StrEnum
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.util.hass_dict import HassKey as HassKey
from typing import Final

DOMAIN: Final[str]
DATA_COMPONENT: HassKey[EntityComponent[SelectEntity]]

class SelectEntityCapabilityAttribute(StrEnum):
    OPTIONS = 'options'

ATTR_CYCLE: str
ATTR_OPTIONS: str
CONF_CYCLE: str
CONF_OPTION: str
SERVICE_SELECT_FIRST: str
SERVICE_SELECT_LAST: str
SERVICE_SELECT_NEXT: str
SERVICE_SELECT_PREVIOUS: str
