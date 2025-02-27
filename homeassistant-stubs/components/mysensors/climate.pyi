from . import setup_mysensors_platform as setup_mysensors_platform
from .const import DiscoveryInfo as DiscoveryInfo, MYSENSORS_DISCOVERY as MYSENSORS_DISCOVERY
from .entity import MySensorsChildEntity as MySensorsChildEntity
from .helpers import on_unload as on_unload
from _typeshed import Incomplete
from homeassistant.components.climate import ATTR_TARGET_TEMP_HIGH as ATTR_TARGET_TEMP_HIGH, ATTR_TARGET_TEMP_LOW as ATTR_TARGET_TEMP_LOW, ClimateEntity as ClimateEntity, ClimateEntityFeature as ClimateEntityFeature, HVACMode as HVACMode
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, Platform as Platform, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.util.unit_system import METRIC_SYSTEM as METRIC_SYSTEM
from typing import Any

DICT_HA_TO_MYS: Incomplete
DICT_MYS_TO_HA: Incomplete
FAN_LIST: Incomplete
OPERATION_LIST: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class MySensorsHVAC(MySensorsChildEntity, ClimateEntity):
    _attr_hvac_modes = OPERATION_LIST
    @property
    def supported_features(self) -> ClimateEntityFeature: ...
    @property
    def temperature_unit(self) -> str: ...
    @property
    def current_temperature(self) -> float | None: ...
    @property
    def target_temperature(self) -> float | None: ...
    @property
    def target_temperature_high(self) -> float | None: ...
    @property
    def target_temperature_low(self) -> float | None: ...
    @property
    def hvac_mode(self) -> HVACMode: ...
    @property
    def fan_mode(self) -> str | None: ...
    @property
    def fan_modes(self) -> list[str]: ...
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    async def async_set_fan_mode(self, fan_mode: str) -> None: ...
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    @callback
    def _async_update(self) -> None: ...
