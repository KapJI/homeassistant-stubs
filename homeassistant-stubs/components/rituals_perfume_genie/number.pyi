from .const import DOMAIN as DOMAIN
from .coordinator import RitualsDataUpdateCoordinator as RitualsDataUpdateCoordinator
from .entity import DiffuserEntity as DiffuserEntity
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.number import NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pyrituals import Diffuser as Diffuser
from typing import Any

@dataclass
class RitualsNumberEntityDescriptionMixin:
    value_fn: Callable[[Diffuser], int]
    set_value_fn: Callable[[Diffuser, int], Awaitable[Any]]
    def __init__(self, value_fn, set_value_fn) -> None: ...

@dataclass
class RitualsNumberEntityDescription(NumberEntityDescription, RitualsNumberEntityDescriptionMixin):
    def __init__(self, value_fn, set_value_fn, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, max_value, min_value, mode, native_max_value, native_min_value, native_step, native_unit_of_measurement, step) -> None: ...

ENTITY_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RitualsNumberEntity(DiffuserEntity, NumberEntity):
    entity_description: RitualsNumberEntityDescription
    @property
    def native_value(self) -> int: ...
    async def async_set_native_value(self, value: float) -> None: ...
