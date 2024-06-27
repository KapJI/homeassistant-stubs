from . import RoborockCoordinators as RoborockCoordinators
from .const import DOMAIN as DOMAIN
from .coordinator import RoborockDataUpdateCoordinator as RoborockDataUpdateCoordinator
from .device import RoborockCoordinatedEntityV1 as RoborockCoordinatedEntityV1
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.util import slugify as slugify
from roborock.containers import Status as Status
from roborock.roborock_message import RoborockDataProtocol
from roborock.roborock_typing import RoborockCommand

@dataclass(frozen=True, kw_only=True)
class RoborockSelectDescription(SelectEntityDescription):
    api_command: RoborockCommand
    value_fn: Callable[[Status], str | None]
    options_lambda: Callable[[Status], list[str] | None]
    parameter_lambda: Callable[[str, Status], list[int]]
    protocol_listener: RoborockDataProtocol | None = ...
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, options, api_command, value_fn, options_lambda, parameter_lambda, protocol_listener) -> None: ...

SELECT_DESCRIPTIONS: list[RoborockSelectDescription]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RoborockSelectEntity(RoborockCoordinatedEntityV1, SelectEntity):
    entity_description: RoborockSelectDescription
    _attr_options: Incomplete
    def __init__(self, coordinator: RoborockDataUpdateCoordinator, entity_description: RoborockSelectDescription, options: list[str]) -> None: ...
    async def async_select_option(self, option: str) -> None: ...
    @property
    def current_option(self) -> str | None: ...
