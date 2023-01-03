import aiounifi
from .const import ATTR_MANUFACTURER as ATTR_MANUFACTURER
from .controller import UniFiController as UniFiController
from .entity import DataT as DataT, HandlerT as HandlerT, UnifiEntity as UnifiEntity, UnifiEntityDescription as UnifiEntityDescription
from _typeshed import Incomplete
from aiounifi.interfaces.api_handlers import ItemEvent
from collections.abc import Callable as Callable, Coroutine
from homeassistant.components.update import UpdateDeviceClass as UpdateDeviceClass, UpdateEntity as UpdateEntity, UpdateEntityDescription as UpdateEntityDescription, UpdateEntityFeature as UpdateEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

LOGGER: Incomplete

def async_device_available_fn(controller: UniFiController, obj_id: str) -> bool: ...
async def async_device_control_fn(api: aiounifi.Controller, obj_id: str) -> None: ...
def async_device_device_info_fn(api: aiounifi.Controller, obj_id: str) -> DeviceInfo: ...

class UnifiEntityLoader:
    control_fn: Callable[[aiounifi.Controller, str], Coroutine[Any, Any, None]]
    state_fn: Callable[[aiounifi.Controller, DataT], bool]
    def __init__(self, control_fn, state_fn) -> None: ...

class UnifiUpdateEntityDescription(UpdateEntityDescription, UnifiEntityDescription[HandlerT, DataT], UnifiEntityLoader[HandlerT, DataT]):
    def __init__(self, *, control_fn, state_fn, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, **) -> None: ...

ENTITY_DESCRIPTIONS: tuple[UnifiUpdateEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class UnifiDeviceUpdateEntity(UnifiEntity[HandlerT, DataT], UpdateEntity):
    entity_description: UnifiUpdateEntityDescription[HandlerT, DataT]
    _attr_supported_features: Incomplete
    def async_initiate_state(self) -> None: ...
    async def async_install(self, version: Union[str, None], backup: bool, **kwargs: Any) -> None: ...
    _attr_in_progress: Incomplete
    _attr_installed_version: Incomplete
    _attr_latest_version: Incomplete
    def async_update_state(self, event: ItemEvent, obj_id: str) -> None: ...
