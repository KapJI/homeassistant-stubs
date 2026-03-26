from .coordinator import ArcamFmjConfigEntry as ArcamFmjConfigEntry
from .entity import ArcamFmjEntity as ArcamFmjEntity
from arcam.fmj.state import State as State
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

@dataclass(frozen=True, kw_only=True)
class ArcamFmjBinarySensorEntityDescription(BinarySensorEntityDescription):
    value_fn: Callable[[State], bool | None]

BINARY_SENSORS: tuple[ArcamFmjBinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: ArcamFmjConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class ArcamFmjBinarySensorEntity(ArcamFmjEntity, BinarySensorEntity):
    entity_description: ArcamFmjBinarySensorEntityDescription
    @property
    def is_on(self) -> bool | None: ...
