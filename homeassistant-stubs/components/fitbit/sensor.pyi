from .api import FitbitApi as FitbitApi
from .const import ATTRIBUTION as ATTRIBUTION, ATTR_ACCESS_TOKEN as ATTR_ACCESS_TOKEN, ATTR_LAST_SAVED_AT as ATTR_LAST_SAVED_AT, ATTR_REFRESH_TOKEN as ATTR_REFRESH_TOKEN, BATTERY_LEVELS as BATTERY_LEVELS, CONF_CLOCK_FORMAT as CONF_CLOCK_FORMAT, CONF_MONITORED_RESOURCES as CONF_MONITORED_RESOURCES, DEFAULT_CLOCK_FORMAT as DEFAULT_CLOCK_FORMAT, DEFAULT_CONFIG as DEFAULT_CONFIG, FITBIT_AUTH_CALLBACK_PATH as FITBIT_AUTH_CALLBACK_PATH, FITBIT_AUTH_START as FITBIT_AUTH_START, FITBIT_CONFIG_FILE as FITBIT_CONFIG_FILE, FITBIT_DEFAULT_RESOURCES as FITBIT_DEFAULT_RESOURCES, FitbitUnitSystem as FitbitUnitSystem
from .model import FitbitDevice as FitbitDevice
from _typeshed import Incomplete
from aiohttp.web import Request as Request
from collections.abc import Callable as Callable
from fitbit.api import FitbitOauth2Client
from homeassistant.components import configurator as configurator
from homeassistant.components.http import HomeAssistantView as HomeAssistantView
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import CONF_CLIENT_ID as CONF_CLIENT_ID, CONF_CLIENT_SECRET as CONF_CLIENT_SECRET, CONF_UNIT_SYSTEM as CONF_UNIT_SYSTEM, PERCENTAGE as PERCENTAGE, UnitOfLength as UnitOfLength, UnitOfMass as UnitOfMass, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.icon import icon_for_battery_level as icon_for_battery_level
from homeassistant.helpers.json import save_json as save_json
from homeassistant.helpers.network import NoURLAvailableError as NoURLAvailableError, get_url as get_url
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from homeassistant.util.json import load_json_object as load_json_object
from typing import Any, Final

_LOGGER: Final[Incomplete]
_CONFIGURING: dict[str, str]
SCAN_INTERVAL: Final[Incomplete]

def _default_value_fn(result: dict[str, Any]) -> str: ...
def _distance_value_fn(result: dict[str, Any]) -> int | str: ...
def _body_value_fn(result: dict[str, Any]) -> int | str: ...
def _clock_format_12h(result: dict[str, Any]) -> str: ...
def _weight_unit(unit_system: FitbitUnitSystem) -> UnitOfMass: ...
def _distance_unit(unit_system: FitbitUnitSystem) -> UnitOfLength: ...
def _elevation_unit(unit_system: FitbitUnitSystem) -> UnitOfLength: ...

class FitbitSensorEntityDescription(SensorEntityDescription):
    unit_type: str | None
    value_fn: Callable[[dict[str, Any]], Any]
    unit_fn: Callable[[FitbitUnitSystem], str | None]
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement, unit_type, value_fn, unit_fn) -> None: ...

FITBIT_RESOURCES_LIST: Final[tuple[FitbitSensorEntityDescription, ...]]
SLEEP_START_TIME: Incomplete
SLEEP_START_TIME_12HR: Incomplete
FITBIT_RESOURCE_BATTERY: Incomplete
FITBIT_RESOURCES_KEYS: Final[list[str]]
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
    api: Incomplete
    config_path: Incomplete
    device: Incomplete
    _attr_unique_id: Incomplete
    _attr_name: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    def __init__(self, api: FitbitApi, user_profile_id: str, config_path: str, description: FitbitSensorEntityDescription, device: FitbitDevice | None = ..., units: str | None = ...) -> None: ...
    @property
    def icon(self) -> str | None: ...
    @property
    def extra_state_attributes(self) -> dict[str, str | None]: ...
    _attr_native_value: Incomplete
    async def async_update(self) -> None: ...
    def _update_token(self) -> None: ...
