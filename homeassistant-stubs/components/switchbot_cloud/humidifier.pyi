from . import SwitchbotCloudData as SwitchbotCloudData
from .const import AFTER_COMMAND_REFRESH as AFTER_COMMAND_REFRESH, DOMAIN as DOMAIN, HUMIDITY_LEVELS as HUMIDITY_LEVELS, Humidifier2Mode as Humidifier2Mode
from .entity import SwitchBotCloudEntity as SwitchBotCloudEntity
from _typeshed import Incomplete
from homeassistant.components.humidifier import HumidifierDeviceClass as HumidifierDeviceClass, HumidifierEntity as HumidifierEntity, HumidifierEntityFeature as HumidifierEntityFeature, MODE_AUTO as MODE_AUTO, MODE_NORMAL as MODE_NORMAL
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import STATE_ON as STATE_ON
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class SwitchBotHumidifier(SwitchBotCloudEntity, HumidifierEntity):
    _attr_supported_features: Incomplete
    _attr_device_class: Incomplete
    _attr_available_modes: Incomplete
    _attr_min_humidity: int
    _attr_translation_key: str
    _attr_name: Incomplete
    _attr_target_humidity: int
    _attr_is_on: Incomplete
    _attr_mode: Incomplete
    _attr_current_humidity: Incomplete
    def _set_attributes(self) -> None: ...
    async def async_set_humidity(self, humidity: int) -> None: ...
    async def async_set_mode(self, mode: str) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    def _map_humidity_to_supported_level(self, humidity: int) -> tuple[int, int]: ...

class SwitchBotEvaporativeHumidifier(SwitchBotCloudEntity, HumidifierEntity):
    _attr_supported_features: Incomplete
    _attr_device_class: Incomplete
    _attr_available_modes: Incomplete
    _attr_translation_key: str
    _attr_name: Incomplete
    _attr_target_humidity: int
    _attr_is_on: Incomplete
    _attr_mode: Incomplete
    _attr_current_humidity: Incomplete
    def _set_attributes(self) -> None: ...
    async def async_set_humidity(self, humidity: int) -> None: ...
    async def async_set_mode(self, mode: str) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
