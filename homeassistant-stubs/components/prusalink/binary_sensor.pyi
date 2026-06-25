from .coordinator import PrusaLinkConfigEntry as PrusaLinkConfigEntry, PrusaLinkUpdateCoordinator as PrusaLinkUpdateCoordinator
from .entity import PrusaLinkEntity as PrusaLinkEntity, PrusaLinkEntityDescription as PrusaLinkEntityDescription
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pyprusalink.types import JobInfo as JobInfo, PrinterInfo, PrinterStatus
from pyprusalink.types_legacy import LegacyPrinterStatus as LegacyPrinterStatus
from typing import override

@dataclass(frozen=True, kw_only=True)
class PrusaLinkBinarySensorEntityDescription[T: (PrinterStatus, LegacyPrinterStatus, JobInfo, PrinterInfo)](BinarySensorEntityDescription, PrusaLinkEntityDescription):
    value_fn: Callable[[T], bool]

BINARY_SENSORS: dict[str, tuple[PrusaLinkBinarySensorEntityDescription, ...]]

async def async_setup_entry(hass: HomeAssistant, entry: PrusaLinkConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class PrusaLinkBinarySensorEntity(PrusaLinkEntity, BinarySensorEntity):
    entity_description: PrusaLinkBinarySensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: PrusaLinkUpdateCoordinator, description: PrusaLinkBinarySensorEntityDescription) -> None: ...
    @property
    @override
    def is_on(self) -> bool: ...
