from . import BesenConfigEntry as BesenConfigEntry
from .coordinator import BesenCoordinator as BesenCoordinator
from .entity import BesenEntity as BesenEntity
from homeassistant.components.switch import SwitchEntity as SwitchEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any, override

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: BesenConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class BesenChargeSwitch(BesenEntity, SwitchEntity):
    def __init__(self, coordinator: BesenCoordinator) -> None: ...
    @property
    @override
    def is_on(self) -> bool | None: ...
    @override
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @override
    async def async_turn_off(self, **kwargs: Any) -> None: ...
