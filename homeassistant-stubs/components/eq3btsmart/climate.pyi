from .const import CurrentTemperatureSelector as CurrentTemperatureSelector, DEVICE_MODEL as DEVICE_MODEL, DOMAIN as DOMAIN, EQ_TO_HA_HVAC as EQ_TO_HA_HVAC, HA_TO_EQ_HVAC as HA_TO_EQ_HVAC, MANUFACTURER as MANUFACTURER, Preset as Preset, SIGNAL_THERMOSTAT_CONNECTED as SIGNAL_THERMOSTAT_CONNECTED, SIGNAL_THERMOSTAT_DISCONNECTED as SIGNAL_THERMOSTAT_DISCONNECTED, TargetTemperatureSelector as TargetTemperatureSelector
from .entity import Eq3Entity as Eq3Entity
from .models import Eq3Config as Eq3Config, Eq3ConfigEntryData as Eq3ConfigEntryData
from _typeshed import Incomplete
from eq3btsmart import Thermostat as Thermostat
from eq3btsmart.const import EQ3BT_MAX_TEMP, EQ3BT_OFF_TEMP
from homeassistant.components.climate import ATTR_HVAC_MODE as ATTR_HVAC_MODE, ClimateEntity as ClimateEntity, ClimateEntityFeature as ClimateEntityFeature, HVACAction as HVACAction, HVACMode as HVACMode, PRESET_NONE as PRESET_NONE
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, PRECISION_HALVES as PRECISION_HALVES, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ServiceValidationError as ServiceValidationError
from homeassistant.helpers.device_registry import CONNECTION_BLUETOOTH as CONNECTION_BLUETOOTH, DeviceInfo as DeviceInfo
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.util import slugify as slugify
from typing import Any

_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class Eq3Climate(Eq3Entity, ClimateEntity):
    _attr_name: Incomplete
    _attr_supported_features: Incomplete
    _attr_temperature_unit: Incomplete
    _attr_min_temp = EQ3BT_OFF_TEMP
    _attr_max_temp = EQ3BT_MAX_TEMP
    _attr_precision = PRECISION_HALVES
    _attr_hvac_modes: Incomplete
    _attr_preset_modes: Incomplete
    _attr_should_poll: bool
    _attr_available: bool
    _attr_hvac_mode: HVACMode | None
    _attr_hvac_action: HVACAction | None
    _attr_preset_mode: str | None
    _target_temperature: float | None
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, eq3_config: Eq3Config, thermostat: Thermostat) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    def _async_on_disconnected(self) -> None: ...
    def _async_on_connected(self) -> None: ...
    def _async_on_updated(self) -> None: ...
    _attr_current_temperature: Incomplete
    _attr_target_temperature: Incomplete
    def _async_on_status_updated(self) -> None: ...
    def _async_on_device_updated(self) -> None: ...
    def _get_current_temperature(self) -> float | None: ...
    def _get_target_temperature(self) -> float | None: ...
    def _get_current_preset_mode(self) -> str: ...
    def _get_current_hvac_action(self) -> HVACAction: ...
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    async def async_set_preset_mode(self, preset_mode: str) -> None: ...
