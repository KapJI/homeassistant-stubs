from .const import CONF_DIMMABLE as CONF_DIMMABLE, CONF_DOMAIN_DATA as CONF_DOMAIN_DATA, CONF_OUTPUT as CONF_OUTPUT, CONF_TRANSITION as CONF_TRANSITION, OUTPUT_PORTS as OUTPUT_PORTS
from .entity import LcnEntity as LcnEntity
from .helpers import InputType as InputType, LcnConfigEntry as LcnConfigEntry
from _typeshed import Incomplete
from collections.abc import Iterable
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ATTR_TRANSITION as ATTR_TRANSITION, ColorMode as ColorMode, LightEntity as LightEntity, LightEntityFeature as LightEntityFeature
from homeassistant.const import CONF_DOMAIN as CONF_DOMAIN, CONF_ENTITIES as CONF_ENTITIES
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.util.color import brightness_to_value as brightness_to_value, value_to_brightness as value_to_brightness
from typing import Any

BRIGHTNESS_SCALE: Incomplete
PARALLEL_UPDATES: int
SCAN_INTERVAL: Incomplete

def add_lcn_entities(config_entry: LcnConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback, entity_configs: Iterable[ConfigType]) -> None: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: LcnConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LcnOutputLight(LcnEntity, LightEntity):
    _attr_supported_features: Incomplete
    _attr_is_on: bool
    _attr_brightness: int
    output: Incomplete
    _transition: Incomplete
    dimmable: Incomplete
    _attr_color_mode: Incomplete
    _attr_supported_color_modes: Incomplete
    def __init__(self, config: ConfigType, config_entry: LcnConfigEntry) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    _attr_available: Incomplete
    async def async_update(self) -> None: ...
    def input_received(self, input_obj: InputType) -> None: ...

class LcnRelayLight(LcnEntity, LightEntity):
    _attr_color_mode: Incomplete
    _attr_supported_color_modes: Incomplete
    _attr_is_on: bool
    output: Incomplete
    def __init__(self, config: ConfigType, config_entry: LcnConfigEntry) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    _attr_available: Incomplete
    async def async_update(self) -> None: ...
    def input_received(self, input_obj: InputType) -> None: ...
