import RFXtrx as rfxtrxmod
from . import DEFAULT_OFF_DELAY as DEFAULT_OFF_DELAY, DeviceTuple as DeviceTuple, RfxtrxCommandEntity as RfxtrxCommandEntity, async_setup_platform_entry as async_setup_platform_entry
from .const import CONF_OFF_DELAY as CONF_OFF_DELAY
from _typeshed import Incomplete
from homeassistant.components.siren import ATTR_TONE as ATTR_TONE, SirenEntity as SirenEntity, SirenEntityFeature as SirenEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.event import async_call_later as async_call_later
from typing import Any

SECURITY_PANIC_ON: str
SECURITY_PANIC_OFF: str
SECURITY_PANIC_ALL: Incomplete

def supported(event: rfxtrxmod.RFXtrxEvent) -> bool: ...
def get_first_key(data: dict[int, str], entry: str) -> int: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RfxtrxOffDelayMixin(Entity):
    _timeout: Union[CALLBACK_TYPE, None]
    _off_delay: Union[float, None]
    def _setup_timeout(self) -> None: ...
    def _cancel_timeout(self) -> None: ...

class RfxtrxChime(RfxtrxCommandEntity, SirenEntity, RfxtrxOffDelayMixin):
    _attr_supported_features: Incomplete
    _device: rfxtrxmod.ChimeDevice
    _attr_available_tones: Incomplete
    _default_tone: Incomplete
    _off_delay: Incomplete
    def __init__(self, device: rfxtrxmod.RFXtrxDevice, device_id: DeviceTuple, off_delay: Union[float, None] = ..., event: Union[rfxtrxmod.RFXtrxEvent, None] = ...) -> None: ...
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    def _apply_event(self, event: rfxtrxmod.ControlEvent) -> None: ...
    def _handle_event(self, event: rfxtrxmod.RFXtrxEvent, device_id: DeviceTuple) -> None: ...

class RfxtrxSecurityPanic(RfxtrxCommandEntity, SirenEntity, RfxtrxOffDelayMixin):
    _attr_supported_features: Incomplete
    _device: rfxtrxmod.SecurityDevice
    _on_value: Incomplete
    _off_value: Incomplete
    _off_delay: Incomplete
    def __init__(self, device: rfxtrxmod.RFXtrxDevice, device_id: DeviceTuple, off_delay: Union[float, None] = ..., event: Union[rfxtrxmod.RFXtrxEvent, None] = ...) -> None: ...
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    def _apply_event(self, event: rfxtrxmod.SensorEvent) -> None: ...
    def _handle_event(self, event: rfxtrxmod.RFXtrxEvent, device_id: DeviceTuple) -> None: ...
