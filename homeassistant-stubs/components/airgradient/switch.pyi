from . import AirGradientConfigEntry as AirGradientConfigEntry
from .const import DOMAIN as DOMAIN
from .coordinator import AirGradientConfigCoordinator as AirGradientConfigCoordinator
from .entity import AirGradientEntity as AirGradientEntity
from _typeshed import Incomplete
from airgradient import AirGradientClient as AirGradientClient, Config as Config
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

@dataclass(frozen=True, kw_only=True)
class AirGradientSwitchEntityDescription(SwitchEntityDescription):
    value_fn: Callable[[Config], bool]
    set_value_fn: Callable[[AirGradientClient, bool], Awaitable[None]]
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, value_fn, set_value_fn) -> None: ...

POST_DATA_TO_AIRGRADIENT: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: AirGradientConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AirGradientSwitch(AirGradientEntity, SwitchEntity):
    entity_description: AirGradientSwitchEntityDescription
    coordinator: AirGradientConfigCoordinator
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: AirGradientConfigCoordinator, description: AirGradientSwitchEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
