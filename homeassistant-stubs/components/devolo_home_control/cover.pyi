from .const import DOMAIN as DOMAIN
from .devolo_multi_level_switch import DevoloMultiLevelSwitchDeviceEntity as DevoloMultiLevelSwitchDeviceEntity
from devolo_home_control_api.devices.zwave import Zwave as Zwave
from devolo_home_control_api.homecontrol import HomeControl as HomeControl
from homeassistant.components.cover import CoverEntity as CoverEntity, DEVICE_CLASS_BLIND as DEVICE_CLASS_BLIND, SUPPORT_CLOSE as SUPPORT_CLOSE, SUPPORT_OPEN as SUPPORT_OPEN, SUPPORT_SET_POSITION as SUPPORT_SET_POSITION
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DevoloCoverDeviceEntity(DevoloMultiLevelSwitchDeviceEntity, CoverEntity):
    _attr_device_class: Any
    _attr_supported_features: Any
    def __init__(self, homecontrol: HomeControl, device_instance: Zwave, element_uid: str) -> None: ...
    @property
    def current_cover_position(self) -> int: ...
    @property
    def is_closed(self) -> bool: ...
    def open_cover(self, **kwargs: Any) -> None: ...
    def close_cover(self, **kwargs: Any) -> None: ...
    def set_cover_position(self, **kwargs: Any) -> None: ...
