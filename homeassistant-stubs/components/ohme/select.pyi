from .const import DOMAIN as DOMAIN
from .coordinator import OhmeConfigEntry as OhmeConfigEntry
from .entity import OhmeEntity as OhmeEntity, OhmeEntityDescription as OhmeEntityDescription
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from ohme import OhmeApiClient as OhmeApiClient
from typing import Any, Final

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class OhmeSelectDescription(OhmeEntityDescription, SelectEntityDescription):
    select_fn: Callable[[OhmeApiClient, Any], Coroutine[Any, Any, bool | None]]
    options: list[str] | None = ...
    options_fn: Callable[[OhmeApiClient], list[str]] | None = ...
    current_option_fn: Callable[[OhmeApiClient], str | None]

MODE_SELECT_DESCRIPTION: Final[OhmeSelectDescription]
VEHICLE_SELECT_DESCRIPTION: Final[OhmeSelectDescription]

async def async_setup_entry(hass: HomeAssistant, config_entry: OhmeConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class OhmeSelect(OhmeEntity, SelectEntity):
    entity_description: OhmeSelectDescription
    async def async_select_option(self, option: str) -> None: ...
    @property
    def options(self) -> list[str]: ...
    @property
    def current_option(self) -> str | None: ...
