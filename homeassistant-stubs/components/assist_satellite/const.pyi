import asyncio
from .entity import AssistSatelliteEntity as AssistSatelliteEntity
from _typeshed import Incomplete
from enum import IntFlag
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.util.hass_dict import HassKey as HassKey

DOMAIN: str
DATA_COMPONENT: HassKey[EntityComponent[AssistSatelliteEntity]]
CONNECTION_TEST_DATA: HassKey[dict[str, asyncio.Event]]
PREANNOUNCE_FILENAME: str
PREANNOUNCE_URL: Incomplete

class AssistSatelliteEntityFeature(IntFlag):
    ANNOUNCE = 1
    START_CONVERSATION = 2
