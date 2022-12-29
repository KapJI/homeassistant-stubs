from .const import DOMAIN as DOMAIN
from .coordinator import SleepIQData as SleepIQData
from .entity import SleepIQEntity as SleepIQEntity
from _typeshed import Incomplete
from asyncsleepiq import SleepIQBed as SleepIQBed
from collections.abc import Callable as Callable
from homeassistant.components.button import ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

class SleepIQButtonEntityDescriptionMixin:
    press_action: Callable[[SleepIQBed], Any]
    def __init__(self, press_action) -> None: ...

class SleepIQButtonEntityDescription(ButtonEntityDescription, SleepIQButtonEntityDescriptionMixin):
    def __init__(self, press_action, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement) -> None: ...

ENTITY_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SleepNumberButton(SleepIQEntity, ButtonEntity):
    entity_description: SleepIQButtonEntityDescription
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, bed: SleepIQBed, entity_description: SleepIQButtonEntityDescription) -> None: ...
    async def async_press(self) -> None: ...
