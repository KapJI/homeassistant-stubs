from . import VistapoolConfigEntry as VistapoolConfigEntry
from .const import DOMAIN as DOMAIN, SIGNAL_NEW_POOL as SIGNAL_NEW_POOL
from .coordinator import VistapoolDataUpdateCoordinator as VistapoolDataUpdateCoordinator
from .entity import VistapoolEntity as VistapoolEntity
from _typeshed import Incomplete
from homeassistant.components.button import ButtonEntity as ButtonEntity
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import override

PARALLEL_UPDATES: int
_HASLED_PATH: str
_LIGHT_STATUS_PATH: str
_LED_PULSE_DELAY_SECONDS: float

def _build_button_entities(coordinator: VistapoolDataUpdateCoordinator) -> list[VistapoolLEDPulseButton]: ...
async def async_setup_entry(hass: HomeAssistant, entry: VistapoolConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class VistapoolLEDPulseButton(VistapoolEntity, ButtonEntity):
    _attr_translation_key: str
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: VistapoolDataUpdateCoordinator) -> None: ...
    @override
    async def async_press(self) -> None: ...
