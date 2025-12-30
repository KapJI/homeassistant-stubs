from .coordinator import TransmissionConfigEntry as TransmissionConfigEntry, TransmissionDataUpdateCoordinator as TransmissionDataUpdateCoordinator
from .entity import TransmissionEntity as TransmissionEntity
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any

PARALLEL_UPDATES: int
AFTER_WRITE_SLEEP: int

@dataclass(frozen=True, kw_only=True)
class TransmissionSwitchEntityDescription(SwitchEntityDescription):
    is_on_func: Callable[[TransmissionDataUpdateCoordinator], bool | None]
    on_func: Callable[[TransmissionDataUpdateCoordinator], None]
    off_func: Callable[[TransmissionDataUpdateCoordinator], None]

SWITCH_TYPES: tuple[TransmissionSwitchEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: TransmissionConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class TransmissionSwitch(TransmissionEntity, SwitchEntity):
    entity_description: TransmissionSwitchEntityDescription
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
