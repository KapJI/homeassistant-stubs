from . import LcnEntity as LcnEntity
from .const import CONF_DOMAIN_DATA as CONF_DOMAIN_DATA, CONF_LOCKABLE as CONF_LOCKABLE, CONF_MAX_TEMP as CONF_MAX_TEMP, CONF_MIN_TEMP as CONF_MIN_TEMP, CONF_SETPOINT as CONF_SETPOINT
from .helpers import DeviceConnectionType as DeviceConnectionType, InputType as InputType, get_device_connection as get_device_connection
from _typeshed import Incomplete
from homeassistant.components.climate import ClimateEntity as ClimateEntity, ClimateEntityFeature as ClimateEntityFeature, HVACMode as HVACMode
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, CONF_ADDRESS as CONF_ADDRESS, CONF_DOMAIN as CONF_DOMAIN, CONF_ENTITIES as CONF_ENTITIES, CONF_SOURCE as CONF_SOURCE, CONF_UNIT_OF_MEASUREMENT as CONF_UNIT_OF_MEASUREMENT, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

PARALLEL_UPDATES: int

def create_lcn_climate_entity(hass: HomeAssistant, entity_config: ConfigType, config_entry: ConfigEntry) -> LcnEntity: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class LcnClimate(LcnEntity, ClimateEntity):
    _enable_turn_on_off_backwards_compatibility: bool
    variable: Incomplete
    setpoint: Incomplete
    unit: Incomplete
    regulator_id: Incomplete
    is_lockable: Incomplete
    _max_temp: Incomplete
    _min_temp: Incomplete
    _current_temperature: Incomplete
    _target_temperature: Incomplete
    _is_on: bool
    _attr_hvac_modes: Incomplete
    _attr_supported_features: Incomplete
    def __init__(self, config: ConfigType, entry_id: str, device_connection: DeviceConnectionType) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    @property
    def temperature_unit(self) -> str: ...
    @property
    def current_temperature(self) -> float | None: ...
    @property
    def target_temperature(self) -> float | None: ...
    @property
    def hvac_mode(self) -> HVACMode: ...
    @property
    def max_temp(self) -> float: ...
    @property
    def min_temp(self) -> float: ...
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    def input_received(self, input_obj: InputType) -> None: ...
