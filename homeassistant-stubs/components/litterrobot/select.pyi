from .const import DOMAIN as DOMAIN
from .entity import LitterRobotEntity as LitterRobotEntity, _RobotT as _RobotT, async_update_unique_id as async_update_unique_id
from .hub import LitterRobotHub as LitterRobotHub
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import TIME_MINUTES as TIME_MINUTES
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any, TypeVar

_CastTypeT = TypeVar('_CastTypeT', int, float)

class RequiredKeysMixin:
    current_fn: Callable[[_RobotT], _CastTypeT]
    options_fn: Callable[[_RobotT], list[_CastTypeT]]
    select_fn: Callable[[_RobotT, str], Coroutine[Any, Any, bool]]
    def __init__(self, current_fn, options_fn, select_fn) -> None: ...

class RobotSelectEntityDescription(SelectEntityDescription, RequiredKeysMixin[_RobotT, _CastTypeT]):
    entity_category: EntityCategory
    def __init__(self, current_fn, options_fn, select_fn, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, unit_of_measurement, options) -> None: ...

LITTER_ROBOT_SELECT: Incomplete
FEEDER_ROBOT_SELECT: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class LitterRobotSelect(LitterRobotEntity[_RobotT], SelectEntity):
    entity_description: RobotSelectEntityDescription[_RobotT, _CastTypeT]
    _attr_options: Incomplete
    def __init__(self, robot: _RobotT, hub: LitterRobotHub, description: RobotSelectEntityDescription[_RobotT, _CastTypeT]) -> None: ...
    @property
    def current_option(self) -> Union[str, None]: ...
    async def async_select_option(self, option: str) -> None: ...
