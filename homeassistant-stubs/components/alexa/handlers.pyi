from .config import AbstractConfig as AbstractConfig
from .const import API_TEMP_UNITS as API_TEMP_UNITS, API_THERMOSTAT_MODES as API_THERMOSTAT_MODES, API_THERMOSTAT_MODES_CUSTOM as API_THERMOSTAT_MODES_CUSTOM, API_THERMOSTAT_PRESETS as API_THERMOSTAT_PRESETS, Cause as Cause, DATE_FORMAT as DATE_FORMAT, Inputs as Inputs, PRESET_MODE_NA as PRESET_MODE_NA
from .entities import async_get_entities as async_get_entities
from .errors import AlexaInvalidDirectiveError as AlexaInvalidDirectiveError, AlexaInvalidValueError as AlexaInvalidValueError, AlexaSecurityPanelAuthorizationRequired as AlexaSecurityPanelAuthorizationRequired, AlexaTempRangeError as AlexaTempRangeError, AlexaUnsupportedThermostatModeError as AlexaUnsupportedThermostatModeError, AlexaUnsupportedThermostatTargetStateError as AlexaUnsupportedThermostatTargetStateError, AlexaVideoActionNotPermittedForContentError as AlexaVideoActionNotPermittedForContentError
from .state_report import AlexaDirective as AlexaDirective, AlexaResponse as AlexaResponse, async_enable_proactive_mode as async_enable_proactive_mode
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from homeassistant import core as ha
from homeassistant.components import button as button, camera as camera, climate as climate, cover as cover, fan as fan, group as group, humidifier as humidifier, input_button as input_button, input_number as input_number, light as light, media_player as media_player, number as number, remote as remote, timer as timer, vacuum as vacuum, valve as valve, water_heater as water_heater
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, ATTR_ENTITY_PICTURE as ATTR_ENTITY_PICTURE, ATTR_SUPPORTED_FEATURES as ATTR_SUPPORTED_FEATURES, ATTR_TEMPERATURE as ATTR_TEMPERATURE, SERVICE_ALARM_ARM_AWAY as SERVICE_ALARM_ARM_AWAY, SERVICE_ALARM_ARM_HOME as SERVICE_ALARM_ARM_HOME, SERVICE_ALARM_ARM_NIGHT as SERVICE_ALARM_ARM_NIGHT, SERVICE_ALARM_DISARM as SERVICE_ALARM_DISARM, SERVICE_LOCK as SERVICE_LOCK, SERVICE_MEDIA_NEXT_TRACK as SERVICE_MEDIA_NEXT_TRACK, SERVICE_MEDIA_PAUSE as SERVICE_MEDIA_PAUSE, SERVICE_MEDIA_PLAY as SERVICE_MEDIA_PLAY, SERVICE_MEDIA_PREVIOUS_TRACK as SERVICE_MEDIA_PREVIOUS_TRACK, SERVICE_MEDIA_STOP as SERVICE_MEDIA_STOP, SERVICE_SET_COVER_POSITION as SERVICE_SET_COVER_POSITION, SERVICE_SET_COVER_TILT_POSITION as SERVICE_SET_COVER_TILT_POSITION, SERVICE_TURN_OFF as SERVICE_TURN_OFF, SERVICE_TURN_ON as SERVICE_TURN_ON, SERVICE_UNLOCK as SERVICE_UNLOCK, SERVICE_VOLUME_DOWN as SERVICE_VOLUME_DOWN, SERVICE_VOLUME_MUTE as SERVICE_VOLUME_MUTE, SERVICE_VOLUME_SET as SERVICE_VOLUME_SET, SERVICE_VOLUME_UP as SERVICE_VOLUME_UP, STATE_ALARM_DISARMED as STATE_ALARM_DISARMED, UnitOfTemperature as UnitOfTemperature
from homeassistant.helpers import network as network
from homeassistant.util.decorator import Registry as Registry
from homeassistant.util.unit_conversion import TemperatureConverter as TemperatureConverter
from typing import Any

