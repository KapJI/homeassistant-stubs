import pyatmo
from .const import ATTR_HEATING_POWER_REQUEST as ATTR_HEATING_POWER_REQUEST, ATTR_SCHEDULE_NAME as ATTR_SCHEDULE_NAME, ATTR_SELECTED_SCHEDULE as ATTR_SELECTED_SCHEDULE, DATA_HANDLER as DATA_HANDLER, DATA_HOMES as DATA_HOMES, DATA_SCHEDULES as DATA_SCHEDULES, DOMAIN as DOMAIN, EVENT_TYPE_CANCEL_SET_POINT as EVENT_TYPE_CANCEL_SET_POINT, EVENT_TYPE_SCHEDULE as EVENT_TYPE_SCHEDULE, EVENT_TYPE_SET_POINT as EVENT_TYPE_SET_POINT, EVENT_TYPE_THERM_MODE as EVENT_TYPE_THERM_MODE, NETATMO_CREATE_BATTERY as NETATMO_CREATE_BATTERY, SERVICE_SET_SCHEDULE as SERVICE_SET_SCHEDULE, SIGNAL_NAME as SIGNAL_NAME, TYPE_ENERGY as TYPE_ENERGY
from .data_handler import CLIMATE_STATE_CLASS_NAME as CLIMATE_STATE_CLASS_NAME, CLIMATE_TOPOLOGY_CLASS_NAME as CLIMATE_TOPOLOGY_CLASS_NAME, NetatmoDataHandler as NetatmoDataHandler, NetatmoDevice as NetatmoDevice
from .netatmo_entity_base import NetatmoBase as NetatmoBase
from homeassistant.components.climate import ClimateEntity as ClimateEntity
from homeassistant.components.climate.const import CURRENT_HVAC_HEAT as CURRENT_HVAC_HEAT, CURRENT_HVAC_IDLE as CURRENT_HVAC_IDLE, DEFAULT_MIN_TEMP as DEFAULT_MIN_TEMP, HVAC_MODE_AUTO as HVAC_MODE_AUTO, HVAC_MODE_HEAT as HVAC_MODE_HEAT, HVAC_MODE_OFF as HVAC_MODE_OFF, PRESET_AWAY as PRESET_AWAY, PRESET_BOOST as PRESET_BOOST, SUPPORT_PRESET_MODE as SUPPORT_PRESET_MODE, SUPPORT_TARGET_TEMPERATURE as SUPPORT_TARGET_TEMPERATURE
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_SUGGESTED_AREA as ATTR_SUGGESTED_AREA, ATTR_TEMPERATURE as ATTR_TEMPERATURE, PRECISION_HALVES as PRECISION_HALVES, STATE_OFF as STATE_OFF, TEMP_CELSIUS as TEMP_CELSIUS
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import PlatformNotReady as PlatformNotReady
from homeassistant.helpers import entity_platform as entity_platform
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect, async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

_LOGGER: Any
PRESET_FROST_GUARD: str
PRESET_SCHEDULE: str
PRESET_MANUAL: str
SUPPORT_FLAGS: Any
SUPPORT_HVAC: Any
SUPPORT_PRESET: Any
STATE_NETATMO_SCHEDULE: str
STATE_NETATMO_HG: str
STATE_NETATMO_MAX: str
STATE_NETATMO_AWAY = PRESET_AWAY
STATE_NETATMO_OFF = STATE_OFF
STATE_NETATMO_MANUAL: str
STATE_NETATMO_HOME: str
PRESET_MAP_NETATMO: Any
NETATMO_MAP_PRESET: Any
HVAC_MAP_NETATMO: Any
CURRENT_HVAC_MAP_NETATMO: Any
DEFAULT_MAX_TEMP: int
NA_THERM: str
NA_VALVE: str

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class NetatmoThermostat(NetatmoBase, ClimateEntity):
    _attr_hvac_mode: Any
    _attr_max_temp: Any
    _attr_preset_modes: Any
    _attr_supported_features: Any
    _attr_target_temperature_step: Any
    _attr_temperature_unit: Any
    _room: Any
    _id: Any
    _climate_state_class: Any
    _climate_state: Any
    _model: Any
    _netatmo_type: Any
    _attr_name: Any
    _away: Any
    _connected: Any
    _away_temperature: Any
    _hg_temperature: Any
    _boilerstatus: Any
    _selected_schedule: Any
    _attr_hvac_modes: Any
    _attr_unique_id: Any
    def __init__(self, data_handler: NetatmoDataHandler, room: pyatmo.climate.NetatmoRoom) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    _attr_preset_mode: Any
    _attr_target_temperature: Any
    def handle_event(self, event: dict) -> None: ...
    @property
    def hvac_action(self) -> Union[str, None]: ...
    async def async_set_hvac_mode(self, hvac_mode: str) -> None: ...
    async def async_set_preset_mode(self, preset_mode: str) -> None: ...
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self) -> None: ...
    async def async_turn_on(self) -> None: ...
    @property
    def available(self) -> bool: ...
    _attr_current_temperature: Any
    def async_update_callback(self) -> None: ...
    async def _async_service_set_schedule(self, **kwargs: Any) -> None: ...
    @property
    def device_info(self) -> DeviceInfo: ...
