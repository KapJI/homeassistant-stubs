from . import BSBLanConfigEntry as BSBLanConfigEntry, BSBLanData as BSBLanData
from .coordinator import BSBLanFastCoordinator as BSBLanFastCoordinator
from .entity import BSBLanEntity as BSBLanEntity
from .helpers import async_sync_device_time as async_sync_device_time
from _typeshed import Incomplete
from homeassistant.components.button import ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

PARALLEL_UPDATES: int
BUTTON_DESCRIPTIONS: tuple[ButtonEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: BSBLanConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class BSBLanButtonEntity(BSBLanEntity, ButtonEntity):
    entity_description: ButtonEntityDescription
    _attr_unique_id: Incomplete
    _data: Incomplete
    def __init__(self, coordinator: BSBLanFastCoordinator, data: BSBLanData, description: ButtonEntityDescription) -> None: ...
    async def async_press(self) -> None: ...
