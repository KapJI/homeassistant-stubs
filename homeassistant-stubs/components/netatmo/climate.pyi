from .const import ATTR_HEATING_POWER_REQUEST as ATTR_HEATING_POWER_REQUEST, ATTR_SCHEDULE_NAME as ATTR_SCHEDULE_NAME, ATTR_SELECTED_SCHEDULE as ATTR_SELECTED_SCHEDULE, CONF_URL_ENERGY as CONF_URL_ENERGY, DATA_SCHEDULES as DATA_SCHEDULES, DOMAIN as DOMAIN, EVENT_TYPE_CANCEL_SET_POINT as EVENT_TYPE_CANCEL_SET_POINT, EVENT_TYPE_SCHEDULE as EVENT_TYPE_SCHEDULE, EVENT_TYPE_SET_POINT as EVENT_TYPE_SET_POINT, EVENT_TYPE_THERM_MODE as EVENT_TYPE_THERM_MODE, NETATMO_CREATE_CLIMATE as NETATMO_CREATE_CLIMATE, SERVICE_SET_SCHEDULE as SERVICE_SET_SCHEDULE
from .data_handler import HOME as HOME, NetatmoRoom as NetatmoRoom, SIGNAL_NAME as SIGNAL_NAME
from .netatmo_entity_base import NetatmoBase as NetatmoBase
from _typeshed import Incomplete
from homeassistant.components.climate import ClimateEntity as ClimateEntity, ClimateEntityFeature as ClimateEntityFeature, DEFAULT_MIN_TEMP as DEFAULT_MIN_TEMP, HVACAction as HVACAction, HVACMode as HVACMode, PRESET_AWAY as PRESET_AWAY, PRESET_BOOST as PRESET_BOOST, PRESET_HOME as PRESET_HOME
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_SUGGESTED_AREA as ATTR_SUGGESTED_AREA, ATTR_TEMPERATURE as ATTR_TEMPERATURE, PRECISION_HALVES as PRECISION_HALVES, STATE_OFF as STATE_OFF, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import entity_platform as entity_platform
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

_LOGGER: Incomplete
PRESET_FROST_GUARD: str
PRESET_SCHEDULE: str
PRESET_MANUAL: str
SUPPORT_FLAGS: Incomplete
SUPPORT_PRESET: Incomplete
STATE_NETATMO_SCHEDULE: str
STATE_NETATMO_HG: str
STATE_NETATMO_MAX: str
STATE_NETATMO_AWAY = PRESET_AWAY
STATE_NETATMO_OFF = STATE_OFF
STATE_NETATMO_MANUAL: str
STATE_NETATMO_HOME: str
PRESET_MAP_NETATMO: Incomplete
NETATMO_MAP_PRESET: Incomplete
HVAC_MAP_NETATMO: Incomplete
CURRENT_HVAC_MAP_NETATMO: Incomplete
DEFAULT_MAX_TEMP: int
NA_THERM: str
NA_VALVE: str

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class NetatmoThermostat(NetatmoBase, ClimateEntity):
    _attr_hvac_mode: Incomplete
    _attr_max_temp: Incomplete
    _attr_preset_modes: Incomplete
    _attr_supported_features: Incomplete
    _attr_target_temperature_step: Incomplete
    _attr_temperature_unit: Incomplete
    _room: Incomplete
    _id: Incomplete
    _home_id: Incomplete
    _signal_name: Incomplete
    _model: Incomplete
    _config_url: Incomplete
    _attr_name: Incomplete
    _away: Incomplete
    _connected: Incomplete
    _away_temperature: Incomplete
    _hg_temperature: Incomplete
    _boilerstatus: Incomplete
    _selected_schedule: Incomplete
    _attr_hvac_modes: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, netatmo_device: NetatmoRoom) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    _attr_preset_mode: Incomplete
    _attr_target_temperature: Incomplete
    def handle_event(self, event: dict) -> None: ...
    @property
    def hvac_action(self) -> HVACAction: ...
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    async def async_set_preset_mode(self, preset_mode: str) -> None: ...
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self) -> None: ...
    async def async_turn_on(self) -> None: ...
    @property
    def available(self) -> bool: ...
    _attr_current_temperature: Incomplete
    def async_update_callback(self) -> None: ...
    async def _async_service_set_schedule(self, **kwargs: Any) -> None: ...
    @property
    def device_info(self) -> DeviceInfo: ...
