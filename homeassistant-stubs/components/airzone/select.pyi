from . import AirzoneConfigEntry as AirzoneConfigEntry
from .coordinator import AirzoneUpdateCoordinator as AirzoneUpdateCoordinator
from .entity import AirzoneEntity as AirzoneEntity, AirzoneZoneEntity as AirzoneZoneEntity
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any, Final

@dataclass(frozen=True, kw_only=True)
class AirzoneSelectDescription(SelectEntityDescription):
    api_param: str
    options_dict: dict[str, int]
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, options, api_param, options_dict) -> None: ...

GRILLE_ANGLE_DICT: Final[dict[str, int]]
SLEEP_DICT: Final[dict[str, int]]
ZONE_SELECT_TYPES: Final[tuple[AirzoneSelectDescription, ...]]

async def async_setup_entry(hass: HomeAssistant, entry: AirzoneConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AirzoneBaseSelect(AirzoneEntity, SelectEntity):
    entity_description: AirzoneSelectDescription
    values_dict: dict[int, str]
    def _handle_coordinator_update(self) -> None: ...
    def _get_current_option(self) -> str | None: ...
    _attr_current_option: Incomplete
    def _async_update_attrs(self) -> None: ...

class AirzoneZoneSelect(AirzoneZoneEntity, AirzoneBaseSelect):
    _attr_unique_id: Incomplete
    entity_description: Incomplete
    values_dict: Incomplete
    def __init__(self, coordinator: AirzoneUpdateCoordinator, description: AirzoneSelectDescription, entry: ConfigEntry, system_zone_id: str, zone_data: dict[str, Any]) -> None: ...
    async def async_select_option(self, option: str) -> None: ...
