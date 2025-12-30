from .coordinator import SFRConfigEntry as SFRConfigEntry
from .entity import SFRCoordinatorEntity as SFRCoordinatorEntity
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from sfrbox_api.models import DslInfo, FtthInfo, WanInfo

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class SFRBoxBinarySensorEntityDescription[_T](BinarySensorEntityDescription):
    value_fn: Callable[[_T], bool | None]

DSL_SENSOR_TYPES: tuple[SFRBoxBinarySensorEntityDescription[DslInfo], ...]
FTTH_SENSOR_TYPES: tuple[SFRBoxBinarySensorEntityDescription[FtthInfo], ...]
WAN_SENSOR_TYPES: tuple[SFRBoxBinarySensorEntityDescription[WanInfo], ...]

async def async_setup_entry(hass: HomeAssistant, entry: SFRConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class SFRBoxBinarySensor[_T](SFRCoordinatorEntity[_T], BinarySensorEntity):
    entity_description: SFRBoxBinarySensorEntityDescription[_T]
    @property
    def is_on(self) -> bool | None: ...
