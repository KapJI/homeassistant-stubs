from . import async_get_config_and_coordinator as async_get_config_and_coordinator, create_rest_data_from_config as create_rest_data_from_config
from .const import CONF_JSON_ATTRS as CONF_JSON_ATTRS, CONF_JSON_ATTRS_PATH as CONF_JSON_ATTRS_PATH, DEFAULT_SENSOR_NAME as DEFAULT_SENSOR_NAME
from .data import RestData as RestData
from .entity import RestEntity as RestEntity
from .schema import RESOURCE_SCHEMA as RESOURCE_SCHEMA, SENSOR_SCHEMA as SENSOR_SCHEMA
from _typeshed import Incomplete
from homeassistant.components.sensor import PLATFORM_SCHEMA as PLATFORM_SCHEMA, SensorDeviceClass as SensorDeviceClass
from homeassistant.components.sensor.helpers import async_parse_date_datetime as async_parse_date_datetime
from homeassistant.const import CONF_FORCE_UPDATE as CONF_FORCE_UPDATE, CONF_RESOURCE as CONF_RESOURCE, CONF_RESOURCE_TEMPLATE as CONF_RESOURCE_TEMPLATE, CONF_UNIQUE_ID as CONF_UNIQUE_ID, CONF_VALUE_TEMPLATE as CONF_VALUE_TEMPLATE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import PlatformNotReady as PlatformNotReady
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.template_entity import TemplateSensor as TemplateSensor
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from homeassistant.util.json import json_loads as json_loads

_LOGGER: Incomplete

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = ...) -> None: ...

class RestSensor(RestEntity, TemplateSensor):
    _value_template: Incomplete
    _json_attrs: Incomplete
    _json_attrs_path: Incomplete
    def __init__(self, hass: HomeAssistant, coordinator: DataUpdateCoordinator[None] | None, rest: RestData, config: ConfigType, unique_id: str | None) -> None: ...
    _attr_extra_state_attributes: Incomplete
    _attr_native_value: Incomplete
    def _update_from_rest_data(self) -> None: ...