_LOGGER: Incomplete
DIRECTIVE_NOT_SUPPORTED: str
MIN_MAX_TEMP: Incomplete
SERVICE_SET_TEMPERATURE: Incomplete
HANDLERS: Registry[tuple[str, str], Callable[[ha.HomeAssistant, AbstractConfig, AlexaDirective, ha.Context], Coroutine[Any, Any, AlexaResponse]]]

async def async_api_discovery(hass: ha.HomeAssistant, config: AbstractConfig, directive: AlexaDirective, context: ha.Context) -> AlexaResponse: ...
async def async_api_accept_grant(hass: ha.HomeAssistant, config: AbstractConfig, directive: AlexaDirective, context: ha.Context) -> AlexaResponse: ...
async def async_api_turn_on(hass: ha.HomeAssistant, config: AbstractConfig, directive: AlexaDirective, context: ha.Context) -> AlexaResponse: ...
async def async_api_turn_off(hass: ha.HomeAssistant, config: AbstractConfig, directive: AlexaDirective, context: ha.Context) -> AlexaResponse: ...
async def async_api_set_brightness(hass: ha.HomeAssistant, config: AbstractConfig, directive: AlexaDirective, context: ha.Context) -> AlexaResponse: ...
async def async_api_adjust_brightness(hass: ha.HomeAssistant, config: AbstractConfig, directive: AlexaDirective, context: ha.Context) -> AlexaResponse: ...
async def async_api_set_color(hass: ha.HomeAssistant, config: AbstractConfig, directive: AlexaDirective, context: ha.Context) -> AlexaResponse: ...
async def async_api_set_color_temperature(hass: ha.HomeAssistant, config: AbstractConfig, directive: AlexaDirective, context: ha.Context) -> AlexaResponse: ...
async def async_api_decrease_color_temp(hass: ha.HomeAssistant, config: AbstractConfig, directive: AlexaDirective, context: ha.Context) -> AlexaResponse: ...
async def async_api_increase_color_temp(hass: ha.HomeAssistant, config: AbstractConfig, directive: AlexaDirective, context: ha.Context) -> AlexaResponse: ...
async def async_api_activate(hass: ha.HomeAssistant, config: AbstractConfig, directive: AlexaDirective, context: ha.Context) -> AlexaResponse: ...
async def async_api_deactivate(hass: ha.HomeAssistant, config: AbstractConfig, directive: AlexaDirective, context: ha.Context) -> AlexaResponse: ...
async def async_api_lock(hass: ha.HomeAssistant, config: AbstractConfig, directive: AlexaDirective, context: ha.Context) -> AlexaResponse: ...
async def async_api_unlock(hass: ha.HomeAssistant, config: AbstractConfig, directive: AlexaDirective, context: ha.Context) -> AlexaResponse: ...
async def async_api_set_volume(hass: ha.HomeAssistant, config: AbstractConfig, directive: AlexaDirective, context: ha.Context) -> AlexaResponse: ...
async def async_api_select_input(hass: ha.HomeAssistant, config: AbstractConfig, directive: AlexaDirective, context: ha.Context) -> AlexaResponse: ...
async def async_api_adjust_volume(hass: ha.HomeAssistant, config: AbstractConfig, directive: AlexaDirective, context: ha.Context) -> AlexaResponse: ...
async def async_api_adjust_volume_step(hass: ha.HomeAssistant, config: AbstractConfig, directive: AlexaDirective, context: ha.Context) -> AlexaResponse: ...
async def async_api_set_mute(hass: ha.HomeAssistant, config: AbstractConfig, directive: AlexaDirective, context: ha.Context) -> AlexaResponse: ...
async def async_api_play(hass: ha.HomeAssistant, config: AbstractConfig, directive: AlexaDirective, context: ha.Context) -> AlexaResponse: ...
async def async_api_pause(hass: ha.HomeAssistant, config: AbstractConfig, directive: AlexaDirective, context: ha.Context) -> AlexaResponse: ...
async def async_api_stop(hass: ha.HomeAssistant, config: AbstractConfig, directive: AlexaDirective, context: ha.Context) -> AlexaResponse: ...
async def async_api_next(hass: ha.HomeAssistant, config: AbstractConfig, directive: AlexaDirective, context: ha.Context) -> AlexaResponse: ...
async def async_api_previous(hass: ha.HomeAssistant, config: AbstractConfig, directive: AlexaDirective, context: ha.Context) -> AlexaResponse: ...
def temperature_from_object(hass: ha.HomeAssistant, temp_obj: dict[str, Any], interval: bool = False) -> float: ...
async def async_api_set_target_temp(hass: ha.HomeAssistant, config: AbstractConfig, directive: AlexaDirective, context: ha.Context) -> AlexaResponse: ...
async def async_api_adjust_target_temp(hass: ha.HomeAssistant, config: AbstractConfig, directive: AlexaDirective, context: ha.Context) -> AlexaResponse: ...
async def async_api_set_thermostat_mode(hass: ha.HomeAssistant, config: AbstractConfig, directive: AlexaDirective, context: ha.Context) -> AlexaResponse: ...
async def async_api_reportstate(hass: ha.HomeAssistant, config: AbstractConfig, directive: AlexaDirective, context: ha.Context) -> AlexaResponse: ...
async def async_api_arm(hass: ha.HomeAssistant, config: AbstractConfig, directive: AlexaDirective, context: ha.Context) -> AlexaResponse: ...
async def async_api_disarm(hass: ha.HomeAssistant, config: AbstractConfig, directive: AlexaDirective, context: ha.Context) -> AlexaResponse: ...
async def async_api_set_mode(hass: ha.HomeAssistant, config: AbstractConfig, directive: AlexaDirective, context: ha.Context) -> AlexaResponse: ...
async def async_api_adjust_mode(hass: ha.HomeAssistant, config: AbstractConfig, directive: AlexaDirective, context: ha.Context) -> AlexaResponse: ...
async def async_api_toggle_on(hass: ha.HomeAssistant, config: AbstractConfig, directive: AlexaDirective, context: ha.Context) -> AlexaResponse: ...
async def async_api_toggle_off(hass: ha.HomeAssistant, config: AbstractConfig, directive: AlexaDirective, context: ha.Context) -> AlexaResponse: ...
async def async_api_set_range(hass: ha.HomeAssistant, config: AbstractConfig, directive: AlexaDirective, context: ha.Context) -> AlexaResponse: ...
async def async_api_adjust_range(hass: ha.HomeAssistant, config: AbstractConfig, directive: AlexaDirective, context: ha.Context) -> AlexaResponse: ...
async def async_api_changechannel(hass: ha.HomeAssistant, config: AbstractConfig, directive: AlexaDirective, context: ha.Context) -> AlexaResponse: ...
async def async_api_skipchannel(hass: ha.HomeAssistant, config: AbstractConfig, directive: AlexaDirective, context: ha.Context) -> AlexaResponse: ...
async def async_api_seek(hass: ha.HomeAssistant, config: AbstractConfig, directive: AlexaDirective, context: ha.Context) -> AlexaResponse: ...
async def async_api_set_eq_mode(hass: ha.HomeAssistant, config: AbstractConfig, directive: AlexaDirective, context: ha.Context) -> AlexaResponse: ...
async def async_api_bands_directive(hass: ha.HomeAssistant, config: AbstractConfig, directive: AlexaDirective, context: ha.Context) -> AlexaResponse: ...
async def async_api_hold(hass: ha.HomeAssistant, config: AbstractConfig, directive: AlexaDirective, context: ha.Context) -> AlexaResponse: ...
async def async_api_resume(hass: ha.HomeAssistant, config: AbstractConfig, directive: AlexaDirective, context: ha.Context) -> AlexaResponse: ...
async def async_api_initialize_camera_stream(hass: ha.HomeAssistant, config: AbstractConfig, directive: AlexaDirective, context: ha.Context) -> AlexaResponse: ...
