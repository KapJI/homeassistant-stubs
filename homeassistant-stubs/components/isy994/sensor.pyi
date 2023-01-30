from .const import DOMAIN as DOMAIN, UOM_DOUBLE_TEMP as UOM_DOUBLE_TEMP, UOM_FRIENDLY_NAME as UOM_FRIENDLY_NAME, UOM_INDEX as UOM_INDEX, UOM_ON_OFF as UOM_ON_OFF, UOM_TO_STATES as UOM_TO_STATES, _LOGGER as _LOGGER
from .entity import ISYEntity as ISYEntity, ISYNodeEntity as ISYNodeEntity
from .helpers import convert_isy_value_to_hass as convert_isy_value_to_hass
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pyisy.helpers import EventListener as EventListener, NodeProperty
from pyisy.nodes import Node as Node, NodeChangedEvent as NodeChangedEvent
from pyisy.variables import Variable as Variable
from typing import Any

AUX_DISABLED_BY_DEFAULT_MATCH: Incomplete
AUX_DISABLED_BY_DEFAULT_EXACT: Incomplete
ISY_CONTROL_TO_DEVICE_CLASS: Incomplete
ISY_CONTROL_TO_STATE_CLASS: Incomplete
ISY_CONTROL_TO_ENTITY_CATEGORY: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ISYSensorEntity(ISYNodeEntity, SensorEntity):
    @property
    def target(self) -> Union[Node, NodeProperty, None]: ...
    @property
    def target_value(self) -> Any: ...
    @property
    def raw_unit_of_measurement(self) -> Union[dict, str, None]: ...
    @property
    def native_value(self) -> Union[float, int, str, None]: ...
    @property
    def native_unit_of_measurement(self) -> Union[str, None]: ...

class ISYAuxSensorEntity(ISYSensorEntity):
    _control: Incomplete
    _attr_entity_registry_enabled_default: Incomplete
    _attr_entity_category: Incomplete
    _attr_device_class: Incomplete
    _attr_state_class: Incomplete
    _attr_unique_id: Incomplete
    _change_handler: Incomplete
    _availability_handler: Incomplete
    _attr_name: Incomplete
    def __init__(self, node: Node, control: str, enabled_default: bool, unique_id: str, device_info: Union[DeviceInfo, None] = ...) -> None: ...
    @property
    def target(self) -> Union[Node, NodeProperty, None]: ...
    @property
    def target_value(self) -> Any: ...
    async def async_added_to_hass(self) -> None: ...
    def async_on_update(self, event: Union[NodeProperty, NodeChangedEvent]) -> None: ...
    @property
    def available(self) -> bool: ...

class ISYSensorVariableEntity(ISYEntity, SensorEntity):
    _attr_entity_registry_enabled_default: bool
    _name: Incomplete
    def __init__(self, variable_node: Variable) -> None: ...
    @property
    def native_value(self) -> Union[float, int, None]: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
    @property
    def icon(self) -> str: ...
