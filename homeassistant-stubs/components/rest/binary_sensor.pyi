from .const import DEFAULT_BINARY_SENSOR_NAME as DEFAULT_BINARY_SENSOR_NAME
from .coordinator import RestCoordinator as RestCoordinator
from .data import RestData as RestData
from .entity import RestEntity as RestEntity, async_get_config_rest_data_and_coordinator as async_get_config_rest_data_and_coordinator, async_get_trigger_entity_config as async_get_trigger_entity_config
from .schema import BINARY_SENSOR_SCHEMA as BINARY_SENSOR_SCHEMA, RESOURCE_SCHEMA as RESOURCE_SCHEMA
from _typeshed import Incomplete
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity
from homeassistant.const import CONF_FORCE_UPDATE as CONF_FORCE_UPDATE, CONF_RESOURCE as CONF_RESOURCE, CONF_RESOURCE_TEMPLATE as CONF_RESOURCE_TEMPLATE, CONF_VALUE_TEMPLATE as CONF_VALUE_TEMPLATE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.trigger_template_entity import ManualTriggerEntity as ManualTriggerEntity, ValueTemplate as ValueTemplate
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import override

_LOGGER: Incomplete
PLATFORM_SCHEMA: Incomplete

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...

class RestBinarySensor(ManualTriggerEntity, RestEntity, BinarySensorEntity):
    _previous_data: Incomplete
    _value_template: ValueTemplate | None
    def __init__(self, hass: HomeAssistant, coordinator: RestCoordinator | None, rest: RestData, config: ConfigType, trigger_entity_config: ConfigType) -> None: ...
    @property
    @override
    def available(self) -> bool: ...
    _attr_is_on: bool
    @override
    def _update_from_rest_data(self) -> None: ...
