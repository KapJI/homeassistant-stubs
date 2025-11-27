from . import ATTR_CURRENT_POSITION as ATTR_CURRENT_POSITION, CoverDeviceClass as CoverDeviceClass, CoverState as CoverState
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.const import CONF_OPTIONS as CONF_OPTIONS
from homeassistant.core import HomeAssistant as HomeAssistant, State as State
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity import get_device_class as get_device_class
from homeassistant.helpers.trigger import ENTITY_STATE_TRIGGER_SCHEMA_FIRST_LAST as ENTITY_STATE_TRIGGER_SCHEMA_FIRST_LAST, EntityTriggerBase as EntityTriggerBase, Trigger as Trigger, TriggerConfig as TriggerConfig
from homeassistant.helpers.typing import UNDEFINED as UNDEFINED, UndefinedType as UndefinedType
from typing import Final

ATTR_FULLY_OPENED: Final[str]
COVER_OPENED_TRIGGER_SCHEMA: Incomplete

def get_device_class_or_undefined(hass: HomeAssistant, entity_id: str) -> str | None | UndefinedType: ...

class CoverOpenedClosedTrigger(EntityTriggerBase):
    _attribute: str
    _attribute_value: int | None
    _device_class: CoverDeviceClass | None
    _domain: str
    _to_states: set[str]
    def is_to_state(self, state: State) -> bool: ...
    def entity_filter(self, entities: set[str]) -> set[str]: ...

class CoverOpenedTrigger(CoverOpenedClosedTrigger):
    _schema = COVER_OPENED_TRIGGER_SCHEMA
    _to_states: Incomplete
    _attribute_value: int
    def __init__(self, hass: HomeAssistant, config: TriggerConfig) -> None: ...

def make_cover_opened_trigger(device_class: CoverDeviceClass | None) -> type[CoverOpenedTrigger]: ...

TRIGGERS: dict[str, type[Trigger]]

async def async_get_triggers(hass: HomeAssistant) -> dict[str, type[Trigger]]: ...
