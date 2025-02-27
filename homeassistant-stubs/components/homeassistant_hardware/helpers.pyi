from . import DATA_COMPONENT as DATA_COMPONENT
from .util import FirmwareInfo as FirmwareInfo
from _typeshed import Incomplete
from collections import defaultdict
from collections.abc import AsyncIterator, Awaitable, Callable as Callable
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, callback as hass_callback
from typing import Protocol

_LOGGER: Incomplete

class SyncHardwareFirmwareInfoModule(Protocol):
    def get_firmware_info(self, hass: HomeAssistant, entry: ConfigEntry) -> FirmwareInfo | None: ...

class AsyncHardwareFirmwareInfoModule(Protocol):
    async def async_get_firmware_info(self, hass: HomeAssistant, entry: ConfigEntry) -> FirmwareInfo | None: ...
type HardwareFirmwareInfoModule = SyncHardwareFirmwareInfoModule | AsyncHardwareFirmwareInfoModule

class HardwareInfoDispatcher:
    hass: Incomplete
    _providers: dict[str, HardwareFirmwareInfoModule]
    _notification_callbacks: defaultdict[str, set[Callable[[FirmwareInfo], None]]]
    def __init__(self, hass: HomeAssistant) -> None: ...
    def register_firmware_info_provider(self, domain: str, platform: HardwareFirmwareInfoModule) -> None: ...
    def register_firmware_info_callback(self, device: str, callback: Callable[[FirmwareInfo], None]) -> CALLBACK_TYPE: ...
    async def notify_firmware_info(self, domain: str, firmware_info: FirmwareInfo) -> None: ...
    async def iter_firmware_info(self) -> AsyncIterator[FirmwareInfo]: ...

@hass_callback
def async_register_firmware_info_provider(hass: HomeAssistant, domain: str, platform: HardwareFirmwareInfoModule) -> None: ...
@hass_callback
def async_register_firmware_info_callback(hass: HomeAssistant, device: str, callback: Callable[[FirmwareInfo], None]) -> CALLBACK_TYPE: ...
@hass_callback
def async_notify_firmware_info(hass: HomeAssistant, domain: str, firmware_info: FirmwareInfo) -> Awaitable[None]: ...
