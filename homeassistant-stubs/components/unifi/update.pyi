from .const import ATTR_MANUFACTURER as ATTR_MANUFACTURER
from .controller import UniFiController as UniFiController
from _typeshed import Incomplete
from aiounifi.interfaces.api_handlers import ItemEvent
from homeassistant.components.update import DOMAIN as DOMAIN, UpdateDeviceClass as UpdateDeviceClass, UpdateEntity as UpdateEntity, UpdateEntityFeature as UpdateEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

LOGGER: Incomplete
DEVICE_UPDATE: str

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class UnifiDeviceUpdateEntity(UpdateEntity):
    DOMAIN: Incomplete
    TYPE: Incomplete
    _attr_device_class: Incomplete
    _attr_has_entity_name: bool
    controller: Incomplete
    _obj_id: Incomplete
    _attr_unique_id: Incomplete
    _attr_supported_features: Incomplete
    _attr_available: Incomplete
    _attr_in_progress: Incomplete
    _attr_installed_version: Incomplete
    _attr_latest_version: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, obj_id: str, controller: UniFiController) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    def async_signalling_callback(self, event: ItemEvent, obj_id: str) -> None: ...
    def async_signal_reachable_callback(self) -> None: ...
    async def async_install(self, version: Union[str, None], backup: bool, **kwargs: Any) -> None: ...
