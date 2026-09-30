import probatio
from ..const import CONF_PAYLOAD_LENGTH as CONF_PAYLOAD_LENGTH, CONF_RESPOND_TO_READ as CONF_RESPOND_TO_READ, CONF_SYNC_STATE as CONF_SYNC_STATE, CONF_VALUE as CONF_VALUE, ClimateConf as ClimateConf, ColorTempModes as ColorTempModes, CoverConf as CoverConf, DOMAIN as DOMAIN, FanConf as FanConf, FanZeroMode as FanZeroMode, SUPPORTED_PLATFORMS_UI as SUPPORTED_PLATFORMS_UI, SelectConf as SelectConf
from ..dpt import get_supported_dpts as get_supported_dpts, raw_payload_length as raw_payload_length
from ..validation import entity_category_supported as entity_category_supported, parse_entity_category as parse_entity_category, validate_number_attributes as validate_number_attributes, validate_sensor_attributes as validate_sensor_attributes
from .const import CONF_COLOR as CONF_COLOR, CONF_COLOR_TEMP_MAX as CONF_COLOR_TEMP_MAX, CONF_COLOR_TEMP_MIN as CONF_COLOR_TEMP_MIN, CONF_DATA as CONF_DATA, CONF_DPT as CONF_DPT, CONF_ENTITY as CONF_ENTITY, CONF_GA_ACTIVE as CONF_GA_ACTIVE, CONF_GA_AIR_PRESSURE as CONF_GA_AIR_PRESSURE, CONF_GA_ANGLE as CONF_GA_ANGLE, CONF_GA_BLUE_BRIGHTNESS as CONF_GA_BLUE_BRIGHTNESS, CONF_GA_BLUE_SWITCH as CONF_GA_BLUE_SWITCH, CONF_GA_BRIGHTNESS as CONF_GA_BRIGHTNESS, CONF_GA_BRIGHTNESS_EAST as CONF_GA_BRIGHTNESS_EAST, CONF_GA_BRIGHTNESS_NORTH as CONF_GA_BRIGHTNESS_NORTH, CONF_GA_BRIGHTNESS_SOUTH as CONF_GA_BRIGHTNESS_SOUTH, CONF_GA_BRIGHTNESS_WEST as CONF_GA_BRIGHTNESS_WEST, CONF_GA_COLOR as CONF_GA_COLOR, CONF_GA_COLOR_TEMP as CONF_GA_COLOR_TEMP, CONF_GA_CONTROLLER_MODE as CONF_GA_CONTROLLER_MODE, CONF_GA_CONTROLLER_STATUS as CONF_GA_CONTROLLER_STATUS, CONF_GA_DAY_NIGHT as CONF_GA_DAY_NIGHT, CONF_GA_FAN_SPEED as CONF_GA_FAN_SPEED, CONF_GA_FAN_SWING as CONF_GA_FAN_SWING, CONF_GA_FAN_SWING_HORIZONTAL as CONF_GA_FAN_SWING_HORIZONTAL, CONF_GA_FROST_ALARM as CONF_GA_FROST_ALARM, CONF_GA_GREEN_BRIGHTNESS as CONF_GA_GREEN_BRIGHTNESS, CONF_GA_GREEN_SWITCH as CONF_GA_GREEN_SWITCH, CONF_GA_HEAT_COOL as CONF_GA_HEAT_COOL, CONF_GA_HUE as CONF_GA_HUE, CONF_GA_HUMIDITY as CONF_GA_HUMIDITY, CONF_GA_HUMIDITY_CURRENT as CONF_GA_HUMIDITY_CURRENT, CONF_GA_ON_OFF as CONF_GA_ON_OFF, CONF_GA_OPERATION_MODE as CONF_GA_OPERATION_MODE, CONF_GA_OP_MODE_COMFORT as CONF_GA_OP_MODE_COMFORT, CONF_GA_OP_MODE_ECO as CONF_GA_OP_MODE_ECO, CONF_GA_OP_MODE_PROTECTION as CONF_GA_OP_MODE_PROTECTION, CONF_GA_OP_MODE_STANDBY as CONF_GA_OP_MODE_STANDBY, CONF_GA_OSCILLATION as CONF_GA_OSCILLATION, CONF_GA_POSITION_SET as CONF_GA_POSITION_SET, CONF_GA_POSITION_STATE as CONF_GA_POSITION_STATE, CONF_GA_RAIN_ALARM as CONF_GA_RAIN_ALARM, CONF_GA_RED_BRIGHTNESS as CONF_GA_RED_BRIGHTNESS, CONF_GA_RED_SWITCH as CONF_GA_RED_SWITCH, CONF_GA_SATURATION as CONF_GA_SATURATION, CONF_GA_SEND as CONF_GA_SEND, CONF_GA_SETPOINT_SHIFT as CONF_GA_SETPOINT_SHIFT, CONF_GA_SPEED as CONF_GA_SPEED, CONF_GA_STEP as CONF_GA_STEP, CONF_GA_STOP as CONF_GA_STOP, CONF_GA_SWITCH as CONF_GA_SWITCH, CONF_GA_TEMPERATURE as CONF_GA_TEMPERATURE, CONF_GA_TEMPERATURE_CURRENT as CONF_GA_TEMPERATURE_CURRENT, CONF_GA_TEMPERATURE_TARGET as CONF_GA_TEMPERATURE_TARGET, CONF_GA_UP_DOWN as CONF_GA_UP_DOWN, CONF_GA_VALVE as CONF_GA_VALVE, CONF_GA_WHITE_BRIGHTNESS as CONF_GA_WHITE_BRIGHTNESS, CONF_GA_WHITE_SWITCH as CONF_GA_WHITE_SWITCH, CONF_GA_WIND_ALARM as CONF_GA_WIND_ALARM, CONF_GA_WIND_BEARING as CONF_GA_WIND_BEARING, CONF_GA_WIND_SPEED as CONF_GA_WIND_SPEED, CONF_IGNORE_AUTO_MODE as CONF_IGNORE_AUTO_MODE, CONF_INVERT_DAY_NIGHT as CONF_INVERT_DAY_NIGHT, CONF_SPEED as CONF_SPEED, CONF_TARGET_TEMPERATURE as CONF_TARGET_TEMPERATURE
from .knx_selector import AllSerializeFirst as AllSerializeFirst, GASelector as GASelector, GroupAddressConfig as GroupAddressConfig, GroupSelect as GroupSelect, GroupSelectOption as GroupSelectOption, KNXSectionFlat as KNXSectionFlat, KnxPayloadSelector as KnxPayloadSelector, KnxSelectOptionsSelector as KnxSelectOptionsSelector, SyncStateSelector as SyncStateSelector, ga as ga
from _typeshed import Incomplete
from dataclasses import dataclass
from enum import StrEnum
from homeassistant.components.climate import HVACMode as HVACMode
from homeassistant.components.number import NumberMode as NumberMode
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass
from homeassistant.components.text import TextMode as TextMode
from homeassistant.const import CONF_ENTITY_CATEGORY as CONF_ENTITY_CATEGORY, CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_PAYLOAD as CONF_PAYLOAD, CONF_PLATFORM as CONF_PLATFORM, EntityCategory as EntityCategory, Platform as Platform
from homeassistant.helpers import selector as selector
from homeassistant.helpers.typing import VolDictType as VolDictType
from probatio import Key as Key
from typing import Annotated, Any

