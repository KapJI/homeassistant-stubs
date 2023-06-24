from .const import DOMAIN as DOMAIN
from .entity import LitterRobotEntity as LitterRobotEntity, _RobotT as _RobotT
from .hub import LitterRobotHub as LitterRobotHub
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any, Generic

class RequiredKeysMixin(Generic[_RobotT]):
    icons: tuple[str, str]
    set_fn: Callable[[_RobotT, bool], Coroutine[Any, Any, bool]]
    def __init__(self, icons, set_fn) -> None: ...

class RobotSwitchEntityDescription(SwitchEntityDescription, RequiredKeysMixin[_RobotT]):
    entity_category: EntityCategory
    def __init__(self, icons, set_fn, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement) -> None: ...

ROBOT_SWITCHES: Incomplete

class RobotSwitchEntity(LitterRobotEntity[_RobotT], SwitchEntity):
    entity_description: RobotSwitchEntityDescription[_RobotT]
    @property
    def is_on(self) -> bool | None: ...
    @property
    def icon(self) -> str: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
