from .coordinator import PrusaLinkConfigEntry as PrusaLinkConfigEntry, PrusaLinkUpdateCoordinator as PrusaLinkUpdateCoordinator
from .entity import PrusaLinkEntity as PrusaLinkEntity, PrusaLinkEntityDescription as PrusaLinkEntityDescription
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.components.button import ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pyprusalink import JobInfo as JobInfo, LegacyPrinterStatus as LegacyPrinterStatus, PrinterStatus, PrusaLink as PrusaLink
from typing import Any

@dataclass(frozen=True, kw_only=True)
class PrusaLinkButtonEntityDescription[T: (PrinterStatus, LegacyPrinterStatus, JobInfo)](ButtonEntityDescription, PrusaLinkEntityDescription):
    press_fn: Callable[[PrusaLink], Callable[[int], Coroutine[Any, Any, None]]]

BUTTONS: dict[str, tuple[PrusaLinkButtonEntityDescription, ...]]

async def async_setup_entry(hass: HomeAssistant, entry: PrusaLinkConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class PrusaLinkButtonEntity(PrusaLinkEntity, ButtonEntity):
    entity_description: PrusaLinkButtonEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: PrusaLinkUpdateCoordinator, description: PrusaLinkButtonEntityDescription) -> None: ...
    async def async_press(self) -> None: ...
