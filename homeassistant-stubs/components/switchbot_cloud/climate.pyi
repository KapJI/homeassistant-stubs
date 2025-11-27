from . import SwitchBotCoordinator as SwitchBotCoordinator, SwitchbotCloudData as SwitchbotCloudData
from .const import DOMAIN as DOMAIN, SMART_RADIATOR_THERMOSTAT_AFTER_COMMAND_REFRESH as SMART_RADIATOR_THERMOSTAT_AFTER_COMMAND_REFRESH
from .entity import SwitchBotCloudEntity as SwitchBotCloudEntity
from _typeshed import Incomplete
from homeassistant.components.climate import ATTR_FAN_MODE as ATTR_FAN_MODE, ATTR_TEMPERATURE as ATTR_TEMPERATURE, ClimateEntity as ClimateEntity, ClimateEntityFeature as ClimateEntityFeature, HVACMode as HVACMode, PRESET_AWAY as PRESET_AWAY, PRESET_BOOST as PRESET_BOOST, PRESET_COMFORT as PRESET_COMFORT, PRESET_ECO as PRESET_ECO, PRESET_HOME as PRESET_HOME, PRESET_NONE as PRESET_NONE, PRESET_SLEEP as PRESET_SLEEP
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import PRECISION_TENTHS as PRECISION_TENTHS, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from switchbot_api import Device as Device, Remote as Remote, SmartRadiatorThermostatMode, SwitchBotAPI as SwitchBotAPI
from typing import Any

_LOGGER: Incomplete
_SWITCHBOT_HVAC_MODES: dict[HVACMode, int]
_DEFAULT_SWITCHBOT_HVAC_MODE: Incomplete
_SWITCHBOT_FAN_MODES: dict[str, int]
_DEFAULT_SWITCHBOT_FAN_MODE: Incomplete

async def async_setup_entry(hass: HomeAssistant, config: ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class SwitchBotCloudAirConditioner(SwitchBotCloudEntity, ClimateEntity, RestoreEntity):
    _attr_assumed_state: bool
    _attr_supported_features: Incomplete
    _attr_fan_modes: Incomplete
    _attr_fan_mode: Incomplete
    _attr_hvac_modes: Incomplete
    _attr_hvac_mode: Incomplete
    _attr_temperature_unit: Incomplete
    _attr_target_temperature: int
    _attr_target_temperature_step: int
    _attr_precision: int
    _attr_name: Incomplete
    async def async_added_to_hass(self) -> None: ...
    def _get_mode(self, hvac_mode: HVACMode | None) -> int: ...
    async def _do_send_command(self, hvac_mode: HVACMode | None = None, fan_mode: str | None = None, temperature: float | None = None) -> None: ...
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    async def async_set_fan_mode(self, fan_mode: str) -> None: ...
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self) -> None: ...
    async def async_turn_on(self) -> None: ...

RADIATOR_PRESET_MODE_MAP: dict[str, SmartRadiatorThermostatMode]
RADIATOR_HA_PRESET_MODE_MAP: Incomplete

class SwitchBotCloudSmartRadiatorThermostat(SwitchBotCloudEntity, ClimateEntity):
    _attr_name: Incomplete
    _attr_supported_features: Incomplete
    _attr_max_temp: int
    _attr_min_temp: int
    _attr_target_temperature_step = PRECISION_TENTHS
    _attr_temperature_unit: Incomplete
    _attr_preset_modes: Incomplete
    _attr_preset_mode = PRESET_HOME
    _attr_hvac_modes: Incomplete
    _attr_target_temperature: Incomplete
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    async def async_set_preset_mode(self, preset_mode: str) -> None: ...
    _attr_hvac_mode: Incomplete
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    _attr_current_temperature: Incomplete
    def _set_attributes(self) -> None: ...

@callback
def _async_make_entity(api: SwitchBotAPI, device: Device | Remote, coordinator: SwitchBotCoordinator) -> SwitchBotCloudAirConditioner | SwitchBotCloudSmartRadiatorThermostat: ...
