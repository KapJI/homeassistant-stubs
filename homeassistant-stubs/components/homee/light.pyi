from . import HomeeConfigEntry as HomeeConfigEntry
from .const import LIGHT_PROFILES as LIGHT_PROFILES
from .entity import HomeeNodeEntity as HomeeNodeEntity
from _typeshed import Incomplete
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ATTR_COLOR_TEMP_KELVIN as ATTR_COLOR_TEMP_KELVIN, ATTR_HS_COLOR as ATTR_HS_COLOR, ColorMode as ColorMode, LightEntity as LightEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.util.color import brightness_to_value as brightness_to_value, color_RGB_to_hs as color_RGB_to_hs, color_hs_to_RGB as color_hs_to_RGB, value_to_brightness as value_to_brightness
from pyHomee.const import AttributeType
from pyHomee.model import HomeeAttribute as HomeeAttribute, HomeeNode as HomeeNode
from typing import Any

LIGHT_ATTRIBUTES: Incomplete
PARALLEL_UPDATES: int

def is_light_node(node: HomeeNode) -> bool: ...
def get_color_mode(supported_modes: set[ColorMode]) -> ColorMode: ...
def get_light_attribute_sets(node: HomeeNode) -> list[dict[AttributeType, HomeeAttribute]]: ...
def rgb_list_to_decimal(color: tuple[int, int, int]) -> int: ...
def decimal_to_rgb_list(color: float) -> list[int]: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: HomeeConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class HomeeLight(HomeeNodeEntity, LightEntity):
    _on_off_attr: HomeeAttribute
    _dimmer_attr: HomeeAttribute | None
    _col_attr: HomeeAttribute | None
    _temp_attr: HomeeAttribute | None
    _mode_attr: HomeeAttribute | None
    _attr_supported_color_modes: Incomplete
    _attr_color_mode: Incomplete
    _attr_min_color_temp_kelvin: Incomplete
    _attr_max_color_temp_kelvin: Incomplete
    _attr_translation_key: str
    _attr_translation_placeholders: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, node: HomeeNode, light: dict[AttributeType, HomeeAttribute], entry: HomeeConfigEntry) -> None: ...
    @property
    def brightness(self) -> int: ...
    @property
    def hs_color(self) -> tuple[float, float] | None: ...
    @property
    def color_temp_kelvin(self) -> int: ...
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    def _get_supported_color_modes(self) -> set[ColorMode]: ...
