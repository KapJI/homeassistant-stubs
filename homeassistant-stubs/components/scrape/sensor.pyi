from .const import CONF_INDEX as CONF_INDEX, CONF_SELECT as CONF_SELECT, DEFAULT_NAME as DEFAULT_NAME, DEFAULT_SCAN_INTERVAL as DEFAULT_SCAN_INTERVAL, DEFAULT_VERIFY_SSL as DEFAULT_VERIFY_SSL, DOMAIN as DOMAIN
from .coordinator import ScrapeCoordinator as ScrapeCoordinator
from _typeshed import Incomplete
from homeassistant.components.rest import RESOURCE_SCHEMA as RESOURCE_SCHEMA, create_rest_data_from_config as create_rest_data_from_config
from homeassistant.components.sensor import CONF_STATE_CLASS as CONF_STATE_CLASS, DEVICE_CLASSES_SCHEMA as DEVICE_CLASSES_SCHEMA, STATE_CLASSES_SCHEMA as STATE_CLASSES_SCHEMA, SensorDeviceClass as SensorDeviceClass
from homeassistant.components.sensor.helpers import async_parse_date_datetime as async_parse_date_datetime
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_ATTRIBUTE as CONF_ATTRIBUTE, CONF_AUTHENTICATION as CONF_AUTHENTICATION, CONF_DEVICE_CLASS as CONF_DEVICE_CLASS, CONF_HEADERS as CONF_HEADERS, CONF_NAME as CONF_NAME, CONF_PASSWORD as CONF_PASSWORD, CONF_RESOURCE as CONF_RESOURCE, CONF_SCAN_INTERVAL as CONF_SCAN_INTERVAL, CONF_UNIQUE_ID as CONF_UNIQUE_ID, CONF_UNIT_OF_MEASUREMENT as CONF_UNIT_OF_MEASUREMENT, CONF_USERNAME as CONF_USERNAME, CONF_VALUE_TEMPLATE as CONF_VALUE_TEMPLATE, CONF_VERIFY_SSL as CONF_VERIFY_SSL, HTTP_BASIC_AUTHENTICATION as HTTP_BASIC_AUTHENTICATION, HTTP_DIGEST_AUTHENTICATION as HTTP_DIGEST_AUTHENTICATION
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import PlatformNotReady as PlatformNotReady
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue
from homeassistant.helpers.template import Template as Template
from homeassistant.helpers.template_entity import TEMPLATE_SENSOR_BASE_SCHEMA as TEMPLATE_SENSOR_BASE_SCHEMA, TemplateSensor as TemplateSensor
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

_LOGGER: Incomplete
PLATFORM_SCHEMA: Incomplete

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: Union[DiscoveryInfoType, None] = ...) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ScrapeSensor(CoordinatorEntity[ScrapeCoordinator], TemplateSensor):
    _select: Incomplete
    _attr: Incomplete
    _index: Incomplete
    _value_template: Incomplete
    def __init__(self, hass: HomeAssistant, coordinator: ScrapeCoordinator, config: ConfigType, name: str, unique_id: Union[str, None], select: str, attr: Union[str, None], index: int, value_template: Union[Template, None]) -> None: ...
    def _extract_value(self) -> Any: ...
    async def async_added_to_hass(self) -> None: ...
    _attr_native_value: Incomplete
    def _async_update_from_rest_data(self) -> None: ...
    def _handle_coordinator_update(self) -> None: ...
