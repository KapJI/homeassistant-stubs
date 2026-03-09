from . import WattsVisionConfigEntry as WattsVisionConfigEntry
from .const import DOMAIN as DOMAIN
from .coordinator import WattsVisionDeviceCoordinator as WattsVisionDeviceCoordinator
from .entity import WattsVisionEntity as WattsVisionEntity
from _typeshed import Incomplete
from homeassistant.components.switch import SwitchEntity as SwitchEntity
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any
from visionpluspython.models import SwitchDevice

_LOGGER: Incomplete
PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: WattsVisionConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class WattsVisionSwitch(WattsVisionEntity[SwitchDevice], SwitchEntity):
    _attr_name: Incomplete
    def __init__(self, coordinator: WattsVisionDeviceCoordinator, switch: SwitchDevice) -> None: ...
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
