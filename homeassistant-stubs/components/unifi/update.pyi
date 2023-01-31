import aiounifi
from .controller import UniFiController as UniFiController
from .entity import UnifiEntity as UnifiEntity, UnifiEntityDescription as UnifiEntityDescription, async_device_available_fn as async_device_available_fn, async_device_device_info_fn as async_device_device_info_fn
from _typeshed import Incomplete
from aiounifi.interfaces.api_handlers import ItemEvent
from aiounifi.interfaces.devices import Devices
from aiounifi.models.device import Device
from collections.abc import Callable as Callable, Coroutine
from homeassistant.components.update import UpdateDeviceClass as UpdateDeviceClass, UpdateEntity as UpdateEntity, UpdateEntityDescription as UpdateEntityDescription, UpdateEntityFeature as UpdateEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any, TypeVar

LOGGER: Incomplete
_DataT = TypeVar('_DataT', bound=Device)
_HandlerT = TypeVar('_HandlerT', bound=Devices)

async def async_device_control_fn(api: aiounifi.Controller, obj_id: str) -> None: ...

class UnifiUpdateEntityDescriptionMixin:
    control_fn: Callable[[aiounifi.Controller, str], Coroutine[Any, Any, None]]
    state_fn: Callable[[aiounifi.Controller, _DataT], bool]
    def __init__(self, control_fn, state_fn) -> None: ...

class UnifiUpdateEntityDescription(UpdateEntityDescription, UnifiEntityDescription[_HandlerT, _DataT], UnifiUpdateEntityDescriptionMixin[_HandlerT, _DataT]):
    def __init__(self, *, control_fn, state_fn, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, **kwargs) -> None: ...

ENTITY_DESCRIPTIONS: tuple[UnifiUpdateEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class UnifiDeviceUpdateEntity(UnifiEntity[_HandlerT, _DataT], UpdateEntity):
    entity_description: UnifiUpdateEntityDescription[_HandlerT, _DataT]
    _attr_supported_features: Incomplete
    def async_initiate_state(self) -> None: ...
    async def async_install(self, version: Union[str, None], backup: bool, **kwargs: Any) -> None: ...
    _attr_in_progress: Incomplete
    _attr_installed_version: Incomplete
    _attr_latest_version: Incomplete
    def async_update_state(self, event: ItemEvent, obj_id: str) -> None: ...
