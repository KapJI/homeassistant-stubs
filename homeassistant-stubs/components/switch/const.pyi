from . import SwitchEntity as SwitchEntity
from _typeshed import Incomplete
from enum import StrEnum
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.util.hass_dict import HassKey as HassKey
from typing import Final

DOMAIN: Final[str]
DATA_COMPONENT: HassKey[EntityComponent[SwitchEntity]]

class SwitchDeviceClass(StrEnum):
    OUTLET = 'outlet'
    SWITCH = 'switch'

DEVICE_CLASSES_SCHEMA: Incomplete
