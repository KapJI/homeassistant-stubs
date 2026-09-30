from . import ELGATO_KEY as ELGATO_KEY
from .const import DOMAIN as DOMAIN
from .coordinator import ElgatoConfigEntry as ElgatoConfigEntry, ElgatoDataUpdateCoordinator as ElgatoDataUpdateCoordinator, ElgatoFirmwareCoordinator as ElgatoFirmwareCoordinator
from .entity import ElgatoEntity as ElgatoEntity
from .helpers import elgato_device_action as elgato_device_action
from _typeshed import Incomplete
from datetime import datetime
from elgato import FirmwareImage as FirmwareImage, FirmwareVersion as FirmwareVersion
from homeassistant.components.update import UpdateDeviceClass as UpdateDeviceClass, UpdateEntity as UpdateEntity, UpdateEntityFeature as UpdateEntityFeature
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.event import async_call_later as async_call_later
from typing import Any, override

PARALLEL_UPDATES: int
REBOOT_TIMEOUT: int

async def async_setup_entry(hass: HomeAssistant, entry: ElgatoConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class ElgatoUpdateEntity(ElgatoEntity, UpdateEntity):
    _attr_device_class: Incomplete
    _installing: bool
    _installing_build: int | None
    _installing_timeout: CALLBACK_TYPE | None
    _attr_entity_category: Incomplete
    _attr_supported_features: Incomplete
    firmware: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: ElgatoDataUpdateCoordinator, firmware: ElgatoFirmwareCoordinator) -> None: ...
    @override
    async def async_added_to_hass(self) -> None: ...
    @property
    @override
    def available(self) -> bool: ...
    @override
    async def async_update(self) -> None: ...
    @property
    @override
    def installed_version(self) -> str: ...
    @property
    @override
    def in_progress(self) -> bool: ...
    @property
    @override
    def latest_version(self) -> str | None: ...
    @property
    def _latest(self) -> FirmwareVersion | None: ...
    _attr_update_percentage: Incomplete
    @override
    async def async_install(self, version: str | None, backup: bool, **kwargs: Any) -> None: ...
    @elgato_device_action
    async def _upload(self, image: FirmwareImage) -> None: ...
    async def _download(self) -> FirmwareImage: ...
    @callback
    @override
    def _handle_coordinator_update(self) -> None: ...
    @callback
    def _sync_device_firmware(self) -> None: ...
    @callback
    def _installing_finished(self) -> None: ...
    @callback
    def _installing_timed_out(self, _now: datetime) -> None: ...
    @callback
    def _handle_progress(self, sent: int, total: int) -> None: ...
