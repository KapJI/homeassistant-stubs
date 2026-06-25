from .coordinator import YotoConfigEntry as YotoConfigEntry, YotoDataUpdateCoordinator as YotoDataUpdateCoordinator
from .entity import YotoConfigEntity as YotoConfigEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any, override
from yoto_api import Capabilities as Capabilities, PlayerConfig as PlayerConfig, YotoPlayer as YotoPlayer

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class YotoSwitchEntityDescription(SwitchEntityDescription):
    value_fn: Callable[[PlayerConfig], bool | None]
    write_fn: Callable[[bool], dict[str, Any]]
    supported_fn: Callable[[Capabilities], bool] = ...

SWITCHES: tuple[YotoSwitchEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: YotoConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class YotoSwitch(YotoConfigEntity, SwitchEntity):
    entity_description: YotoSwitchEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: YotoDataUpdateCoordinator, player: YotoPlayer, description: YotoSwitchEntityDescription) -> None: ...
    @property
    @override
    def is_on(self) -> bool | None: ...
    @override
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @override
    async def async_turn_off(self, **kwargs: Any) -> None: ...
