from .const import CONF_CANDLE_LIGHT_MINUTES as CONF_CANDLE_LIGHT_MINUTES, CONF_HAVDALAH_OFFSET_MINUTES as CONF_HAVDALAH_OFFSET_MINUTES, DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import datetime
from hdate.zmanim import Zmanim as Zmanim
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_LANGUAGE as CONF_LANGUAGE, CONF_LOCATION as CONF_LOCATION
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import event as event
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

@dataclass(frozen=True)
class JewishCalendarBinarySensorMixIns(BinarySensorEntityDescription):
    is_on: Callable[[Zmanim], bool] = ...
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, is_on) -> None: ...

@dataclass(frozen=True)
class JewishCalendarBinarySensorEntityDescription(JewishCalendarBinarySensorMixIns, BinarySensorEntityDescription):
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, is_on) -> None: ...

BINARY_SENSORS: tuple[JewishCalendarBinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class JewishCalendarBinarySensor(BinarySensorEntity):
    _attr_should_poll: bool
    entity_description: JewishCalendarBinarySensorEntityDescription
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    _location: Incomplete
    _hebrew: Incomplete
    _candle_lighting_offset: Incomplete
    _havdalah_offset: Incomplete
    _update_unsub: Incomplete
    def __init__(self, entry_id: str, data: dict[str, Any], description: JewishCalendarBinarySensorEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool: ...
    def _get_zmanim(self) -> Zmanim: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    def _update(self, now: datetime | None = None) -> None: ...
    def _schedule_update(self) -> None: ...
