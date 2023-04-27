from . import async_get_config_and_coordinator as async_get_config_and_coordinator, create_rest_data_from_config as create_rest_data_from_config
from .const import DEFAULT_BINARY_SENSOR_NAME as DEFAULT_BINARY_SENSOR_NAME
from .data import RestData as RestData
from .entity import RestEntity as RestEntity
from .schema import BINARY_SENSOR_SCHEMA as BINARY_SENSOR_SCHEMA, RESOURCE_SCHEMA as RESOURCE_SCHEMA
from _typeshed import Incomplete
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity, PLATFORM_SCHEMA as PLATFORM_SCHEMA
from homeassistant.const import CONF_DEVICE_CLASS as CONF_DEVICE_CLASS, CONF_FORCE_UPDATE as CONF_FORCE_UPDATE, CONF_RESOURCE as CONF_RESOURCE, CONF_RESOURCE_TEMPLATE as CONF_RESOURCE_TEMPLATE, CONF_UNIQUE_ID as CONF_UNIQUE_ID, CONF_VALUE_TEMPLATE as CONF_VALUE_TEMPLATE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import PlatformNotReady as PlatformNotReady
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.template import Template as Template
from homeassistant.helpers.template_entity import TemplateEntity as TemplateEntity
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator

_LOGGER: Incomplete

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = ...) -> None: ...

class RestBinarySensor(RestEntity, TemplateEntity, BinarySensorEntity):
    _previous_data: Incomplete
    _value_template: Incomplete
    _attr_device_class: Incomplete
    def __init__(self, hass: HomeAssistant, coordinator: DataUpdateCoordinator[None] | None, rest: RestData, config: ConfigType, unique_id: str | None) -> None: ...
    _attr_is_on: bool
    def _update_from_rest_data(self) -> None: ...
