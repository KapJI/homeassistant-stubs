from .const import DOMAIN as DOMAIN
from .coordinator import UnifiAccessConfigEntry as UnifiAccessConfigEntry, UnifiAccessCoordinator as UnifiAccessCoordinator
from .entity import UnifiAccessHubEntity as UnifiAccessHubEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any
from unifi_access_api import EmergencyStatus

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class UnifiAccessSwitchEntityDescription(SwitchEntityDescription):
    value_fn: Callable[[EmergencyStatus], bool]
    set_fn: Callable[[EmergencyStatus, bool], EmergencyStatus]

SWITCH_DESCRIPTIONS: tuple[UnifiAccessSwitchEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: UnifiAccessConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class UnifiAccessEmergencySwitch(UnifiAccessHubEntity, SwitchEntity):
    entity_description: UnifiAccessSwitchEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: UnifiAccessCoordinator, description: UnifiAccessSwitchEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def _async_set_emergency(self, value: bool) -> None: ...
