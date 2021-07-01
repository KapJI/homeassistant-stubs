from .const import ATTRIBUTION as ATTRIBUTION, ATTR_ACCESS_TOKEN as ATTR_ACCESS_TOKEN, ATTR_LAST_SAVED_AT as ATTR_LAST_SAVED_AT, ATTR_REFRESH_TOKEN as ATTR_REFRESH_TOKEN, BATTERY_LEVELS as BATTERY_LEVELS, CONF_CLOCK_FORMAT as CONF_CLOCK_FORMAT, CONF_MONITORED_RESOURCES as CONF_MONITORED_RESOURCES, DEFAULT_CLOCK_FORMAT as DEFAULT_CLOCK_FORMAT, DEFAULT_CONFIG as DEFAULT_CONFIG, FITBIT_AUTH_CALLBACK_PATH as FITBIT_AUTH_CALLBACK_PATH, FITBIT_AUTH_START as FITBIT_AUTH_START, FITBIT_CONFIG_FILE as FITBIT_CONFIG_FILE, FITBIT_DEFAULT_RESOURCES as FITBIT_DEFAULT_RESOURCES, FITBIT_MEASUREMENTS as FITBIT_MEASUREMENTS, FITBIT_RESOURCES_LIST as FITBIT_RESOURCES_LIST
from aiohttp.web import Request as Request
from fitbit import Fitbit
from fitbit.api import FitbitOauth2Client
from homeassistant.components.http import HomeAssistantView as HomeAssistantView
from homeassistant.components.sensor import SensorEntity as SensorEntity
from homeassistant.const import ATTR_ATTRIBUTION as ATTR_ATTRIBUTION, CONF_CLIENT_ID as CONF_CLIENT_ID, CONF_CLIENT_SECRET as CONF_CLIENT_SECRET, CONF_UNIT_SYSTEM as CONF_UNIT_SYSTEM
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.icon import icon_for_battery_level as icon_for_battery_level
from homeassistant.helpers.network import get_url as get_url
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from homeassistant.util.json import load_json as load_json, save_json as save_json
from typing import Any, Final

_LOGGER: Final[Any]
_CONFIGURING: dict[str, str]
SCAN_INTERVAL: Final[Any]
PLATFORM_SCHEMA: Final[Any]

def request_app_setup(hass: HomeAssistant, config: ConfigType, add_entities: AddEntitiesCallback, config_path: str, discovery_info: Union[DiscoveryInfoType, None] = ...) -> None: ...
def request_oauth_completion(hass: HomeAssistant) -> None: ...
def setup_platform(hass: HomeAssistant, config: ConfigType, add_entities: AddEntitiesCallback, discovery_info: Union[DiscoveryInfoType, None] = ...) -> None: ...

class FitbitAuthCallbackView(HomeAssistantView):
    requires_auth: bool
    url: Any
    name: str
    config: Any
    add_entities: Any
    oauth: Any
    def __init__(self, config: ConfigType, add_entities: AddEntitiesCallback, oauth: FitbitOauth2Client) -> None: ...
    async def get(self, request: Request) -> str: ...

class FitbitSensor(SensorEntity):
    client: Any
    config_path: Any
    resource_type: Any
    is_metric: Any
    clock_format: Any
    extra: Any
    _name: Any
    _unit_of_measurement: Any
    _state: Any
    def __init__(self, client: Fitbit, config_path: str, resource_type: str, is_metric: bool, clock_format: str, extra: Union[dict[str, str], None] = ...) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def state(self) -> Union[str, None]: ...
    @property
    def unit_of_measurement(self) -> Union[str, None]: ...
    @property
    def icon(self) -> str: ...
    @property
    def extra_state_attributes(self) -> dict[str, Union[str, None]]: ...
    def update(self) -> None: ...
