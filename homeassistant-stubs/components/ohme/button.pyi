from .const import DOMAIN as DOMAIN
from .coordinator import OhmeConfigEntry as OhmeConfigEntry
from .entity import OhmeEntity as OhmeEntity, OhmeEntityDescription as OhmeEntityDescription
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.components.button import ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from ohme import OhmeApiClient as OhmeApiClient
from typing import Any

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class OhmeButtonDescription(OhmeEntityDescription, ButtonEntityDescription):
    press_fn: Callable[[OhmeApiClient], Coroutine[Any, Any, bool]]

BUTTON_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: OhmeConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class OhmeButton(OhmeEntity, ButtonEntity):
    entity_description: OhmeButtonDescription
    async def async_press(self) -> None: ...
