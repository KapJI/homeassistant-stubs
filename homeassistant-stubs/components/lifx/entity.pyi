from .const import DOMAIN as DOMAIN
from .coordinator import LIFXConfigEntry as LIFXConfigEntry, LIFXState as LIFXState, LIFXUpdateCoordinator as LIFXUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import override

@callback
def async_repair_device_registry(hass: HomeAssistant, entry: LIFXConfigEntry, state: LIFXState) -> None: ...

class LIFXEntity(CoordinatorEntity[LIFXUpdateCoordinator]):
    _attr_has_entity_name: bool
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: LIFXUpdateCoordinator, description: EntityDescription | None = None) -> None: ...
    @callback
    def _async_update_attrs(self) -> None: ...
    @callback
    @override
    def _handle_coordinator_update(self) -> None: ...
