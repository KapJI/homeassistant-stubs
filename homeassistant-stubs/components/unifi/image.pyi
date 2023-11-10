from .controller import UniFiController as UniFiController
from .entity import HandlerT as HandlerT, UnifiEntity as UnifiEntity, UnifiEntityDescription as UnifiEntityDescription, async_wlan_available_fn as async_wlan_available_fn, async_wlan_device_info_fn as async_wlan_device_info_fn
from _typeshed import Incomplete
from aiounifi.interfaces.api_handlers import ItemEvent as ItemEvent
from aiounifi.models.api import ApiItemT
from aiounifi.models.wlan import Wlan
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.image import ImageEntity as ImageEntity, ImageEntityDescription as ImageEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Generic

def async_wlan_qr_code_image_fn(controller: UniFiController, wlan: Wlan) -> bytes: ...

@dataclass
class UnifiImageEntityDescriptionMixin(Generic[HandlerT, ApiItemT]):
    image_fn: Callable[[UniFiController, ApiItemT], bytes]
    value_fn: Callable[[ApiItemT], str | None]
    def __init__(self, image_fn, value_fn) -> None: ...

@dataclass
class UnifiImageEntityDescription(ImageEntityDescription, UnifiEntityDescription[HandlerT, ApiItemT], UnifiImageEntityDescriptionMixin[HandlerT, ApiItemT]):
    def __init__(self, image_fn, value_fn, allowed_fn, api_handler_fn, available_fn, device_info_fn, event_is_on, event_to_subscribe, name_fn, object_fn, should_poll, supported_fn, unique_id_fn, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement) -> None: ...

ENTITY_DESCRIPTIONS: tuple[UnifiImageEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class UnifiImageEntity(UnifiEntity[HandlerT, ApiItemT], ImageEntity):
    entity_description: UnifiImageEntityDescription[HandlerT, ApiItemT]
    _attr_content_type: str
    current_image: bytes | None
    previous_value: str | None
    def __init__(self, obj_id: str, controller: UniFiController, description: UnifiEntityDescription[HandlerT, ApiItemT]) -> None: ...
    def image(self) -> bytes | None: ...
    _attr_image_last_updated: Incomplete
    def async_update_state(self, event: ItemEvent, obj_id: str) -> None: ...
