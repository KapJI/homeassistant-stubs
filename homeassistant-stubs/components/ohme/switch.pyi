from .const import DOMAIN as DOMAIN
from .coordinator import OhmeConfigEntry as OhmeConfigEntry
from .entity import OhmeEntity as OhmeEntity, OhmeEntityDescription as OhmeEntityDescription
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from ohme import OhmeApiClient as OhmeApiClient
from typing import Any

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class OhmeConfigSwitchDescription(OhmeEntityDescription, SwitchEntityDescription):
    configuration_key: str

@dataclass(frozen=True, kw_only=True)
class OhmeSwitchDescription(OhmeEntityDescription, SwitchEntityDescription):
    is_on_fn: Callable[[OhmeApiClient], bool]
    off_fn: Callable[[OhmeApiClient], Awaitable]
    on_fn: Callable[[OhmeApiClient], Awaitable]

SWITCH_CONFIG: Incomplete
SWITCH_DESCRIPTION: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: OhmeConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class OhmeSwitch(OhmeEntity, SwitchEntity):
    entity_description: OhmeSwitchDescription
    @property
    def is_on(self) -> bool: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...

class OhmeConfigSwitch(OhmeEntity, SwitchEntity):
    entity_description: OhmeConfigSwitchDescription
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def _toggle(self, on: bool) -> None: ...
