from _typeshed import Incomplete
from homeassistant.components.fan import FanEntity as FanEntity, FanEntityFeature as FanEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any, override

PRESET_MODE_AUTO: str
PRESET_MODE_SMART: str
PRESET_MODE_SLEEP: str
PRESET_MODE_ON: str
FULL_SUPPORT: Incomplete
LIMITED_SUPPORT: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class BaseDemoFan(FanEntity):
    _attr_should_poll: bool
    _attr_translation_key: str
    hass: Incomplete
    _unique_id: Incomplete
    _attr_supported_features: Incomplete
    _percentage: int | None
    _preset_modes: Incomplete
    _preset_mode: str | None
    _oscillating: bool | None
    _direction: str | None
    _attr_name: Incomplete
    def __init__(self, hass: HomeAssistant, unique_id: str, name: str, supported_features: FanEntityFeature, preset_modes: list[str] | None) -> None: ...
    @property
    @override
    def unique_id(self) -> str: ...
    @property
    @override
    def current_direction(self) -> str | None: ...
    @property
    @override
    def oscillating(self) -> bool | None: ...

class DemoPercentageFan(BaseDemoFan, FanEntity):
    @property
    @override
    def percentage(self) -> int | None: ...
    @property
    @override
    def speed_count(self) -> int: ...
    _percentage: Incomplete
    _preset_mode: Incomplete
    @override
    def set_percentage(self, percentage: int) -> None: ...
    @property
    @override
    def preset_mode(self) -> str | None: ...
    @property
    @override
    def preset_modes(self) -> list[str] | None: ...
    @override
    def set_preset_mode(self, preset_mode: str) -> None: ...
    @override
    def turn_on(self, percentage: int | None = None, preset_mode: str | None = None, **kwargs: Any) -> None: ...
    @override
    def turn_off(self, **kwargs: Any) -> None: ...
    _direction: Incomplete
    @override
    def set_direction(self, direction: str) -> None: ...
    _oscillating: Incomplete
    @override
    def oscillate(self, oscillating: bool) -> None: ...

class AsyncDemoPercentageFan(BaseDemoFan, FanEntity):
    @property
    @override
    def percentage(self) -> int | None: ...
    @property
    @override
    def speed_count(self) -> int: ...
    _percentage: Incomplete
    _preset_mode: Incomplete
    @override
    async def async_set_percentage(self, percentage: int) -> None: ...
    @property
    @override
    def preset_mode(self) -> str | None: ...
    @property
    @override
    def preset_modes(self) -> list[str] | None: ...
    @override
    async def async_set_preset_mode(self, preset_mode: str) -> None: ...
    @override
    async def async_turn_on(self, percentage: int | None = None, preset_mode: str | None = None, **kwargs: Any) -> None: ...
    @override
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    _direction: Incomplete
    @override
    async def async_set_direction(self, direction: str) -> None: ...
    _oscillating: Incomplete
    @override
    async def async_oscillate(self, oscillating: bool) -> None: ...