SyncState: Incomplete
SyncStateAllowFalse: Incomplete

@dataclass(kw_only=True, slots=True)
class BaseEntityConfig:
    name: str | None = ...
    device_info: str | None = ...
    entity_category: Annotated[EntityCategory | None, None] = ...
    @property
    def xknx_name(self) -> str: ...

def _name_or_device_required(config: BaseEntityConfig) -> BaseEntityConfig: ...
def base_entity_schema(platform: Platform) -> probatio.All: ...

@dataclass(kw_only=True, slots=True)
class KnxEntityData[KnxT]:
    entity: BaseEntityConfig
    knx: KnxT

def _to_entity_data(data: dict[str, Any]) -> KnxEntityData[Any]: ...

@dataclass(kw_only=True, slots=True)
class BinarySensorKnxConfig:
    ga_sensor: Annotated[GroupAddressConfig, None]
    invert: Annotated[bool, None] = ...
    section_advanced_options: Annotated[None, None, None] = ...
    ignore_internal_state: Annotated[bool, None] = ...
    context_timeout: Annotated[float | None, None] = ...
    reset_after: Annotated[float | None, None] = ...
    sync_state: Annotated[SyncStateAllowFalse, None] = ...

BINARY_SENSOR_KNX_SCHEMA: Incomplete

def _button_data_sub_validator(config: dict) -> dict: ...

BUTTON_KNX_SCHEMA: Incomplete
COVER_KNX_SCHEMA: Incomplete

