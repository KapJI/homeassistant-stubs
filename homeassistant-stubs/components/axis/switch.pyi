from . import AxisConfigEntry as AxisConfigEntry
from .entity import AxisEventDescription as AxisEventDescription, AxisEventEntity as AxisEventEntity
from .hub import AxisHub as AxisHub
from _typeshed import Incomplete
from axis.models.event import Event as Event
from dataclasses import dataclass
from homeassistant.components.switch import SwitchDeviceClass as SwitchDeviceClass, SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

@dataclass(frozen=True, kw_only=True)
class AxisSwitchDescription(AxisEventDescription, SwitchEntityDescription):
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., event_topic, name_fn=..., supported_fn=...) -> None: ...

ENTITY_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: AxisConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AxisSwitch(AxisEventEntity, SwitchEntity):
    entity_description: AxisSwitchDescription
    _attr_is_on: Incomplete
    def __init__(self, hub: AxisHub, description: AxisSwitchDescription, event: Event) -> None: ...
    def async_event_callback(self, event: Event) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
