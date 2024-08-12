from _typeshed import Incomplete
from homeassistant.components.fan import FanEntity as FanEntity, FanEntityFeature as FanEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

PRESET_MODE_AUTO: str
PRESET_MODE_SMART: str
PRESET_MODE_SLEEP: str
PRESET_MODE_ON: str
FULL_SUPPORT: Incomplete
LIMITED_SUPPORT: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class BaseDemoFan(FanEntity):
    _attr_should_poll: bool
    _attr_translation_key: str
    _enable_turn_on_off_backwards_compatibility: bool
    hass: Incomplete
    _unique_id: Incomplete
    _attr_supported_features: Incomplete
    _percentage: Incomplete
    _preset_modes: Incomplete
    _preset_mode: Incomplete
    _oscillating: Incomplete
    _direction: Incomplete
    _attr_name: Incomplete
    def __init__(self, hass: HomeAssistant, unique_id: str, name: str, supported_features: FanEntityFeature, preset_modes: list[str] | None) -> None: ...
    @property
    def unique_id(self) -> str: ...
    @property
    def current_direction(self) -> str | None: ...
    @property
    def oscillating(self) -> bool | None: ...

class DemoPercentageFan(BaseDemoFan, FanEntity):
    @property
    def percentage(self) -> int | None: ...
    @property
    def speed_count(self) -> int: ...
    _percentage: Incomplete
    _preset_mode: Incomplete
    def set_percentage(self, percentage: int) -> None: ...
    @property
    def preset_mode(self) -> str | None: ...
    @property
    def preset_modes(self) -> list[str] | None: ...
    def set_preset_mode(self, preset_mode: str) -> None: ...
    def turn_on(self, percentage: int | None = None, preset_mode: str | None = None, **kwargs: Any) -> None: ...
    def turn_off(self, **kwargs: Any) -> None: ...
    _direction: Incomplete
    def set_direction(self, direction: str) -> None: ...
    _oscillating: Incomplete
    def oscillate(self, oscillating: bool) -> None: ...

class AsyncDemoPercentageFan(BaseDemoFan, FanEntity):
    @property
    def percentage(self) -> int | None: ...
    @property
    def speed_count(self) -> int: ...
    _percentage: Incomplete
    _preset_mode: Incomplete
    async def async_set_percentage(self, percentage: int) -> None: ...
    @property
    def preset_mode(self) -> str | None: ...
    @property
    def preset_modes(self) -> list[str] | None: ...
    async def async_set_preset_mode(self, preset_mode: str) -> None: ...
    async def async_turn_on(self, percentage: int | None = None, preset_mode: str | None = None, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    _direction: Incomplete
    async def async_set_direction(self, direction: str) -> None: ...
    _oscillating: Incomplete
    async def async_oscillate(self, oscillating: bool) -> None: ...
