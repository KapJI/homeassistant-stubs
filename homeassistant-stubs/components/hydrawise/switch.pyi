from .const import DEFAULT_WATERING_TIME as DEFAULT_WATERING_TIME
from .coordinator import HydrawiseConfigEntry as HydrawiseConfigEntry
from .entity import HydrawiseEntity as HydrawiseEntity
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.components.switch import SwitchDeviceClass as SwitchDeviceClass, SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pydrawise import Controller as Controller, HydrawiseBase as HydrawiseBase, Zone as Zone
from typing import Any

@dataclass(frozen=True, kw_only=True)
class HydrawiseSwitchEntityDescription(SwitchEntityDescription):
    turn_on_fn: Callable[[HydrawiseBase, Zone], Coroutine[Any, Any, None]]
    turn_off_fn: Callable[[HydrawiseBase, Zone], Coroutine[Any, Any, None]]
    value_fn: Callable[[Zone], bool]

SWITCH_TYPES: tuple[HydrawiseSwitchEntityDescription, ...]
SWITCH_KEYS: list[str]

async def async_setup_entry(hass: HomeAssistant, config_entry: HydrawiseConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class HydrawiseSwitch(HydrawiseEntity, SwitchEntity):
    entity_description: HydrawiseSwitchEntityDescription
    zone: Zone
    _attr_is_on: bool
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    def _update_attrs(self) -> None: ...
