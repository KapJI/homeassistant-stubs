from .const import DOMAIN as DOMAIN
from .coordinator import AirGradientConfigCoordinator as AirGradientConfigCoordinator, AirGradientMeasurementCoordinator as AirGradientMeasurementCoordinator
from .entity import AirGradientEntity as AirGradientEntity
from _typeshed import Incomplete
from airgradient import AirGradientClient as AirGradientClient, Config as Config
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ServiceValidationError as ServiceValidationError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

@dataclass(frozen=True, kw_only=True)
class AirGradientSelectEntityDescription(SelectEntityDescription):
    value_fn: Callable[[Config], str | None]
    set_value_fn: Callable[[AirGradientClient, str], Awaitable[None]]
    requires_display: bool = ...
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, options, value_fn, set_value_fn, requires_display) -> None: ...

CONFIG_CONTROL_ENTITY: Incomplete
PROTECTED_SELECT_TYPES: tuple[AirGradientSelectEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AirGradientSelect(AirGradientEntity, SelectEntity):
    entity_description: AirGradientSelectEntityDescription
    coordinator: AirGradientConfigCoordinator
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: AirGradientConfigCoordinator, description: AirGradientSelectEntityDescription) -> None: ...
    @property
    def current_option(self) -> str | None: ...
    async def async_select_option(self, option: str) -> None: ...

class AirGradientProtectedSelect(AirGradientSelect):
    async def async_select_option(self, option: str) -> None: ...
