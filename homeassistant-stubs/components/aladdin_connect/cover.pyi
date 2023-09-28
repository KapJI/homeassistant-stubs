from .const import DOMAIN as DOMAIN, STATES_MAP as STATES_MAP, SUPPORTED_FEATURES as SUPPORTED_FEATURES
from .model import DoorDevice as DoorDevice
from AIOAladdinConnect import AladdinConnectClient as AladdinConnectClient
from _typeshed import Incomplete
from homeassistant.components.cover import CoverDeviceClass as CoverDeviceClass, CoverEntity as CoverEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import STATE_CLOSED as STATE_CLOSED, STATE_CLOSING as STATE_CLOSING, STATE_OPENING as STATE_OPENING
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, PlatformNotReady as PlatformNotReady
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

SCAN_INTERVAL: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AladdinDevice(CoverEntity):
    _attr_device_class: Incomplete
    _attr_supported_features = SUPPORTED_FEATURES
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    _acc: Incomplete
    _device_id: Incomplete
    _number: Incomplete
    _serial: Incomplete
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, acc: AladdinConnectClient, device: DoorDevice, entry: ConfigEntry) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    async def async_close_cover(self, **kwargs: Any) -> None: ...
    async def async_open_cover(self, **kwargs: Any) -> None: ...
    _attr_available: bool
    async def async_update(self) -> None: ...
    @property
    def is_closed(self) -> bool | None: ...
    @property
    def is_closing(self) -> bool: ...
    @property
    def is_opening(self) -> bool: ...
