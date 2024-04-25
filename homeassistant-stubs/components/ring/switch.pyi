from . import RingData as RingData
from .const import DOMAIN as DOMAIN
from .coordinator import RingDataCoordinator as RingDataCoordinator
from .entity import RingEntity as RingEntity, exception_wrap as exception_wrap
from _typeshed import Incomplete
from homeassistant.components.switch import SwitchEntity as SwitchEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from ring_doorbell import RingStickUpCam
from typing import Any

_LOGGER: Incomplete
SKIP_UPDATES_DELAY: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class BaseRingSwitch(RingEntity[RingStickUpCam], SwitchEntity):
    _device_type: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, device: RingStickUpCam, coordinator: RingDataCoordinator, device_type: str) -> None: ...

class SirenSwitch(BaseRingSwitch):
    _attr_translation_key: str
    _no_updates_until: Incomplete
    _attr_is_on: Incomplete
    def __init__(self, device: RingStickUpCam, coordinator: RingDataCoordinator) -> None: ...
    def _handle_coordinator_update(self) -> None: ...
    def _set_switch(self, new_state: int) -> None: ...
    def turn_on(self, **kwargs: Any) -> None: ...
    def turn_off(self, **kwargs: Any) -> None: ...
