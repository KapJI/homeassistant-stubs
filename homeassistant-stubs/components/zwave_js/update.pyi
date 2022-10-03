import asyncio
from .const import API_KEY_FIRMWARE_UPDATE_SERVICE as API_KEY_FIRMWARE_UPDATE_SERVICE, DATA_CLIENT as DATA_CLIENT, DOMAIN as DOMAIN, LOGGER as LOGGER
from .helpers import get_device_info as get_device_info, get_valueless_base_unique_id as get_valueless_base_unique_id
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from datetime import datetime
from homeassistant.components.update import UpdateDeviceClass as UpdateDeviceClass, UpdateEntity as UpdateEntity, UpdateEntityFeature as UpdateEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.event import async_call_later as async_call_later
from homeassistant.helpers.start import async_at_start as async_at_start
from typing import Any
from zwave_js_server.model.driver import Driver as Driver
from zwave_js_server.model.firmware import FirmwareUpdateFinished as FirmwareUpdateFinished, FirmwareUpdateInfo as FirmwareUpdateInfo, FirmwareUpdateProgress as FirmwareUpdateProgress
from zwave_js_server.model.node import Node as ZwaveNode

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ZWaveNodeFirmwareUpdate(UpdateEntity):
    _attr_entity_category: Incomplete
    _attr_device_class: Incomplete
    _attr_supported_features: Incomplete
    _attr_has_entity_name: bool
    _attr_should_poll: bool
    driver: Incomplete
    node: Incomplete
    semaphore: Incomplete
    _latest_version_firmware: Incomplete
    _status_unsub: Incomplete
    _poll_unsub: Incomplete
    _progress_unsub: Incomplete
    _finished_unsub: Incomplete
    _num_files_installed: int
    _finished_event: Incomplete
    _finished_status: Incomplete
    _attr_name: str
    _base_unique_id: Incomplete
    _attr_unique_id: Incomplete
    _attr_installed_version: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, driver: Driver, node: ZwaveNode, semaphore: asyncio.Semaphore) -> None: ...
    def _update_on_status_change(self, _: dict[str, Any]) -> None: ...
    _attr_in_progress: Incomplete
    def _update_progress(self, event: dict[str, Any]) -> None: ...
    def _update_finished(self, event: dict[str, Any]) -> None: ...
    def _unsub_firmware_events_and_reset_progress(self, write_state: bool = ...) -> None: ...
    _attr_latest_version: Incomplete
    async def _async_update(self, _: Union[HomeAssistant, datetime, None] = ...) -> None: ...
    async def async_release_notes(self) -> Union[str, None]: ...
    async def async_install(self, version: Union[str, None], backup: bool, **kwargs: Any) -> None: ...
    async def async_poll_value(self, _: bool) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
