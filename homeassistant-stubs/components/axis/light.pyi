from .entity import AxisEventDescription as AxisEventDescription, AxisEventEntity as AxisEventEntity, TOPIC_TO_EVENT_TYPE as TOPIC_TO_EVENT_TYPE
from .hub import AxisHub as AxisHub
from _typeshed import Incomplete
from axis.models.event import Event as Event
from dataclasses import dataclass
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ColorMode as ColorMode, LightEntity as LightEntity, LightEntityDescription as LightEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

def light_name_fn(hub: AxisHub, event: Event) -> str: ...

@dataclass(frozen=True, kw_only=True)
class AxisLightDescription(AxisEventDescription, LightEntityDescription):
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, event_topic, name_fn, supported_fn) -> None: ...

ENTITY_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AxisLight(AxisEventEntity, LightEntity):
    entity_description: AxisLightDescription
    _attr_should_poll: bool
    _attr_color_mode: Incomplete
    _attr_supported_color_modes: Incomplete
    _attr_is_on: Incomplete
    _light_id: Incomplete
    current_intensity: int
    max_intensity: int
    def __init__(self, hub: AxisHub, description: AxisLightDescription, event: Event) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    def async_event_callback(self, event: Event) -> None: ...
    @property
    def brightness(self) -> int: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_update(self) -> None: ...
