from .const import CONF_JSON_ATTRS as CONF_JSON_ATTRS, CONF_JSON_ATTRS_PATH as CONF_JSON_ATTRS_PATH, DEFAULT_SENSOR_NAME as DEFAULT_SENSOR_NAME
from .coordinator import RestCoordinator as RestCoordinator
from .data import RestData as RestData
from .entity import RestEntity as RestEntity, async_get_config_rest_data_and_coordinator as async_get_config_rest_data_and_coordinator, async_get_trigger_entity_config as async_get_trigger_entity_config
from .schema import RESOURCE_SCHEMA as RESOURCE_SCHEMA, SENSOR_SCHEMA as SENSOR_SCHEMA
from .util import parse_json_attributes as parse_json_attributes
from _typeshed import Incomplete
from homeassistant.const import CONF_FORCE_UPDATE as CONF_FORCE_UPDATE, CONF_RESOURCE as CONF_RESOURCE, CONF_RESOURCE_TEMPLATE as CONF_RESOURCE_TEMPLATE, CONF_VALUE_TEMPLATE as CONF_VALUE_TEMPLATE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.trigger_template_entity import ManualTriggerSensorEntity as ManualTriggerSensorEntity, ValueTemplate as ValueTemplate
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any, override

_LOGGER: Incomplete
PLATFORM_SCHEMA: Incomplete

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...

class RestSensor(ManualTriggerSensorEntity, RestEntity):
    _value_template: ValueTemplate | None
    _json_attrs: Incomplete
    _json_attrs_path: Incomplete
    _attr_extra_state_attributes: Incomplete
    def __init__(self, hass: HomeAssistant, coordinator: RestCoordinator | None, rest: RestData, config: ConfigType, trigger_entity_config: ConfigType) -> None: ...
    @property
    @override
    def available(self) -> bool: ...
    @property
    @override
    def extra_state_attributes(self) -> dict[str, Any]: ...
    @override
    def _update_from_rest_data(self) -> None: ...
