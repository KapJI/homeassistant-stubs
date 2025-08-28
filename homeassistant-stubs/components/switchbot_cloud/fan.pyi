from . import SwitchbotCloudData as SwitchbotCloudData
from .const import AFTER_COMMAND_REFRESH as AFTER_COMMAND_REFRESH, AirPurifierMode as AirPurifierMode, DOMAIN as DOMAIN
from .entity import SwitchBotCloudEntity as SwitchBotCloudEntity
from _typeshed import Incomplete
from homeassistant.components.fan import FanEntity as FanEntity, FanEntityFeature as FanEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import STATE_ON as STATE_ON
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from switchbot_api import SwitchBotAPI as SwitchBotAPI
from typing import Any

_LOGGER: Incomplete
PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, config: ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class SwitchBotCloudFan(SwitchBotCloudEntity, FanEntity):
    _attr_name: Incomplete
    _api: SwitchBotAPI
    _attr_supported_features: Incomplete
    _attr_preset_modes: Incomplete
    _attr_is_on: bool | None
    @property
    def is_on(self) -> bool | None: ...
    _attr_preset_mode: Incomplete
    _attr_percentage: Incomplete
    def _set_attributes(self) -> None: ...
    async def async_turn_on(self, percentage: int | None = None, preset_mode: str | None = None, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_set_percentage(self, percentage: int) -> None: ...
    async def async_set_preset_mode(self, preset_mode: str) -> None: ...

class SwitchBotAirPurifierEntity(SwitchBotCloudEntity, FanEntity):
    _api: SwitchBotAPI
    _attr_supported_features: Incomplete
    _attr_preset_modes: Incomplete
    _attr_translation_key: str
    _attr_name: Incomplete
    _attr_is_on: bool | None
    @property
    def is_on(self) -> bool | None: ...
    _attr_preset_mode: Incomplete
    def _set_attributes(self) -> None: ...
    async def async_set_preset_mode(self, preset_mode: str) -> None: ...
    async def async_turn_on(self, percentage: int | None = None, preset_mode: str | None = None, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
