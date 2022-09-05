from .const import API_KEY_FIRMWARE_UPDATE_SERVICE as API_KEY_FIRMWARE_UPDATE_SERVICE, DATA_CLIENT as DATA_CLIENT, DOMAIN as DOMAIN, LOGGER as LOGGER
from .helpers import get_device_id as get_device_id, get_valueless_base_unique_id as get_valueless_base_unique_id
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components.update import UpdateDeviceClass as UpdateDeviceClass, UpdateEntity as UpdateEntity
from homeassistant.components.update.const import UpdateEntityFeature as UpdateEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any
from zwave_js_server.model.driver import Driver as Driver
from zwave_js_server.model.firmware import FirmwareUpdateInfo as FirmwareUpdateInfo
from zwave_js_server.model.node import Node as ZwaveNode

PARALLEL_UPDATES: int
SCAN_INTERVAL: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ZWaveNodeFirmwareUpdate(UpdateEntity):
    _attr_entity_category: Incomplete
    _attr_device_class: Incomplete
    _attr_supported_features: Incomplete
    _attr_has_entity_name: bool
    driver: Incomplete
    node: Incomplete
    _latest_version_firmware: Incomplete
    _status_unsub: Incomplete
    _attr_name: str
    _base_unique_id: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    _attr_installed_version: Incomplete
    def __init__(self, driver: Driver, node: ZwaveNode) -> None: ...
    def _update_on_status_change(self, _: dict[str, Any]) -> None: ...
    async def async_update(self, write_state: bool = ...) -> None: ...
    _attr_latest_version: Incomplete
    def _async_process_available_updates(self, write_state: bool = ...) -> None: ...
    async def async_release_notes(self) -> Union[str, None]: ...
    _attr_in_progress: bool
    async def async_install(self, version: Union[str, None], backup: bool, **kwargs: Any) -> None: ...
    async def async_poll_value(self, _: bool) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
