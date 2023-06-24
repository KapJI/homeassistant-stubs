from .const import DOMAIN as DOMAIN
from .entity import LitterRobotEntity as LitterRobotEntity, _RobotT as _RobotT
from .hub import LitterRobotHub as LitterRobotHub
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from homeassistant.components.button import ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any, Generic

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RequiredKeysMixin(Generic[_RobotT]):
    press_fn: Callable[[_RobotT], Coroutine[Any, Any, bool]]
    def __init__(self, press_fn) -> None: ...

class RobotButtonEntityDescription(ButtonEntityDescription, RequiredKeysMixin[_RobotT]):
    def __init__(self, press_fn, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement) -> None: ...

LITTER_ROBOT_BUTTON: Incomplete
FEEDER_ROBOT_BUTTON: Incomplete

class LitterRobotButtonEntity(LitterRobotEntity[_RobotT], ButtonEntity):
    entity_description: RobotButtonEntityDescription[_RobotT]
    async def async_press(self) -> None: ...
