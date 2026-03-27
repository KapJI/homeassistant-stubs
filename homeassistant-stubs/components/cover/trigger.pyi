from .const import ATTR_IS_CLOSED as ATTR_IS_CLOSED, CoverDeviceClass as CoverDeviceClass, DOMAIN as DOMAIN
from .models import CoverDomainSpec as CoverDomainSpec
from collections.abc import Mapping
from homeassistant.const import STATE_OFF as STATE_OFF, STATE_ON as STATE_ON, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import HomeAssistant as HomeAssistant, State as State
from homeassistant.helpers.trigger import EntityTriggerBase as EntityTriggerBase, Trigger as Trigger

class CoverTriggerBase(EntityTriggerBase):
    _domain_specs: Mapping[str, CoverDomainSpec]
    def _get_value(self, state: State) -> str | bool | None: ...
    def is_valid_state(self, state: State) -> bool: ...
    def is_valid_transition(self, from_state: State, to_state: State) -> bool: ...

def make_cover_opened_trigger(*, device_classes: dict[str, str]) -> type[CoverTriggerBase]: ...
def make_cover_closed_trigger(*, device_classes: dict[str, str]) -> type[CoverTriggerBase]: ...

DEVICE_CLASSES_AWNING: dict[str, str]
DEVICE_CLASSES_BLIND: dict[str, str]
DEVICE_CLASSES_CURTAIN: dict[str, str]
DEVICE_CLASSES_SHADE: dict[str, str]
DEVICE_CLASSES_SHUTTER: dict[str, str]
TRIGGERS: dict[str, type[Trigger]]

async def async_get_triggers(hass: HomeAssistant) -> dict[str, type[Trigger]]: ...
