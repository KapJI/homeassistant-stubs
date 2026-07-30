from .const import DOMAIN as DOMAIN
from .coordinator import EnphaseConfigEntry as EnphaseConfigEntry
from .entity import EnvoyACBAggregateControlEntity as EnvoyACBAggregateControlEntity, exception_handler as exception_handler
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.components.button import ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pyenphase import Envoy as Envoy
from typing import Any, override

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class EnvoyACBButtonEntityDescription(ButtonEntityDescription):
    press_fn: Callable[[Envoy, list[str], int, int], Coroutine[Any, Any, dict[str, Any]]]

ACB_BUTTONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: EnphaseConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class EnvoyACBButtonEntity(EnvoyACBAggregateControlEntity, ButtonEntity):
    entity_description: EnvoyACBButtonEntityDescription
    @exception_handler
    @override
    async def async_press(self) -> None: ...
