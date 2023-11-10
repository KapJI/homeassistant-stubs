from . import DOMAIN as DOMAIN, PrusaLinkEntity as PrusaLinkEntity, PrusaLinkUpdateCoordinator as PrusaLinkUpdateCoordinator
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.components.button import ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pyprusalink import JobInfo, PrinterInfo, PrusaLink as PrusaLink
from typing import Any, Generic, TypeVar

T = TypeVar('T', PrinterInfo, JobInfo)

@dataclass
class PrusaLinkButtonEntityDescriptionMixin(Generic[T]):
    press_fn: Callable[[PrusaLink], Coroutine[Any, Any, None]]
    def __init__(self, press_fn) -> None: ...

@dataclass
class PrusaLinkButtonEntityDescription(ButtonEntityDescription, PrusaLinkButtonEntityDescriptionMixin[T], Generic[T]):
    available_fn: Callable[[T], bool] = ...
    def __init__(self, press_fn, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, available_fn) -> None: ...

BUTTONS: dict[str, tuple[PrusaLinkButtonEntityDescription, ...]]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class PrusaLinkButtonEntity(PrusaLinkEntity, ButtonEntity):
    entity_description: PrusaLinkButtonEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: PrusaLinkUpdateCoordinator, description: PrusaLinkButtonEntityDescription) -> None: ...
    @property
    def available(self) -> bool: ...
    async def async_press(self) -> None: ...
