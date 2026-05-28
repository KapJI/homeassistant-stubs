from .entity import InfraredEmitterEntity as InfraredEmitterEntity, InfraredReceiverEntity as InfraredReceiverEntity
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.util.hass_dict import HassKey as HassKey
from typing import Final

DOMAIN: Final[str]
DATA_COMPONENT: HassKey[EntityComponent[InfraredEmitterEntity | InfraredReceiverEntity]]
