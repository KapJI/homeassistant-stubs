from .const import API_KEY_FIRMWARE_UPDATE_SERVICE as API_KEY_FIRMWARE_UPDATE_SERVICE, DOMAIN as DOMAIN, LOGGER as LOGGER
from .helpers import get_device_info as get_device_info, get_valueless_base_unique_id as get_valueless_base_unique_id
from .models import ZwaveJSConfigEntry as ZwaveJSConfigEntry
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from datetime import datetime, timedelta
from homeassistant.components.update import ATTR_LATEST_VERSION as ATTR_LATEST_VERSION, UpdateDeviceClass as UpdateDeviceClass, UpdateEntity as UpdateEntity, UpdateEntityDescription as UpdateEntityDescription, UpdateEntityFeature as UpdateEntityFeature
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import CoreState as CoreState, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.event import async_call_later as async_call_later
from homeassistant.helpers.restore_state import ExtraStoredData as ExtraStoredData
from typing import Any, Final
from zwave_js_server.model.driver import Driver as Driver
from zwave_js_server.model.firmware import FirmwareUpdateInfo, FirmwareUpdateProgress as FirmwareUpdateProgress, FirmwareUpdateResult as FirmwareUpdateResult
from zwave_js_server.model.node import Node as ZwaveNode

PARALLEL_UPDATES: int
UPDATE_DELAY_STRING: str
UPDATE_DELAY_INTERVAL: int
ATTR_LATEST_VERSION_FIRMWARE: str

@dataclass(frozen=True, kw_only=True)
class ZWaveUpdateEntityDescription(UpdateEntityDescription):
    install_method: Callable[[ZWaveFirmwareUpdateEntity, FirmwareUpdateInfo], Awaitable[FirmwareUpdateResult]]
    progress_method: Callable[[ZWaveFirmwareUpdateEntity], Callable[[], None]]
    finished_method: Callable[[ZWaveFirmwareUpdateEntity], Callable[[], None]]

CONTROLLER_UPDATE_ENTITY_DESCRIPTION: Incomplete
NODE_UPDATE_ENTITY_DESCRIPTION: Incomplete

@dataclass
class ZWaveFirmwareUpdateExtraStoredData(ExtraStoredData):
    latest_version_firmware: FirmwareUpdateInfo | None
    def as_dict(self) -> dict[str, Any]: ...
    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> ZWaveFirmwareUpdateExtraStoredData: ...

async def async_setup_entry(hass: HomeAssistant, config_entry: ZwaveJSConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class ZWaveFirmwareUpdateEntity(UpdateEntity):
    driver: Driver
    entity_description: ZWaveUpdateEntityDescription
    node: ZwaveNode
    _attr_entity_category: Incomplete
    _attr_device_class: Incomplete
    _attr_supported_features: Incomplete
    _attr_has_entity_name: bool
    _attr_should_poll: bool
    _latest_version_firmware: FirmwareUpdateInfo | None
    _poll_unsub: Callable[[], None] | None
    _progress_unsub: Callable[[], None] | None
    _finished_unsub: Callable[[], None] | None
    _finished_event: Incomplete
    _result: FirmwareUpdateResult | None
    _delay: Final[timedelta]
    _attr_name: str
    _base_unique_id: Incomplete
    _attr_unique_id: Incomplete
    _attr_installed_version: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, driver: Driver, node: ZwaveNode, delay: timedelta, entity_description: ZWaveUpdateEntityDescription) -> None: ...
    @property
    def extra_restore_state_data(self) -> ZWaveFirmwareUpdateExtraStoredData: ...
    _attr_in_progress: bool
    _attr_update_percentage: Incomplete
    @callback
    def update_progress(self, event: dict[str, Any]) -> None: ...
    @callback
    def update_finished(self, event: dict[str, Any]) -> None: ...
    @callback
    def _unsub_firmware_events_and_reset_progress(self, write_state: bool = True) -> None: ...
    _attr_latest_version: Incomplete
    async def _async_update(self, _: HomeAssistant | datetime | None = None) -> None: ...
    async def async_release_notes(self) -> str | None: ...
    async def async_install(self, version: str | None, backup: bool, **kwargs: Any) -> None: ...
    async def async_poll_value(self, _: bool) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
