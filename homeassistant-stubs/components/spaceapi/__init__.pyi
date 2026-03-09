from _typeshed import Incomplete
from aiohttp import web as web
from homeassistant import core as ha
from homeassistant.components.http import HomeAssistantView as HomeAssistantView, KEY_HASS as KEY_HASS
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, ATTR_ICON as ATTR_ICON, ATTR_LOCATION as ATTR_LOCATION, ATTR_NAME as ATTR_NAME, ATTR_STATE as ATTR_STATE, ATTR_UNIT_OF_MEASUREMENT as ATTR_UNIT_OF_MEASUREMENT, CONF_ADDRESS as CONF_ADDRESS, CONF_EMAIL as CONF_EMAIL, CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_LOCATION as CONF_LOCATION, CONF_SENSORS as CONF_SENSORS, CONF_STATE as CONF_STATE, CONF_URL as CONF_URL
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

ATTR_ADDRESS: str
ATTR_SPACEFED: str
ATTR_CAM: str
ATTR_STREAM: str
ATTR_FEEDS: str
ATTR_CACHE: str
ATTR_PROJECTS: str
ATTR_RADIO_SHOW: str
ATTR_LAT: str
ATTR_LON: str
ATTR_API: str
ATTR_CLOSED: str
ATTR_CONTACT: str
ATTR_ISSUE_REPORT_CHANNELS: str
ATTR_LASTCHANGE: str
ATTR_LOGO: str
ATTR_OPEN: str
ATTR_SENSORS: str
ATTR_SPACE: str
ATTR_UNIT: str
ATTR_URL: str
ATTR_VALUE: str
ATTR_SENSOR_LOCATION: str
CONF_CONTACT: str
CONF_HUMIDITY: str
CONF_ICON_CLOSED: str
CONF_ICON_OPEN: str
CONF_ICONS: str
CONF_IRC: str
CONF_ISSUE_REPORT_CHANNELS: str
CONF_SPACEFED: str
CONF_SPACENET: str
CONF_SPACESAML: str
CONF_SPACEPHONE: str
CONF_CAM: str
CONF_STREAM: str
CONF_M4: str
CONF_MJPEG: str
CONF_USTREAM: str
CONF_FEEDS: str
CONF_FEED_BLOG: str
CONF_FEED_WIKI: str
CONF_FEED_CALENDAR: str
CONF_FEED_FLICKER: str
CONF_FEED_TYPE: str
CONF_FEED_URL: str
CONF_CACHE: str
CONF_CACHE_SCHEDULE: str
CONF_PROJECTS: str
CONF_RADIO_SHOW: str
CONF_RADIO_SHOW_NAME: str
CONF_RADIO_SHOW_URL: str
CONF_RADIO_SHOW_TYPE: str
CONF_RADIO_SHOW_START: str
CONF_RADIO_SHOW_END: str
CONF_LOGO: str
CONF_PHONE: str
CONF_SIP: str
CONF_KEYMASTERS: str
CONF_KEYMASTER_NAME: str
CONF_KEYMASTER_IRC_NICK: str
CONF_KEYMASTER_PHONE: str
CONF_KEYMASTER_EMAIL: str
CONF_KEYMASTER_TWITTER: str
CONF_TWITTER: str
CONF_FACEBOOK: str
CONF_IDENTICA: str
CONF_FOURSQUARE: str
CONF_ML: str
CONF_JABBER: str
CONF_ISSUE_MAIL: str
CONF_SPACE: str
CONF_TEMPERATURE: str
DATA_SPACEAPI: str
DOMAIN: str
ISSUE_REPORT_CHANNELS: Incomplete
SENSOR_TYPES: Incomplete
SPACEAPI_VERSION: str
URL_API_SPACEAPI: str
LOCATION_SCHEMA: Incomplete
SPACEFED_SCHEMA: Incomplete
STREAM_SCHEMA: Incomplete
FEED_SCHEMA: Incomplete
FEEDS_SCHEMA: Incomplete
CACHE_SCHEMA: Incomplete
RADIO_SHOW_SCHEMA: Incomplete
KEYMASTER_SCHEMA: Incomplete
CONTACT_SCHEMA: Incomplete
STATE_SCHEMA: Incomplete
SENSOR_SCHEMA: Incomplete
CONFIG_SCHEMA: Incomplete

def setup(hass: HomeAssistant, config: ConfigType) -> bool: ...

class APISpaceApiView(HomeAssistantView):
    url = URL_API_SPACEAPI
    name: str
    @staticmethod
    def get_sensor_data(hass: HomeAssistant, spaceapi: dict[str, Any], entity_id: str) -> dict[str, str | float | dict[str, str]] | None: ...
    @ha.callback
    def get(self, request: web.Request) -> web.Response: ...
