import re
from .const import DOMAIN as DOMAIN
from homeassistant.backports.enum import StrEnum
from homeassistant.helpers.entity import Entity, EntityDescription
from homeassistant.helpers.restore_state import ExtraStoredData, RestoreEntity
from typing import Any

class TextMode(StrEnum):
    PASSWORD: str
    TEXT: str

class TextEntityDescription(EntityDescription):
    native_min: int
    native_max: int
    mode: TextMode
    pattern: str | None
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, native_min, native_max, mode, pattern) -> None: ...

class TextEntity(Entity):
    entity_description: TextEntityDescription
    _attr_mode: TextMode
    _attr_native_value: str | None
    _attr_native_min: int
    _attr_native_max: int
    _attr_pattern: str | None
    _attr_state: None
    __pattern_cmp: re.Pattern | None
    @property
    def capability_attributes(self) -> dict[str, Any]: ...
    @property
    def state(self) -> str | None: ...
    @property
    def mode(self) -> TextMode: ...
    @property
    def native_min(self) -> int: ...
    @property
    def min(self) -> int: ...
    @property
    def native_max(self) -> int: ...
    @property
    def max(self) -> int: ...
    @property
    def pattern_cmp(self) -> re.Pattern | None: ...
    @property
    def pattern(self) -> str | None: ...
    @property
    def native_value(self) -> str | None: ...
    def set_value(self, value: str) -> None: ...
    async def async_set_value(self, value: str) -> None: ...

class TextExtraStoredData(ExtraStoredData):
    native_value: str | None
    native_min: int
    native_max: int
    def as_dict(self) -> dict[str, Any]: ...
    @classmethod
    def from_dict(cls, restored: dict[str, Any]) -> TextExtraStoredData | None: ...
    def __init__(self, native_value, native_min, native_max) -> None: ...

class RestoreText(TextEntity, RestoreEntity):
    @property
    def extra_restore_state_data(self) -> TextExtraStoredData: ...
    async def async_get_last_text_data(self) -> TextExtraStoredData | None: ...
