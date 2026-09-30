from .const import IDENTIFY as IDENTIFY, RESTART as RESTART
from .coordinator import LIFXConfigEntry as LIFXConfigEntry
from .entity import LIFXEntity as LIFXEntity
from _typeshed import Incomplete
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import override

PARALLEL_UPDATES: int
RESTART_BUTTON_DESCRIPTION: Incomplete
IDENTIFY_BUTTON_DESCRIPTION: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: LIFXConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LIFXRestartButton(LIFXEntity, ButtonEntity):
    @override
    async def async_press(self) -> None: ...

class LIFXIdentifyButton(LIFXEntity, ButtonEntity):
    @override
    async def async_press(self) -> None: ...
