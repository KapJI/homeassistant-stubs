from .const import DOMAIN as DOMAIN
from .knx_entity import KnxEntity as KnxEntity
from .schema import WeatherSchema as WeatherSchema
from homeassistant.components.weather import WeatherEntity as WeatherEntity
from homeassistant.const import CONF_NAME as CONF_NAME, TEMP_CELSIUS as TEMP_CELSIUS
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any
from xknx import XKNX as XKNX
from xknx.devices import Weather as XknxWeather

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: Union[DiscoveryInfoType, None] = ...) -> None: ...
def _create_weather(xknx: XKNX, config: ConfigType) -> XknxWeather: ...

class KNXWeather(KnxEntity, WeatherEntity):
    _device: XknxWeather
    _attr_temperature_unit: Any
    _attr_unique_id: Any
    def __init__(self, xknx: XKNX, config: ConfigType) -> None: ...
    @property
    def temperature(self) -> Union[float, None]: ...
    @property
    def pressure(self) -> Union[float, None]: ...
    @property
    def condition(self) -> str: ...
    @property
    def humidity(self) -> Union[float, None]: ...
    @property
    def wind_bearing(self) -> Union[int, None]: ...
    @property
    def wind_speed(self) -> Union[float, None]: ...
