from .const import DEFAULT_PROGRAM_STRING as DEFAULT_PROGRAM_STRING, DOMAIN as DOMAIN, FILTER_INSTEON_TYPE as FILTER_INSTEON_TYPE, FILTER_NODE_DEF_ID as FILTER_NODE_DEF_ID, FILTER_STATES as FILTER_STATES, FILTER_UOM as FILTER_UOM, FILTER_ZWAVE_CAT as FILTER_ZWAVE_CAT, ISY_GROUP_PLATFORM as ISY_GROUP_PLATFORM, KEY_ACTIONS as KEY_ACTIONS, KEY_STATUS as KEY_STATUS, NODE_AUX_FILTERS as NODE_AUX_FILTERS, NODE_FILTERS as NODE_FILTERS, NODE_PLATFORMS as NODE_PLATFORMS, PROGRAM_PLATFORMS as PROGRAM_PLATFORMS, SUBNODE_CLIMATE_COOL as SUBNODE_CLIMATE_COOL, SUBNODE_CLIMATE_HEAT as SUBNODE_CLIMATE_HEAT, SUBNODE_EZIO2X4_SENSORS as SUBNODE_EZIO2X4_SENSORS, SUBNODE_FANLINC_LIGHT as SUBNODE_FANLINC_LIGHT, SUBNODE_IOLINC_RELAY as SUBNODE_IOLINC_RELAY, TYPE_CATEGORY_SENSOR_ACTUATORS as TYPE_CATEGORY_SENSOR_ACTUATORS, TYPE_EZIO2X4 as TYPE_EZIO2X4, UOM_DOUBLE_TEMP as UOM_DOUBLE_TEMP, UOM_ISYV4_DEGREES as UOM_ISYV4_DEGREES, _LOGGER as _LOGGER
from .models import IsyData as IsyData
from _typeshed import Incomplete
from homeassistant.const import ATTR_MANUFACTURER as ATTR_MANUFACTURER, ATTR_MODEL as ATTR_MODEL, Platform as Platform
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from pyisy.nodes import Group as Group, Node as Node, Nodes as Nodes
from pyisy.programs import Programs as Programs

BINARY_SENSOR_UOMS: Incomplete
BINARY_SENSOR_ISY_STATES: Incomplete
ROOT_AUX_CONTROLS: Incomplete
SKIP_AUX_PROPS: Incomplete

def _check_for_node_def(isy_data: IsyData, node: Group | Node, single_platform: Platform | None = None) -> bool: ...
def _check_for_insteon_type(isy_data: IsyData, node: Group | Node, single_platform: Platform | None = None) -> bool: ...
def _check_for_zwave_cat(isy_data: IsyData, node: Group | Node, single_platform: Platform | None = None) -> bool: ...
def _check_for_uom_id(isy_data: IsyData, node: Group | Node, single_platform: Platform | None = None, uom_list: list[str] | None = None) -> bool: ...
def _check_for_states_in_uom(isy_data: IsyData, node: Group | Node, single_platform: Platform | None = None, states_list: list[str] | None = None) -> bool: ...
def _is_sensor_a_binary_sensor(isy_data: IsyData, node: Group | Node) -> bool: ...
def _add_backlight_if_supported(isy_data: IsyData, node: Node) -> None: ...
def _generate_device_info(node: Node) -> DeviceInfo: ...
def _categorize_nodes(isy_data: IsyData, nodes: Nodes, ignore_identifier: str, sensor_identifier: str) -> None: ...
def _categorize_programs(isy_data: IsyData, programs: Programs) -> None: ...
def convert_isy_value_to_hass(value: int | float | None, uom: str | None, precision: int | str, fallback_precision: int | None = None) -> float | int | None: ...
