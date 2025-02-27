from . import RingConfigEntry as RingConfigEntry
from .coordinator import RingDataCoordinator as RingDataCoordinator
from .entity import RingEntity as RingEntity, exception_wrap as exception_wrap
from _typeshed import Incomplete
from homeassistant.components.button import ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from ring_doorbell import RingOther

PARALLEL_UPDATES: int
BUTTON_DESCRIPTION: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: RingConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class RingDoorButton(RingEntity[RingOther], ButtonEntity):
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, device: RingOther, coordinator: RingDataCoordinator, description: ButtonEntityDescription) -> None: ...
    @exception_wrap
    async def async_press(self) -> None: ...
