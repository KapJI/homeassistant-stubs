from .const import ATTR_DATETIME as ATTR_DATETIME, DOMAIN as DOMAIN
from datetime import datetime
from functools import cached_property
from homeassistant.helpers.entity import Entity, EntityDescription

__all__ = ['ATTR_DATETIME', 'DOMAIN', 'DateTimeEntity', 'DateTimeEntityDescription']

class DateTimeEntityDescription(EntityDescription, frozen_or_thawed=True):
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement) -> None: ...

class DateTimeEntity(Entity, cached_properties=CACHED_PROPERTIES_WITH_ATTR_):
    entity_description: DateTimeEntityDescription
    _attr_device_class: None
    _attr_state: None
    _attr_native_value: datetime | None
    @cached_property
    def device_class(self) -> None: ...
    @cached_property
    def state_attributes(self) -> None: ...
    @property
    def state(self) -> str | None: ...
    @cached_property
    def native_value(self) -> datetime | None: ...
    def set_value(self, value: datetime) -> None: ...
    async def async_set_value(self, value: datetime) -> None: ...
