from .coordinator import GoalZeroConfigEntry as GoalZeroConfigEntry
from .entity import GoalZeroEntity as GoalZeroEntity
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any, override

SWITCH_TYPES: tuple[SwitchEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: GoalZeroConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class GoalZeroSwitch(GoalZeroEntity, SwitchEntity):
    @property
    @override
    def is_on(self) -> bool: ...
    @override
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @override
    async def async_turn_on(self, **kwargs: Any) -> None: ...
