from . import Eq3ConfigEntry as Eq3ConfigEntry
from .const import DEFAULT_AWAY_HOURS as DEFAULT_AWAY_HOURS, ENTITY_KEY_AWAY as ENTITY_KEY_AWAY, ENTITY_KEY_BOOST as ENTITY_KEY_BOOST, ENTITY_KEY_LOCK as ENTITY_KEY_LOCK
from .entity import Eq3Entity as Eq3Entity
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from eq3btsmart import Thermostat as Thermostat
from eq3btsmart.models import Status as Status
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any

async def async_set_away(thermostat: Thermostat, enable: bool) -> Status: ...

@dataclass(frozen=True, kw_only=True)
class Eq3SwitchEntityDescription(SwitchEntityDescription):
    toggle_func: Callable[[Thermostat], Callable[[bool], Coroutine[None, None, Status]]]
    value_func: Callable[[Status], bool]

SWITCH_ENTITY_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: Eq3ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class Eq3SwitchEntity(Eq3Entity, SwitchEntity):
    entity_description: Eq3SwitchEntityDescription
    def __init__(self, entry: Eq3ConfigEntry, entity_description: Eq3SwitchEntityDescription) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @property
    def is_on(self) -> bool: ...
