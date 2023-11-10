import aiounifi
from .controller import UniFiController as UniFiController
from .entity import HandlerT as HandlerT, UnifiEntity as UnifiEntity, UnifiEntityDescription as UnifiEntityDescription, async_device_available_fn as async_device_available_fn, async_device_device_info_fn as async_device_device_info_fn
from aiounifi.interfaces.api_handlers import ItemEvent as ItemEvent
from aiounifi.models.api import ApiItemT
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any, Generic

async def async_restart_device_control_fn(api: aiounifi.Controller, obj_id: str) -> None: ...

@dataclass
class UnifiButtonEntityDescriptionMixin(Generic[HandlerT, ApiItemT]):
    control_fn: Callable[[aiounifi.Controller, str], Coroutine[Any, Any, None]]
    def __init__(self, control_fn) -> None: ...

@dataclass
class UnifiButtonEntityDescription(ButtonEntityDescription, UnifiEntityDescription[HandlerT, ApiItemT], UnifiButtonEntityDescriptionMixin[HandlerT, ApiItemT]):
    def __init__(self, control_fn, allowed_fn, api_handler_fn, available_fn, device_info_fn, event_is_on, event_to_subscribe, name_fn, object_fn, should_poll, supported_fn, unique_id_fn, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement) -> None: ...

ENTITY_DESCRIPTIONS: tuple[UnifiButtonEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class UnifiButtonEntity(UnifiEntity[HandlerT, ApiItemT], ButtonEntity):
    entity_description: UnifiButtonEntityDescription[HandlerT, ApiItemT]
    async def async_press(self) -> None: ...
    def async_update_state(self, event: ItemEvent, obj_id: str) -> None: ...
