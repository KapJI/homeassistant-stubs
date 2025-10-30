from .coordinator import VolvoConfigEntry as VolvoConfigEntry
from .entity import VolvoEntity as VolvoEntity, VolvoEntityDescription as VolvoEntityDescription
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.device_tracker import TrackerEntity as TrackerEntity, TrackerEntityDescription as TrackerEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from volvocarsapi.models import VolvoCarsApiBaseModel as VolvoCarsApiBaseModel

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class VolvoTrackerDescription(VolvoEntityDescription, TrackerEntityDescription): ...

_DESCRIPTIONS: tuple[VolvoTrackerDescription, ...]

async def async_setup_entry(_: HomeAssistant, entry: VolvoConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class VolvoDeviceTracker(VolvoEntity, TrackerEntity):
    entity_description: VolvoTrackerDescription
    _attr_longitude: Incomplete
    _attr_latitude: Incomplete
    def _update_state(self, api_field: VolvoCarsApiBaseModel | None) -> None: ...
