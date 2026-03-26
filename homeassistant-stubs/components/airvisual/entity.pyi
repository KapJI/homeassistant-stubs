from .coordinator import AirVisualDataUpdateCoordinator as AirVisualDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.core import callback as callback
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class AirVisualEntity(CoordinatorEntity[AirVisualDataUpdateCoordinator]):
    _attr_extra_state_attributes: Incomplete
    entity_description: Incomplete
    def __init__(self, coordinator: AirVisualDataUpdateCoordinator, description: EntityDescription) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @callback
    def update_from_latest_data(self) -> None: ...
