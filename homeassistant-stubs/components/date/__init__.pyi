from .const import DOMAIN as DOMAIN
from datetime import date
from functools import cached_property
from homeassistant.helpers.entity import Entity, EntityDescription

__all__ = ['DOMAIN', 'DateEntity', 'DateEntityDescription']

class DateEntityDescription(EntityDescription, frozen_or_thawed=True):
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement) -> None: ...

class DateEntity(Entity, cached_properties=CACHED_PROPERTIES_WITH_ATTR_):
    entity_description: DateEntityDescription
    _attr_device_class: None
    _attr_native_value: date | None
    _attr_state: None
    @cached_property
    def device_class(self) -> None: ...
    @cached_property
    def state_attributes(self) -> None: ...
    @property
    def state(self) -> str | None: ...
    @cached_property
    def native_value(self) -> date | None: ...
    def set_value(self, value: date) -> None: ...
    async def async_set_value(self, value: date) -> None: ...
