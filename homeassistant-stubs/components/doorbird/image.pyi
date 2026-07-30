from .const import DOMAIN as DOMAIN
from .entity import DoorBirdEntity as DoorBirdEntity
from .models import DoorBirdConfigEntry as DoorBirdConfigEntry, DoorBirdData as DoorBirdData
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.image import Image as Image, ImageEntity as ImageEntity, ImageEntityDescription as ImageEntityDescription, infer_image_type as infer_image_type
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import override

@dataclass(frozen=True, kw_only=True)
class DoorBirdImageEntityDescription(ImageEntityDescription):
    doorbird_event_type: str

IMAGE_DESCRIPTIONS: tuple[DoorBirdImageEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: DoorBirdConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class DoorBirdLastEventImage(ImageEntity, DoorBirdEntity):
    entity_description: DoorBirdImageEntityDescription
    _attr_unique_id: Incomplete
    _image_url: Incomplete
    _matching_event_names: Incomplete
    def __init__(self, hass: HomeAssistant, door_bird_data: DoorBirdData, description: DoorBirdImageEntityDescription) -> None: ...
    _cached_image: Incomplete
    _attr_content_type: Incomplete
    @override
    async def async_image(self) -> bytes | None: ...
    @override
    async def async_added_to_hass(self) -> None: ...
    _attr_image_last_updated: Incomplete
    @callback
    def _async_handle_event(self) -> None: ...
