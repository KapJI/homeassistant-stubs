from .const import IDENTIFY as IDENTIFY, RESTART as RESTART
from .coordinator import LIFXConfigEntry as LIFXConfigEntry, LIFXUpdateCoordinator as LIFXUpdateCoordinator
from .entity import LIFXEntity as LIFXEntity
from _typeshed import Incomplete
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

RESTART_BUTTON_DESCRIPTION: Incomplete
IDENTIFY_BUTTON_DESCRIPTION: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: LIFXConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LIFXButton(LIFXEntity, ButtonEntity):
    _attr_should_poll: bool
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: LIFXUpdateCoordinator) -> None: ...

class LIFXRestartButton(LIFXButton):
    entity_description = RESTART_BUTTON_DESCRIPTION
    async def async_press(self) -> None: ...

class LIFXIdentifyButton(LIFXButton):
    entity_description = IDENTIFY_BUTTON_DESCRIPTION
    async def async_press(self) -> None: ...
