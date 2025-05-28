from . import BoschAlarmConfigEntry as BoschAlarmConfigEntry
from .const import DOMAIN as DOMAIN
from .entity import BoschAlarmDoorEntity as BoschAlarmDoorEntity, BoschAlarmOutputEntity as BoschAlarmOutputEntity
from _typeshed import Incomplete
from bosch_alarm_mode2 import Panel as Panel
from bosch_alarm_mode2.panel import Door as Door
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any

@dataclass(kw_only=True, frozen=True)
class BoschAlarmSwitchEntityDescription(SwitchEntityDescription):
    value_fn: Callable[[Door], bool]
    on_fn: Callable[[Panel, int], Coroutine[Any, Any, None]]
    off_fn: Callable[[Panel, int], Coroutine[Any, Any, None]]

DOOR_SWITCH_TYPES: list[BoschAlarmSwitchEntityDescription]

async def async_setup_entry(hass: HomeAssistant, config_entry: BoschAlarmConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

PARALLEL_UPDATES: int

class PanelDoorEntity(BoschAlarmDoorEntity, SwitchEntity):
    entity_description: BoschAlarmSwitchEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, panel: Panel, door_id: int, unique_id: str, entity_description: BoschAlarmSwitchEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...

class PanelOutputEntity(BoschAlarmOutputEntity, SwitchEntity):
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, panel: Panel, output_id: int, unique_id: str) -> None: ...
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