@dataclass(kw_only=True, slots=True)
class DateKnxConfig:
    ga_date: Annotated[GroupAddressConfig, None]
    respond_to_read: Annotated[bool, None] = ...
    sync_state: SyncState = ...

DATE_KNX_SCHEMA: Incomplete

@dataclass(kw_only=True, slots=True)
class DatetimeKnxConfig:
    ga_datetime: Annotated[GroupAddressConfig, None]
    respond_to_read: Annotated[bool, None] = ...
    sync_state: SyncState = ...

DATETIME_KNX_SCHEMA: Incomplete
FAN_KNX_SCHEMA: Incomplete

class LightColorMode(StrEnum):
    RGB = '232.600'
    RGBW = '251.600'
    XYY = '242.600'

_hs_color_inclusion_msg: str
LIGHT_KNX_SCHEMA: Incomplete

@dataclass(kw_only=True, slots=True)
class NotifyKnxConfig:
    ga_send: Annotated[GroupAddressConfig, None]

NOTIFY_KNX_SCHEMA: Incomplete

@dataclass(kw_only=True, slots=True)
class NumberKnxConfig:
    ga_sensor: Annotated[GroupAddressConfig, None]
    respond_to_read: Annotated[bool, None] = ...
    section_advanced_options: Annotated[None, None, None] = ...
    mode: Annotated[str, None, None] = ...
    min: Annotated[float | None, None] = ...
    max: Annotated[float | None, None] = ...
    step: Annotated[float | None, None] = ...
    unit_of_measurement: Annotated[str | None, None] = ...
    device_class: Annotated[str | None, None] = ...
    sync_state: SyncState = ...

def _number_limit_sub_validator(config: NumberKnxConfig) -> NumberKnxConfig: ...

NUMBER_KNX_SCHEMA: Incomplete

@dataclass(kw_only=True, slots=True)
class SceneKnxConfig:
    ga_scene: Annotated[GroupAddressConfig, None]
    scene_number: Annotated[int, None, None]

SCENE_KNX_SCHEMA: Incomplete

def _select_options_sub_validator(config: dict) -> dict: ...

SELECT_KNX_SCHEMA: Incomplete

@dataclass(kw_only=True, slots=True)
class SwitchKnxConfig:
    ga_switch: Annotated[GroupAddressConfig, None]
    invert: Annotated[bool, None] = ...
    respond_to_read: Annotated[bool, None] = ...
    sync_state: SyncState = ...

SWITCH_KNX_SCHEMA: Incomplete

@dataclass(kw_only=True, slots=True)
class TextKnxConfig:
    ga_text: Annotated[GroupAddressConfig, None]
    mode: Annotated[str, None, None] = ...
    respond_to_read: Annotated[bool, None] = ...
    sync_state: SyncState = ...

TEXT_KNX_SCHEMA: Incomplete

@dataclass(kw_only=True, slots=True)
class TimeKnxConfig:
    ga_time: Annotated[GroupAddressConfig, None]
    respond_to_read: Annotated[bool, None] = ...
    sync_state: SyncState = ...

TIME_KNX_SCHEMA: Incomplete

class ConfSetpointShiftMode(StrEnum):
    COUNT = '6.010'
    FLOAT = '9.002'

class ConfClimateFanSpeedMode(StrEnum):
    PERCENTAGE = '5.001'
    STEPS = '5.010'

CLIMATE_KNX_SCHEMA: Incomplete

@dataclass(kw_only=True, slots=True)
class SensorKnxConfig:
    ga_sensor: Annotated[GroupAddressConfig, None]
    section_advanced_options: Annotated[None, None, None] = ...
    unit_of_measurement: Annotated[str | None, None] = ...
    device_class: Annotated[str | None, None] = ...
    state_class: Annotated[str | None, None] = ...
    always_callback: Annotated[bool, None] = ...
    sync_state: Annotated[SyncStateAllowFalse, None] = ...

def _sensor_attribute_sub_validator(config: SensorKnxConfig) -> SensorKnxConfig: ...

SENSOR_KNX_SCHEMA: Incomplete
WEATHER_KNX_SCHEMA: Incomplete
KNX_SCHEMA_FOR_PLATFORM: Incomplete
ENTITY_STORE_DATA_SCHEMA: Incomplete
CREATE_ENTITY_BASE_SCHEMA: VolDictType
UPDATE_ENTITY_BASE_SCHEMA: Incomplete
