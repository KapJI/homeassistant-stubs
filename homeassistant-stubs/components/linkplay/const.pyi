from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.const import Platform as Platform
from homeassistant.util.hass_dict import HassKey as HassKey
from linkplay.controller import LinkPlayController as LinkPlayController

@dataclass
class LinkPlaySharedData:
    controller: LinkPlayController
    entity_to_bridge: dict[str, str]

DOMAIN: str
SHARED_DATA: str
SHARED_DATA_KEY: HassKey[LinkPlaySharedData]
PLATFORMS: Incomplete
DATA_SESSION: str
