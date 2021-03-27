from homeassistant.const import SERVICE_TOGGLE as SERVICE_TOGGLE, SERVICE_TURN_OFF as SERVICE_TURN_OFF, SERVICE_TURN_ON as SERVICE_TURN_ON, STATE_ON as STATE_ON
from homeassistant.core import callback as callback
from homeassistant.helpers.config_validation import PLATFORM_SCHEMA as PLATFORM_SCHEMA, PLATFORM_SCHEMA_BASE as PLATFORM_SCHEMA_BASE, make_entity_service_schema as make_entity_service_schema
from homeassistant.helpers.entity import ToggleEntity as ToggleEntity
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.typing import HomeAssistantType as HomeAssistantType
from homeassistant.loader import bind_hass as bind_hass
from typing import Any, Dict, List, Optional, Tuple

DOMAIN: str
SCAN_INTERVAL: Any
DATA_PROFILES: str
ENTITY_ID_FORMAT: Any
SUPPORT_BRIGHTNESS: int
SUPPORT_COLOR_TEMP: int
SUPPORT_EFFECT: int
SUPPORT_FLASH: int
SUPPORT_COLOR: int
SUPPORT_TRANSITION: int
SUPPORT_WHITE_VALUE: int
ATTR_TRANSITION: str
ATTR_RGB_COLOR: str
ATTR_XY_COLOR: str
ATTR_HS_COLOR: str
ATTR_COLOR_TEMP: str
ATTR_KELVIN: str
ATTR_MIN_MIREDS: str
ATTR_MAX_MIREDS: str
ATTR_COLOR_NAME: str
ATTR_WHITE_VALUE: str
ATTR_BRIGHTNESS: str
ATTR_BRIGHTNESS_PCT: str
ATTR_BRIGHTNESS_STEP: str
ATTR_BRIGHTNESS_STEP_PCT: str
ATTR_PROFILE: str
ATTR_FLASH: str
FLASH_SHORT: str
FLASH_LONG: str
ATTR_EFFECT_LIST: str
ATTR_EFFECT: str
EFFECT_COLORLOOP: str
EFFECT_RANDOM: str
EFFECT_WHITE: str
COLOR_GROUP: str
LIGHT_PROFILES_FILE: str
VALID_TRANSITION: Any
VALID_BRIGHTNESS: Any
VALID_BRIGHTNESS_PCT: Any
VALID_BRIGHTNESS_STEP: Any
VALID_BRIGHTNESS_STEP_PCT: Any
VALID_FLASH: Any
LIGHT_TURN_ON_SCHEMA: Any

def is_on(hass: Any, entity_id: Any): ...
def preprocess_turn_on_alternatives(hass: Any, params: Any) -> None: ...
def filter_turn_off_params(params: Any): ...
async def async_setup(hass: Any, config: Any): ...
async def async_setup_entry(hass: Any, entry: Any): ...
async def async_unload_entry(hass: Any, entry: Any): ...

class Profile:
    name: str
    color_x: Optional[float] = ...
    color_y: Optional[float] = ...
    brightness: Optional[int]
    transition: Optional[int] = ...
    hs_color: Optional[Tuple[float, float]] = ...
    SCHEMA: Any = ...
    def __post_init__(self) -> None: ...
    @classmethod
    def from_csv_row(cls: Any, csv_row: List[str]) -> Profile: ...
    def __init__(self, name: Any, color_x: Any, color_y: Any, brightness: Any, transition: Any) -> None: ...

class Profiles:
    hass: Any = ...
    data: Any = ...
    def __init__(self, hass: HomeAssistantType) -> None: ...
    async def async_initialize(self) -> None: ...
    def apply_default(self, entity_id: str, params: Dict) -> None: ...
    def apply_profile(self, name: str, params: Dict) -> None: ...

class LightEntity(ToggleEntity):
    @property
    def brightness(self) -> None: ...
    @property
    def hs_color(self) -> None: ...
    @property
    def color_temp(self) -> None: ...
    @property
    def min_mireds(self): ...
    @property
    def max_mireds(self): ...
    @property
    def white_value(self) -> None: ...
    @property
    def effect_list(self) -> None: ...
    @property
    def effect(self) -> None: ...
    @property
    def capability_attributes(self): ...
    @property
    def state_attributes(self): ...
    @property
    def supported_features(self): ...

class Light(LightEntity):
    def __init_subclass__(cls, **kwargs: Any) -> None: ...
