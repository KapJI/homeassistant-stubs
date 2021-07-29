from .const import ATTR_LAST_DATA as ATTR_LAST_DATA, ATTR_MONITORED_CONDITIONS as ATTR_MONITORED_CONDITIONS, CONF_APP_KEY as CONF_APP_KEY, DATA_CLIENT as DATA_CLIENT, DOMAIN as DOMAIN, LOGGER as LOGGER
from aioambient import Client
from homeassistant.components.binary_sensor import DEVICE_CLASS_CONNECTIVITY as DEVICE_CLASS_CONNECTIVITY
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_LOCATION as ATTR_LOCATION, ATTR_NAME as ATTR_NAME, CONCENTRATION_MICROGRAMS_PER_CUBIC_METER as CONCENTRATION_MICROGRAMS_PER_CUBIC_METER, CONCENTRATION_PARTS_PER_MILLION as CONCENTRATION_PARTS_PER_MILLION, CONF_API_KEY as CONF_API_KEY, DEGREE as DEGREE, DEVICE_CLASS_BATTERY as DEVICE_CLASS_BATTERY, DEVICE_CLASS_CO2 as DEVICE_CLASS_CO2, DEVICE_CLASS_HUMIDITY as DEVICE_CLASS_HUMIDITY, DEVICE_CLASS_ILLUMINANCE as DEVICE_CLASS_ILLUMINANCE, DEVICE_CLASS_PRESSURE as DEVICE_CLASS_PRESSURE, DEVICE_CLASS_TEMPERATURE as DEVICE_CLASS_TEMPERATURE, DEVICE_CLASS_TIMESTAMP as DEVICE_CLASS_TIMESTAMP, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, IRRADIATION_WATTS_PER_SQUARE_METER as IRRADIATION_WATTS_PER_SQUARE_METER, LIGHT_LUX as LIGHT_LUX, PERCENTAGE as PERCENTAGE, PRECIPITATION_INCHES as PRECIPITATION_INCHES, PRECIPITATION_INCHES_PER_HOUR as PRECIPITATION_INCHES_PER_HOUR, PRESSURE_INHG as PRESSURE_INHG, SPEED_MILES_PER_HOUR as SPEED_MILES_PER_HOUR, TEMP_FAHRENHEIT as TEMP_FAHRENHEIT
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import aiohttp_client as aiohttp_client
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect, async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.event import async_call_later as async_call_later
from typing import Any

PLATFORMS: Any
DATA_CONFIG: str
DEFAULT_SOCKET_MIN_RETRY: int
TYPE_24HOURRAININ: str
TYPE_BAROMABSIN: str
TYPE_BAROMRELIN: str
TYPE_BATT1: str
TYPE_BATT10: str
TYPE_BATT2: str
TYPE_BATT3: str
TYPE_BATT4: str
TYPE_BATT5: str
TYPE_BATT6: str
TYPE_BATT7: str
TYPE_BATT8: str
TYPE_BATT9: str
TYPE_BATT_CO2: str
TYPE_BATTOUT: str
TYPE_CO2: str
TYPE_DAILYRAININ: str
TYPE_DEWPOINT: str
TYPE_EVENTRAININ: str
TYPE_FEELSLIKE: str
TYPE_HOURLYRAININ: str
TYPE_HUMIDITY: str
TYPE_HUMIDITY1: str
TYPE_HUMIDITY10: str
TYPE_HUMIDITY2: str
TYPE_HUMIDITY3: str
TYPE_HUMIDITY4: str
TYPE_HUMIDITY5: str
TYPE_HUMIDITY6: str
TYPE_HUMIDITY7: str
TYPE_HUMIDITY8: str
TYPE_HUMIDITY9: str
TYPE_HUMIDITYIN: str
TYPE_LASTRAIN: str
TYPE_MAXDAILYGUST: str
TYPE_MONTHLYRAININ: str
TYPE_PM25: str
TYPE_PM25_24H: str
TYPE_PM25_BATT: str
TYPE_PM25_IN: str
TYPE_PM25_IN_24H: str
TYPE_PM25IN_BATT: str
TYPE_RELAY1: str
TYPE_RELAY10: str
TYPE_RELAY2: str
TYPE_RELAY3: str
TYPE_RELAY4: str
TYPE_RELAY5: str
TYPE_RELAY6: str
TYPE_RELAY7: str
TYPE_RELAY8: str
TYPE_RELAY9: str
TYPE_SOILHUM1: str
TYPE_SOILHUM10: str
TYPE_SOILHUM2: str
TYPE_SOILHUM3: str
TYPE_SOILHUM4: str
TYPE_SOILHUM5: str
TYPE_SOILHUM6: str
TYPE_SOILHUM7: str
TYPE_SOILHUM8: str
TYPE_SOILHUM9: str
TYPE_SOILTEMP1F: str
TYPE_SOILTEMP10F: str
TYPE_SOILTEMP2F: str
TYPE_SOILTEMP3F: str
TYPE_SOILTEMP4F: str
TYPE_SOILTEMP5F: str
TYPE_SOILTEMP6F: str
TYPE_SOILTEMP7F: str
TYPE_SOILTEMP8F: str
TYPE_SOILTEMP9F: str
TYPE_SOLARRADIATION: str
TYPE_SOLARRADIATION_LX: str
TYPE_TEMP10F: str
TYPE_TEMP1F: str
TYPE_TEMP2F: str
TYPE_TEMP3F: str
TYPE_TEMP4F: str
TYPE_TEMP5F: str
TYPE_TEMP6F: str
TYPE_TEMP7F: str
TYPE_TEMP8F: str
TYPE_TEMP9F: str
TYPE_TEMPF: str
TYPE_TEMPINF: str
TYPE_TOTALRAININ: str
TYPE_UV: str
TYPE_WEEKLYRAININ: str
TYPE_WINDDIR: str
TYPE_WINDDIR_AVG10M: str
TYPE_WINDDIR_AVG2M: str
TYPE_WINDGUSTDIR: str
TYPE_WINDGUSTMPH: str
TYPE_WINDSPDMPH_AVG10M: str
TYPE_WINDSPDMPH_AVG2M: str
TYPE_WINDSPEEDMPH: str
TYPE_YEARLYRAININ: str
SENSOR_TYPES: Any
CONFIG_SCHEMA: Any

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool: ...

class AmbientStation:
    _config_entry: Any
    _entry_setup_complete: bool
    _hass: Any
    _ws_reconnect_delay: Any
    client: Any
    stations: Any
    def __init__(self, hass: HomeAssistant, config_entry: ConfigEntry, client: Client) -> None: ...
    async def _attempt_connect(self) -> None: ...
    async def ws_connect(self) -> None: ...
    async def ws_disconnect(self) -> None: ...

class AmbientWeatherEntity(Entity):
    _ambient: Any
    _attr_device_class: Any
    _attr_device_info: Any
    _attr_name: Any
    _attr_should_poll: bool
    _attr_unique_id: Any
    _mac_address: Any
    _sensor_type: Any
    def __init__(self, ambient: AmbientStation, mac_address: str, station_name: str, sensor_type: str, sensor_name: str, device_class: Union[str, None]) -> None: ...
    _attr_available: Any
    async def async_added_to_hass(self) -> None: ...
    def update_from_latest_data(self) -> None: ...
