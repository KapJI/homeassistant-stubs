from .const import ATTRIBUTION as ATTRIBUTION, ATTR_ACCESS_TOKEN as ATTR_ACCESS_TOKEN, ATTR_LAST_SAVED_AT as ATTR_LAST_SAVED_AT, ATTR_REFRESH_TOKEN as ATTR_REFRESH_TOKEN, BATTERY_LEVELS as BATTERY_LEVELS, CONF_CLOCK_FORMAT as CONF_CLOCK_FORMAT, CONF_MONITORED_RESOURCES as CONF_MONITORED_RESOURCES, DEFAULT_CLOCK_FORMAT as DEFAULT_CLOCK_FORMAT, DEFAULT_CONFIG as DEFAULT_CONFIG, FITBIT_AUTH_CALLBACK_PATH as FITBIT_AUTH_CALLBACK_PATH, FITBIT_AUTH_START as FITBIT_AUTH_START, FITBIT_CONFIG_FILE as FITBIT_CONFIG_FILE, FITBIT_DEFAULT_RESOURCES as FITBIT_DEFAULT_RESOURCES, FITBIT_MEASUREMENTS as FITBIT_MEASUREMENTS, FITBIT_RESOURCES_KEYS as FITBIT_RESOURCES_KEYS, FITBIT_RESOURCES_LIST as FITBIT_RESOURCES_LIST, FITBIT_RESOURCE_BATTERY as FITBIT_RESOURCE_BATTERY, FitbitSensorEntityDescription as FitbitSensorEntityDescription
from _typeshed import Incomplete
from aiohttp.web import Request as Request
from fitbit import Fitbit
from fitbit.api import FitbitOauth2Client
from homeassistant.components import configurator as configurator
from homeassistant.components.http import HomeAssistantView as HomeAssistantView
from homeassistant.components.sensor import SensorEntity as SensorEntity
from homeassistant.const import CONF_CLIENT_ID as CONF_CLIENT_ID, CONF_CLIENT_SECRET as CONF_CLIENT_SECRET, CONF_UNIT_SYSTEM as CONF_UNIT_SYSTEM
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.icon import icon_for_battery_level as icon_for_battery_level
from homeassistant.helpers.json import save_json as save_json
from homeassistant.helpers.network import NoURLAvailableError as NoURLAvailableError, get_url as get_url
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from homeassistant.util.json import load_json_object as load_json_object
from homeassistant.util.unit_system import METRIC_SYSTEM as METRIC_SYSTEM
from typing import Any, Final

_LOGGER: Final[Incomplete]
_CONFIGURING: dict[str, str]
SCAN_INTERVAL: Final[Incomplete]
PLATFORM_SCHEMA: Final[Incomplete]

def request_app_setup(hass: HomeAssistant, config: ConfigType, add_entities: AddEntitiesCallback, config_path: str, discovery_info: DiscoveryInfoType | None = ...) -> None: ...
def request_oauth_completion(hass: HomeAssistant) -> None: ...
def setup_platform(hass: HomeAssistant, config: ConfigType, add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = ...) -> None: ...

class FitbitAuthCallbackView(HomeAssistantView):
    requires_auth: bool
    url = FITBIT_AUTH_CALLBACK_PATH
    name: str
    config: Incomplete
    add_entities: Incomplete
    oauth: Incomplete
    def __init__(self, config: ConfigType, add_entities: AddEntitiesCallback, oauth: FitbitOauth2Client) -> None: ...
    async def get(self, request: Request) -> str: ...

class FitbitSensor(SensorEntity):
    entity_description: FitbitSensorEntityDescription
    _attr_attribution = ATTRIBUTION
    client: Incomplete
    config_path: Incomplete
    is_metric: Incomplete
    clock_format: Incomplete
    extra: Incomplete
    _attr_unique_id: Incomplete
    _attr_name: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    def __init__(self, client: Fitbit, user_profile: dict[str, Any], config_path: str, description: FitbitSensorEntityDescription, is_metric: bool, clock_format: str, extra: dict[str, str] | None = ...) -> None: ...
    @property
    def icon(self) -> str | None: ...
    @property
    def extra_state_attributes(self) -> dict[str, str | None]: ...
    _attr_native_value: Incomplete
    def update(self) -> None: ...
