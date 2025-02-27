from .coordinator import NanoleafConfigEntry as NanoleafConfigEntry, NanoleafCoordinator as NanoleafCoordinator
from .entity import NanoleafEntity as NanoleafEntity
from _typeshed import Incomplete
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, entry: NanoleafConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class NanoleafIdentifyButton(NanoleafEntity, ButtonEntity):
    _attr_entity_category: Incomplete
    _attr_device_class: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: NanoleafCoordinator) -> None: ...
    async def async_press(self) -> None: ...
