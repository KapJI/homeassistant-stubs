from .const import ColorTempModes as ColorTempModes, KNX_ADDRESS as KNX_ADDRESS, SupportedPlatforms as SupportedPlatforms
from .schema import BinarySensorSchema as BinarySensorSchema, ClimateSchema as ClimateSchema, CoverSchema as CoverSchema, FanSchema as FanSchema, LightSchema as LightSchema, SceneSchema as SceneSchema, SensorSchema as SensorSchema, SwitchSchema as SwitchSchema, WeatherSchema as WeatherSchema
from homeassistant.const import CONF_DEVICE_CLASS as CONF_DEVICE_CLASS, CONF_NAME as CONF_NAME, CONF_TYPE as CONF_TYPE
from homeassistant.helpers.typing import ConfigType as ConfigType
from xknx import XKNX as XKNX
from xknx.devices import Device as XknxDevice

def create_knx_device(platform: SupportedPlatforms, knx_module: XKNX, config: ConfigType) -> XknxDevice: ...
