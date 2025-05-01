from .const import ATTR_DESTINATION_POSITION as ATTR_DESTINATION_POSITION, ATTR_PASSWORD as ATTR_PASSWORD, ATTR_QUEUE_IDS as ATTR_QUEUE_IDS, ATTR_USERNAME as ATTR_USERNAME, DOMAIN as DOMAIN, SERVICE_GET_QUEUE as SERVICE_GET_QUEUE, SERVICE_GROUP_VOLUME_DOWN as SERVICE_GROUP_VOLUME_DOWN, SERVICE_GROUP_VOLUME_SET as SERVICE_GROUP_VOLUME_SET, SERVICE_GROUP_VOLUME_UP as SERVICE_GROUP_VOLUME_UP, SERVICE_MOVE_QUEUE_ITEM as SERVICE_MOVE_QUEUE_ITEM, SERVICE_REMOVE_FROM_QUEUE as SERVICE_REMOVE_FROM_QUEUE, SERVICE_SIGN_IN as SERVICE_SIGN_IN, SERVICE_SIGN_OUT as SERVICE_SIGN_OUT
from .coordinator import HeosConfigEntry as HeosConfigEntry
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.media_player import ATTR_MEDIA_VOLUME_LEVEL as ATTR_MEDIA_VOLUME_LEVEL
from homeassistant.config_entries import ConfigEntryState as ConfigEntryState
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, SupportsResponse as SupportsResponse
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, ServiceValidationError as ServiceValidationError
from homeassistant.helpers import entity_platform as entity_platform
from homeassistant.helpers.typing import VolDictType as VolDictType, VolSchemaType as VolSchemaType
from pyheos import Heos as Heos
from typing import Final

_LOGGER: Incomplete
HEOS_SIGN_IN_SCHEMA: Incomplete
HEOS_SIGN_OUT_SCHEMA: Incomplete

def register(hass: HomeAssistant) -> None: ...

@dataclass(frozen=True)
class EntityServiceDescription:
    name: str
    method_name: str
    schema: VolDictType | VolSchemaType | None = ...
    supports_response: SupportsResponse = ...
    def async_register(self, platform: entity_platform.EntityPlatform) -> None: ...

REMOVE_FROM_QUEUE_SCHEMA: Final[VolDictType]
GROUP_VOLUME_SET_SCHEMA: Final[VolDictType]
MOVE_QEUEUE_ITEM_SCHEMA: Final[VolDictType]
MEDIA_PLAYER_ENTITY_SERVICES: Final[Incomplete]

def register_media_player_services() -> None: ...
def _get_controller(hass: HomeAssistant) -> Heos: ...
async def _sign_in_handler(service: ServiceCall) -> None: ...
async def _sign_out_handler(service: ServiceCall) -> None: ...
