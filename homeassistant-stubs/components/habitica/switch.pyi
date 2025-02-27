from .coordinator import HabiticaConfigEntry as HabiticaConfigEntry, HabiticaData as HabiticaData, HabiticaDataUpdateCoordinator as HabiticaDataUpdateCoordinator
from .entity import HabiticaBase as HabiticaBase
from collections.abc import Callable as Callable
from dataclasses import dataclass
from enum import StrEnum
from homeassistant.components.switch import SwitchDeviceClass as SwitchDeviceClass, SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any

PARALLEL_UPDATES: int

@dataclass(kw_only=True, frozen=True)
class HabiticaSwitchEntityDescription(SwitchEntityDescription):
    turn_on_fn: Callable[[HabiticaDataUpdateCoordinator], Any]
    turn_off_fn: Callable[[HabiticaDataUpdateCoordinator], Any]
    is_on_fn: Callable[[HabiticaData], bool | None]

class HabiticaSwitchEntity(StrEnum):
    SLEEP = 'sleep'

SWTICH_DESCRIPTIONS: tuple[HabiticaSwitchEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: HabiticaConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class HabiticaSwitch(HabiticaBase, SwitchEntity):
    entity_description: HabiticaSwitchEntityDescription
    @property
    def is_on(self) -> bool | None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
