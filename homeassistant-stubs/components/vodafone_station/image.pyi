from .const import _LOGGER as _LOGGER
from .coordinator import VodafoneConfigEntry as VodafoneConfigEntry, VodafoneStationRouter as VodafoneStationRouter
from _typeshed import Incomplete
from homeassistant.components.image import ImageEntity as ImageEntity, ImageEntityDescription as ImageEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Final

PARALLEL_UPDATES: int
IMAGE_TYPES: Final[Incomplete]

async def async_setup_entry(hass: HomeAssistant, entry: VodafoneConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class VodafoneGuestWifiQRImage(CoordinatorEntity[VodafoneStationRouter], ImageEntity):
    _attr_content_type: str
    _attr_entity_category: Incomplete
    _attr_has_entity_name: bool
    entity_description: Incomplete
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    _cached_qr_code: bytes | None
    def __init__(self, hass: HomeAssistant, coordinator: VodafoneStationRouter, description: ImageEntityDescription) -> None: ...
    @property
    def _qr_code(self) -> bytes: ...
    _attr_image_last_updated: Incomplete
    async def async_added_to_hass(self) -> None: ...
    def _handle_coordinator_update(self) -> None: ...
    async def async_image(self) -> bytes | None: ...
