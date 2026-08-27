from .const import CONF_SYNC_STATE as CONF_SYNC_STATE, DOMAIN as DOMAIN, KNX_MODULE_KEY as KNX_MODULE_KEY
from .entity import KnxUiEntity as KnxUiEntity, KnxUiEntityPlatformController as KnxUiEntityPlatformController, KnxYamlEntity as KnxYamlEntity, build_yaml_unique_id as build_yaml_unique_id
from .knx_module import KNXModule as KNXModule
from .schema import WeatherSchema as WeatherSchema
from .storage.const import CONF_ENTITY as CONF_ENTITY, CONF_GA_AIR_PRESSURE as CONF_GA_AIR_PRESSURE, CONF_GA_BRIGHTNESS_EAST as CONF_GA_BRIGHTNESS_EAST, CONF_GA_BRIGHTNESS_NORTH as CONF_GA_BRIGHTNESS_NORTH, CONF_GA_BRIGHTNESS_SOUTH as CONF_GA_BRIGHTNESS_SOUTH, CONF_GA_BRIGHTNESS_WEST as CONF_GA_BRIGHTNESS_WEST, CONF_GA_DAY_NIGHT as CONF_GA_DAY_NIGHT, CONF_GA_FROST_ALARM as CONF_GA_FROST_ALARM, CONF_GA_HUMIDITY as CONF_GA_HUMIDITY, CONF_GA_RAIN_ALARM as CONF_GA_RAIN_ALARM, CONF_GA_TEMPERATURE as CONF_GA_TEMPERATURE, CONF_GA_WIND_ALARM as CONF_GA_WIND_ALARM, CONF_GA_WIND_BEARING as CONF_GA_WIND_BEARING, CONF_GA_WIND_SPEED as CONF_GA_WIND_SPEED, CONF_INVERT_DAY_NIGHT as CONF_INVERT_DAY_NIGHT
from .storage.util import ConfigExtractor as ConfigExtractor
from _typeshed import Incomplete
from homeassistant import config_entries as config_entries
from homeassistant.components.weather import WeatherEntity as WeatherEntity
from homeassistant.const import CONF_NAME as CONF_NAME, Platform as Platform, UnitOfPressure as UnitOfPressure, UnitOfSpeed as UnitOfSpeed, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback, async_get_current_platform as async_get_current_platform
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import override
from xknx.devices import Weather as XknxWeather

async def async_setup_entry(hass: HomeAssistant, config_entry: config_entries.ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class _KnxWeather(WeatherEntity):
    _device: XknxWeather
    _attr_native_pressure_unit: Incomplete
    _attr_native_temperature_unit: Incomplete
    _attr_native_wind_speed_unit: Incomplete
    @property
    @override
    def native_temperature(self) -> float | None: ...
    @property
    @override
    def native_pressure(self) -> float | None: ...
    @property
    @override
    def condition(self) -> str: ...
    @property
    @override
    def humidity(self) -> float | None: ...
    @property
    @override
    def wind_bearing(self) -> int | None: ...
    @property
    @override
    def native_wind_speed(self) -> float | None: ...

class KnxYamlWeather(_KnxWeather, KnxYamlEntity):
    _device: XknxWeather
    def __init__(self, knx_module: KNXModule, config: ConfigType) -> None: ...

class KnxUiWeather(_KnxWeather, KnxUiEntity):
    _device: XknxWeather
    def __init__(self, knx_module: KNXModule, unique_id: str, config: ConfigType) -> None: ...
