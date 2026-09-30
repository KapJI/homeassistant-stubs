from .const import CONF_IR_EMITTER_ENTITY_ID as CONF_IR_EMITTER_ENTITY_ID, CONF_IR_RECEIVER_ENTITY_ID as CONF_IR_RECEIVER_ENTITY_ID
from .entity import OsramIrEmitterEntity as OsramIrEmitterEntity
from _typeshed import Incomplete
from homeassistant.components.infrared import InfraredReceivedSignal as InfraredReceivedSignal, InfraredReceiverConsumerEntity as InfraredReceiverConsumerEntity
from homeassistant.components.light import ATTR_EFFECT as ATTR_EFFECT, ATTR_RGB_COLOR as ATTR_RGB_COLOR, ColorMode as ColorMode, EFFECT_OFF as EFFECT_OFF, LightEntity as LightEntity, LightEntityFeature as LightEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ServiceValidationError as ServiceValidationError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from infrared_protocols.codes.osram.light import OsramLightCode
from typing import Any, Final, override

_LOGGER: Incomplete
PARALLEL_UPDATES: int
WHITE_SATURATION_THRESHOLD: float
RGB_WHITE: Final[tuple[int, int, int]]
HUE_TO_CODE: Final[dict[int, OsramLightCode]]
SUPPORTED_HUES: Final[tuple[int, ...]]
CODE_TO_HUE: Final[dict[OsramLightCode, int]]
CODE_TO_RGB: Final[dict[OsramLightCode, tuple[int, int, int]]]
EFFECT_TO_CODE: Final[dict[str, OsramLightCode]]
CODE_TO_EFFECT: Final[dict[OsramLightCode, str]]
EFFECT_LIST: Final[list[str]]
CMD_REPEAT_COUNT: int

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...
def _snap_hue(hue: float) -> int: ...
def _rgb_color_to_code_and_reported_rgb(rgb_color: tuple[int, int, int]) -> tuple[OsramLightCode, tuple[int, int, int]]: ...

class OsramIrLight(OsramIrEmitterEntity, LightEntity):
    _attr_assumed_state: bool
    _attr_color_mode: Incomplete
    _attr_effect_list = EFFECT_LIST
    _attr_name: Incomplete
    _attr_rgb_color = RGB_WHITE
    _attr_supported_color_modes: Incomplete
    _attr_supported_features: Incomplete
    _attr_is_on: Incomplete
    _attr_effect: Incomplete
    _last_static_color_code: Incomplete
    _last_static_rgb_color: Incomplete
    def __init__(self, entry: ConfigEntry, emitter_entity_id: str) -> None: ...
    @override
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @override
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def _async_set_rgb_color(self, rgb_color: tuple[int, int, int]) -> None: ...
    async def _async_set_effect(self, effect: str) -> None: ...
    @callback
    def _update_off_state(self) -> None: ...
    @callback
    def _update_static_color_state(self, code: OsramLightCode, rgb_color: tuple[int, int, int]) -> None: ...
    @callback
    def _update_effect_state(self, effect: str) -> None: ...

class OsramIrLightWithReceiver(OsramIrLight, InfraredReceiverConsumerEntity):
    _infrared_receiver_entity_id: Incomplete
    def __init__(self, entry: ConfigEntry, emitter_entity_id: str, receiver_entity_id: str) -> None: ...
    @override
    @callback
    def _handle_signal(self, signal: InfraredReceivedSignal) -> None: ...
    _attr_is_on: bool
    @callback
    def _apply_received_code(self, code: OsramLightCode) -> None: ...
