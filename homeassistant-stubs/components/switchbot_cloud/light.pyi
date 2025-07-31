from . import SwitchBotCoordinator as SwitchBotCoordinator, SwitchbotCloudData as SwitchbotCloudData
from .const import AFTER_COMMAND_REFRESH as AFTER_COMMAND_REFRESH, DOMAIN as DOMAIN
from .entity import SwitchBotCloudEntity as SwitchBotCloudEntity
from _typeshed import Incomplete
from homeassistant.components.light import ColorMode as ColorMode, LightEntity as LightEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from switchbot_api import Device as Device, Remote as Remote, SwitchBotAPI as SwitchBotAPI
from typing import Any

def value_map_brightness(value: int) -> int: ...
async def async_setup_entry(hass: HomeAssistant, config: ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class SwitchBotCloudLight(SwitchBotCloudEntity, LightEntity):
    _attr_is_on: bool | None
    _attr_name: str | None
    _attr_color_mode: Incomplete
    _attr_brightness: int | None
    _attr_rgb_color: tuple | None
    _attr_color_temp_kelvin: int | None
    def _set_attributes(self) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def _send_brightness_command(self, brightness: int) -> None: ...
    async def _send_rgb_color_command(self, rgb_color: tuple) -> None: ...
    async def _send_color_temperature_command(self, color_temp_kelvin: int) -> None: ...

class SwitchBotCloudStripLight(SwitchBotCloudLight):
    _attr_supported_color_modes: Incomplete

class SwitchBotCloudRGBWWLight(SwitchBotCloudLight):
    _attr_max_color_temp_kelvin: int
    _attr_min_color_temp_kelvin: int
    _attr_supported_color_modes: Incomplete
    async def _send_brightness_command(self, brightness: int) -> None: ...
    async def _send_rgb_color_command(self, rgb_color: tuple) -> None: ...

@callback
def _async_make_entity(api: SwitchBotAPI, device: Device | Remote, coordinator: SwitchBotCoordinator) -> SwitchBotCloudStripLight | SwitchBotCloudRGBWWLight: ...
