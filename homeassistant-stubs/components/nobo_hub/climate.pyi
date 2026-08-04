from . import NoboHubConfigEntry as NoboHubConfigEntry
from .const import ATTR_TEMP_COMFORT_C as ATTR_TEMP_COMFORT_C, ATTR_TEMP_ECO_C as ATTR_TEMP_ECO_C, CONF_OVERRIDE_TYPE as CONF_OVERRIDE_TYPE, DOMAIN as DOMAIN, OVERRIDE_TYPE_NOW as OVERRIDE_TYPE_NOW
from .entity import NoboBaseEntity as NoboBaseEntity
from _typeshed import Incomplete
from homeassistant.components.climate import ATTR_TARGET_TEMP_HIGH as ATTR_TARGET_TEMP_HIGH, ATTR_TARGET_TEMP_LOW as ATTR_TARGET_TEMP_LOW, ClimateEntity as ClimateEntity, ClimateEntityFeature as ClimateEntityFeature, HVACMode as HVACMode, PRESET_AWAY as PRESET_AWAY, PRESET_COMFORT as PRESET_COMFORT, PRESET_ECO as PRESET_ECO, PRESET_NONE as PRESET_NONE
from homeassistant.const import ATTR_NAME as ATTR_NAME, PRECISION_TENTHS as PRECISION_TENTHS, PRECISION_WHOLE as PRECISION_WHOLE, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pynobo import nobo
from typing import Any, override

PARALLEL_UPDATES: int
SUPPORT_FLAGS: Incomplete
PRESET_MODES: Incomplete
MIN_TEMPERATURE: int
MAX_TEMPERATURE: int

async def async_setup_entry(hass: HomeAssistant, config_entry: NoboHubConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class NoboZone(NoboBaseEntity, ClimateEntity):
    _attr_name: Incomplete
    _attr_max_temp = MAX_TEMPERATURE
    _attr_min_temp = MIN_TEMPERATURE
    _attr_precision = PRECISION_TENTHS
    _attr_hvac_modes: Incomplete
    _attr_hvac_mode: Incomplete
    _attr_preset_modes = PRESET_MODES
    _attr_supported_features = SUPPORT_FLAGS
    _attr_temperature_unit: Incomplete
    _attr_target_temperature_step = PRECISION_WHOLE
    _attr_should_poll: bool
    _id: Incomplete
    _attr_unique_id: Incomplete
    _override_type: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, hass: HomeAssistant, zone_id: str, hub: nobo, override_type: str, entry_id: str) -> None: ...
    @override
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    @override
    async def async_set_preset_mode(self, preset_mode: str) -> None: ...
    async def _apply_preset(self, preset_mode: str, translation_key: str) -> None: ...
    @override
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    async def async_update(self) -> None: ...
    @property
    @override
    def available(self) -> bool: ...
    _attr_preset_mode: Incomplete
    _attr_current_temperature: Incomplete
    _attr_target_temperature_high: Incomplete
    _attr_target_temperature_low: Incomplete
    @callback
    @override
    def _read_state(self) -> None: ...
