from . import HABITICA_KEY as HABITICA_KEY
from .const import ASSETS_URL as ASSETS_URL
from .coordinator import HabiticaConfigEntry as HabiticaConfigEntry, HabiticaDataUpdateCoordinator as HabiticaDataUpdateCoordinator, HabiticaPartyCoordinator as HabiticaPartyCoordinator
from .entity import HabiticaBase as HabiticaBase, HabiticaPartyBase as HabiticaPartyBase, HabiticaPartyMemberBase as HabiticaPartyMemberBase
from _typeshed import Incomplete
from enum import StrEnum
from habiticalib import Avatar as Avatar, ContentData as ContentData
from homeassistant.components.image import Image as Image, ImageEntity as ImageEntity, ImageEntityDescription as ImageEntityDescription
from homeassistant.config_entries import ConfigSubentry as ConfigSubentry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

PARALLEL_UPDATES: int

class HabiticaImageEntity(StrEnum):
    AVATAR = 'avatar'
    QUEST_IMAGE = 'quest_image'

async def async_setup_entry(hass: HomeAssistant, config_entry: HabiticaConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class HabiticaImage(HabiticaBase, ImageEntity):
    entity_description: Incomplete
    _attr_content_type: str
    _avatar: Avatar | None
    _cache: bytes | None
    _attr_image_last_updated: Incomplete
    def __init__(self, hass: HomeAssistant, coordinator: HabiticaDataUpdateCoordinator, subentry: ConfigSubentry | None = None) -> None: ...
    def _handle_coordinator_update(self) -> None: ...
    async def async_image(self) -> bytes | None: ...

class HabiticaPartyMemberImage(HabiticaImage, HabiticaPartyMemberBase):
    def __init__(self, hass: HomeAssistant, coordinator: HabiticaDataUpdateCoordinator, party_coordinator: HabiticaPartyCoordinator, subentry: ConfigSubentry | None = None) -> None: ...

class HabiticaPartyImage(HabiticaPartyBase, ImageEntity):
    entity_description: Incomplete
    _attr_content_type: str
    _attr_image_url: Incomplete
    _attr_image_last_updated: Incomplete
    def __init__(self, hass: HomeAssistant, coordinator: HabiticaPartyCoordinator, config_entry: HabiticaConfigEntry, content: ContentData) -> None: ...
    _cached_image: Incomplete
    def _handle_coordinator_update(self) -> None: ...
    @property
    def image_url(self) -> str | None: ...
    async def _async_load_image_from_url(self, url: str) -> Image | None: ...
