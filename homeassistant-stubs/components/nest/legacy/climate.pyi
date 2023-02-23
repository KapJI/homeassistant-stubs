from .const import DATA_NEST as DATA_NEST, DOMAIN as DOMAIN, SIGNAL_NEST_UPDATE as SIGNAL_NEST_UPDATE
from _typeshed import Incomplete
from homeassistant.components.climate import ATTR_TARGET_TEMP_HIGH as ATTR_TARGET_TEMP_HIGH, ATTR_TARGET_TEMP_LOW as ATTR_TARGET_TEMP_LOW, ClimateEntity as ClimateEntity, ClimateEntityFeature as ClimateEntityFeature, FAN_AUTO as FAN_AUTO, FAN_ON as FAN_ON, HVACAction as HVACAction, HVACMode as HVACMode, PLATFORM_SCHEMA as PLATFORM_SCHEMA, PRESET_AWAY as PRESET_AWAY, PRESET_ECO as PRESET_ECO, PRESET_NONE as PRESET_NONE
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, CONF_SCAN_INTERVAL as CONF_SCAN_INTERVAL, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

_LOGGER: Incomplete
NEST_MODE_HEAT_COOL: str
NEST_MODE_ECO: str
NEST_MODE_HEAT: str
NEST_MODE_COOL: str
NEST_MODE_OFF: str
MODE_HASS_TO_NEST: Incomplete
MODE_NEST_TO_HASS: Incomplete
ACTION_NEST_TO_HASS: Incomplete
PRESET_AWAY_AND_ECO: str
PRESET_MODES: Incomplete

async def async_setup_legacy_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class NestThermostat(ClimateEntity):
    _attr_should_poll: bool
    _unit: Incomplete
    structure: Incomplete
    device: Incomplete
    _fan_modes: Incomplete
    _attr_supported_features: Incomplete
    _operation_list: Incomplete
    _has_fan: Incomplete
    _away: Incomplete
    _location: Incomplete
    _name: Incomplete
    _humidity: Incomplete
    _target_temperature: Incomplete
    _temperature: Incomplete
    _temperature_scale: Incomplete
    _mode: Incomplete
    _action: Incomplete
    _fan: Incomplete
    _eco_temperature: Incomplete
    _is_locked: Incomplete
    _locked_temperature: Incomplete
    _min_temperature: Incomplete
    _max_temperature: Incomplete
    def __init__(self, structure, device, temp_unit) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @property
    def unique_id(self): ...
    @property
    def device_info(self) -> DeviceInfo: ...
    @property
    def name(self): ...
    @property
    def temperature_unit(self): ...
    @property
    def current_temperature(self): ...
    @property
    def hvac_mode(self) -> HVACMode: ...
    @property
    def hvac_action(self) -> HVACAction: ...
    @property
    def target_temperature(self): ...
    @property
    def target_temperature_low(self): ...
    @property
    def target_temperature_high(self): ...
    def set_temperature(self, **kwargs) -> None: ...
    def set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    @property
    def hvac_modes(self) -> list[HVACMode]: ...
    @property
    def preset_mode(self): ...
    @property
    def preset_modes(self): ...
    def set_preset_mode(self, preset_mode) -> None: ...
    @property
    def fan_mode(self): ...
    @property
    def fan_modes(self): ...
    def set_fan_mode(self, fan_mode) -> None: ...
    @property
    def min_temp(self): ...
    @property
    def max_temp(self): ...
    def update(self) -> None: ...
