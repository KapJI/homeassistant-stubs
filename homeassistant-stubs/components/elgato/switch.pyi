from .const import DOMAIN as DOMAIN
from .coordinator import ElgatoData as ElgatoData, ElgatoDataUpdateCoordinator as ElgatoDataUpdateCoordinator
from .entity import ElgatoEntity as ElgatoEntity
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from elgato import Elgato as Elgato
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

class ElgatoEntityDescriptionMixin:
    is_on_fn: Callable[[ElgatoData], bool | None]
    set_fn: Callable[[Elgato, bool], Awaitable[Any]]
    def __init__(self, is_on_fn, set_fn) -> None: ...

class ElgatoSwitchEntityDescription(SwitchEntityDescription, ElgatoEntityDescriptionMixin):
    has_fn: Callable[[ElgatoData], bool]
    def __init__(self, is_on_fn, set_fn, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, has_fn) -> None: ...

SWITCHES: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ElgatoSwitchEntity(ElgatoEntity, SwitchEntity):
    entity_description: ElgatoSwitchEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: ElgatoDataUpdateCoordinator, description: ElgatoSwitchEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool | None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
