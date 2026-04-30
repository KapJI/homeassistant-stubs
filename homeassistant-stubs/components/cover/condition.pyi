from .const import ATTR_IS_CLOSED as ATTR_IS_CLOSED, CoverDeviceClass as CoverDeviceClass, DOMAIN as DOMAIN
from .models import CoverDomainSpec as CoverDomainSpec
from collections.abc import Mapping
from homeassistant.const import STATE_OFF as STATE_OFF, STATE_ON as STATE_ON
from homeassistant.core import HomeAssistant as HomeAssistant, State as State
from homeassistant.helpers.condition import Condition as Condition, ENTITY_STATE_CONDITION_SCHEMA_ANY_ALL_FOR as ENTITY_STATE_CONDITION_SCHEMA_ANY_ALL_FOR, EntityConditionBase as EntityConditionBase

class CoverConditionBase(EntityConditionBase):
    _domain_specs: Mapping[str, CoverDomainSpec]
    _schema = ENTITY_STATE_CONDITION_SCHEMA_ANY_ALL_FOR
    def is_valid_state(self, entity_state: State) -> bool: ...

def make_cover_is_open_condition(*, device_classes: dict[str, str]) -> type[CoverConditionBase]: ...
def make_cover_is_closed_condition(*, device_classes: dict[str, str]) -> type[CoverConditionBase]: ...

DEVICE_CLASSES_AWNING: dict[str, str]
DEVICE_CLASSES_BLIND: dict[str, str]
DEVICE_CLASSES_CURTAIN: dict[str, str]
DEVICE_CLASSES_SHADE: dict[str, str]
DEVICE_CLASSES_SHUTTER: dict[str, str]
CONDITIONS: dict[str, type[Condition]]

async def async_get_conditions(hass: HomeAssistant) -> dict[str, type[Condition]]: ...
