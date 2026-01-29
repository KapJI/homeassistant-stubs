from . import PooldoseConfigEntry as PooldoseConfigEntry
from .coordinator import PooldoseCoordinator as PooldoseCoordinator
from .entity import PooldoseEntity as PooldoseEntity
from _typeshed import Incomplete
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any

_LOGGER: Incomplete
PARALLEL_UPDATES: int
SWITCH_DESCRIPTIONS: tuple[SwitchEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: PooldoseConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class PooldoseSwitch(PooldoseEntity, SwitchEntity):
    def __init__(self, coordinator: PooldoseCoordinator, serial_number: str, device_info: Any, description: SwitchEntityDescription) -> None: ...
    def _handle_coordinator_update(self) -> None: ...
    _attr_is_on: Incomplete
    def _async_update_attrs(self) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
