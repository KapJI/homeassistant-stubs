from .entity import ISYNodeEntity as ISYNodeEntity
from .models import IsyConfigEntry as IsyConfigEntry
from _typeshed import Incomplete
from homeassistant.components.event import ATTR_MULTI_PRESS_COUNT as ATTR_MULTI_PRESS_COUNT, ButtonEventType as ButtonEventType, EventDeviceClass as EventDeviceClass, EventEntity as EventEntity, EventEntityDescription as EventEntityDescription
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pyisy.helpers import NodeProperty as NodeProperty
from pyisy.nodes import Node as Node, NodeChangedEvent as NodeChangedEvent
from typing import Final, NamedTuple, override

EVENT_BUTTON_UNIQUE_ID_SUFFIX: str
ATTR_DIRECTION: str
DIRECTION_UP: str
DIRECTION_DOWN: str

class _ControlEvent(NamedTuple):
    event_type: ButtonEventType
    direction: str
    multi_press_count: int | None = ...

CONTROL_TO_EVENT: Final[dict[str, _ControlEvent]]
BUTTON_DESCRIPTION: Final[EventEntityDescription]

def _sub_button_name(node: Node) -> str: ...
async def async_setup_entry(hass: HomeAssistant, entry: IsyConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class ISYButtonEvent(ISYNodeEntity, EventEntity):
    entity_description = BUTTON_DESCRIPTION
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    _last_fade_direction: str | None
    _attr_name: Incomplete
    _attr_entity_registry_enabled_default: bool
    def __init__(self, node: Node, device_info: DeviceInfo | None = None) -> None: ...
    _control_handler: Incomplete
    _change_handler: Incomplete
    @override
    async def async_added_to_hass(self) -> None: ...
    @callback
    def _async_on_availability_change(self, event: NodeChangedEvent, key: str) -> None: ...
    @callback
    @override
    def async_on_control(self, event: NodeProperty) -> None: ...
