from . import YouTubeDataUpdateCoordinator as YouTubeDataUpdateCoordinator
from .const import ATTR_LATEST_VIDEO as ATTR_LATEST_VIDEO, ATTR_PUBLISHED_AT as ATTR_PUBLISHED_AT, ATTR_SUBSCRIBER_COUNT as ATTR_SUBSCRIBER_COUNT, ATTR_THUMBNAIL as ATTR_THUMBNAIL, ATTR_TITLE as ATTR_TITLE, ATTR_VIDEO_ID as ATTR_VIDEO_ID, COORDINATOR as COORDINATOR, DOMAIN as DOMAIN
from .entity import YouTubeChannelEntity as YouTubeChannelEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_ICON as ATTR_ICON
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from typing import Any

@dataclass(frozen=True, kw_only=True)
class YouTubeSensorEntityDescription(SensorEntityDescription):
    available_fn: Callable[[Any], bool]
    value_fn: Callable[[Any], StateType]
    entity_picture_fn: Callable[[Any], str | None]
    attributes_fn: Callable[[Any], dict[str, Any] | None] | None
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement, available_fn, value_fn, entity_picture_fn, attributes_fn) -> None: ...

SENSOR_TYPES: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class YouTubeSensor(YouTubeChannelEntity, SensorEntity):
    entity_description: YouTubeSensorEntityDescription
    @property
    def available(self) -> bool: ...
    @property
    def native_value(self) -> StateType: ...
    @property
    def entity_picture(self) -> str | None: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any] | None: ...
