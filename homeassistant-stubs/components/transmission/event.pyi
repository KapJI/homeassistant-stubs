from .const import ATTR_DOWNLOAD_PATH as ATTR_DOWNLOAD_PATH, ATTR_LABELS as ATTR_LABELS, EVENT_TYPE_DOWNLOADED as EVENT_TYPE_DOWNLOADED, EVENT_TYPE_REMOVED as EVENT_TYPE_REMOVED, EVENT_TYPE_STARTED as EVENT_TYPE_STARTED
from .coordinator import TransmissionConfigEntry as TransmissionConfigEntry, TransmissionEventData as TransmissionEventData
from .entity import TransmissionEntity as TransmissionEntity
from _typeshed import Incomplete
from homeassistant.components.event import EventEntity as EventEntity, EventEntityDescription as EventEntityDescription
from homeassistant.const import ATTR_ID as ATTR_ID, ATTR_NAME as ATTR_NAME
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

_LOGGER: Incomplete
PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, config_entry: TransmissionConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class TransmissionEvent(TransmissionEntity, EventEntity):
    async def async_added_to_hass(self) -> None: ...
    @callback
    def _handle_event(self, event_data: TransmissionEventData) -> None: ...
