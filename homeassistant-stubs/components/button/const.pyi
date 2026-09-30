from . import ButtonEntity as ButtonEntity
from _typeshed import Incomplete
from enum import StrEnum
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.util.hass_dict import HassKey as HassKey
from typing import Final

DOMAIN: Final[str]
DATA_COMPONENT: HassKey[EntityComponent[ButtonEntity]]
SERVICE_PRESS: str

class ButtonDeviceClass(StrEnum):
    IDENTIFY = 'identify'
    RESTART = 'restart'
    UPDATE = 'update'

DEVICE_CLASSES_SCHEMA: Incomplete
