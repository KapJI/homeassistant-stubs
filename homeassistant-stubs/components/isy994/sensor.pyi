from .const import ISY994_NODES as ISY994_NODES, ISY994_VARIABLES as ISY994_VARIABLES, SENSOR_AUX as SENSOR_AUX, UOM_DOUBLE_TEMP as UOM_DOUBLE_TEMP, UOM_FRIENDLY_NAME as UOM_FRIENDLY_NAME, UOM_INDEX as UOM_INDEX, UOM_ON_OFF as UOM_ON_OFF, UOM_TO_STATES as UOM_TO_STATES, _LOGGER as _LOGGER
from .entity import ISYEntity as ISYEntity, ISYNodeEntity as ISYNodeEntity
from .helpers import convert_isy_value_to_hass as convert_isy_value_to_hass, migrate_old_unique_ids as migrate_old_unique_ids
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import TEMP_CELSIUS as TEMP_CELSIUS, TEMP_FAHRENHEIT as TEMP_FAHRENHEIT
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pyisy.helpers import NodeProperty
from pyisy.nodes import Node as Node
from typing import Any

AUX_DISABLED_BY_DEFAULT_MATCH: Incomplete
AUX_DISABLED_BY_DEFAULT_EXACT: Incomplete
SKIP_AUX_PROPERTIES: Incomplete
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
    def __init__(self, node: Node, control: str, enabled_default: bool) -> None: ...
    @property
    def target(self) -> Union[Node, NodeProperty, None]: ...
    @property
    def target_value(self) -> Any: ...
    @property
    def unique_id(self) -> Union[str, None]: ...
    @property
    def name(self) -> str: ...

class ISYSensorVariableEntity(ISYEntity, SensorEntity):
    _name: Incomplete
    def __init__(self, vname: str, vobj: object) -> None: ...
    @property
    def native_value(self) -> Union[float, int, None]: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
    @property
    def icon(self) -> str: ...
