from . import SwitchBotCoordinator as SwitchBotCoordinator, SwitchbotCloudData as SwitchbotCloudData
from .const import COVER_ENTITY_AFTER_COMMAND_REFRESH as COVER_ENTITY_AFTER_COMMAND_REFRESH, DOMAIN as DOMAIN
from .entity import SwitchBotCloudEntity as SwitchBotCloudEntity
from _typeshed import Incomplete
from homeassistant.components.cover import CoverDeviceClass as CoverDeviceClass, CoverEntity as CoverEntity, CoverEntityFeature as CoverEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from switchbot_api import Device as Device, Remote as Remote, SwitchBotAPI as SwitchBotAPI
from typing import Any

async def async_setup_entry(hass: HomeAssistant, config: ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class SwitchBotCloudCover(SwitchBotCloudEntity, CoverEntity):
    _attr_name: Incomplete
    _attr_is_closed: bool | None
    _attr_current_cover_position: Incomplete
    _attr_current_cover_tilt_position: Incomplete
    def _set_attributes(self) -> None: ...

class SwitchBotCloudCoverCurtain(SwitchBotCloudCover):
    _attr_device_class: Incomplete
    _attr_supported_features: CoverEntityFeature
    async def async_open_cover(self, **kwargs: Any) -> None: ...
    async def async_close_cover(self, **kwargs: Any) -> None: ...
    async def async_set_cover_position(self, **kwargs: Any) -> None: ...
    async def async_stop_cover(self, **kwargs: Any) -> None: ...

class SwitchBotCloudCoverRollerShade(SwitchBotCloudCover):
    _attr_device_class: Incomplete
    _attr_supported_features: CoverEntityFeature
    async def async_open_cover(self, **kwargs: Any) -> None: ...
    async def async_close_cover(self, **kwargs: Any) -> None: ...
    async def async_set_cover_position(self, **kwargs: Any) -> None: ...

class SwitchBotCloudCoverBlindTilt(SwitchBotCloudCover):
    _attr_direction: str | None
    _attr_device_class: Incomplete
    _attr_supported_features: CoverEntityFeature
    _attr_is_closed: Incomplete
    _attr_current_cover_position: Incomplete
    _attr_current_cover_tilt_position: Incomplete
    def _set_attributes(self) -> None: ...
    async def async_set_cover_tilt_position(self, **kwargs: Any) -> None: ...
    async def async_open_cover_tilt(self, **kwargs: Any) -> None: ...
    async def async_close_cover_tilt(self, **kwargs: Any) -> None: ...

class SwitchBotCloudCoverGarageDoorOpener(SwitchBotCloudCover):
    _attr_device_class: Incomplete
    _attr_supported_features: CoverEntityFeature
    _attr_is_closed: Incomplete
    def _set_attributes(self) -> None: ...
    async def async_open_cover(self, **kwargs: Any) -> None: ...
    async def async_close_cover(self, **kwargs: Any) -> None: ...

@callback
def _async_make_entity(api: SwitchBotAPI, device: Device | Remote, coordinator: SwitchBotCoordinator) -> SwitchBotCloudCoverBlindTilt | SwitchBotCloudCoverRollerShade | SwitchBotCloudCoverCurtain | SwitchBotCloudCoverGarageDoorOpener: ...
