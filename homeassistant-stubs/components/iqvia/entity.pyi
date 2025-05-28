from .const import CONF_ZIP_CODE as CONF_ZIP_CODE, TYPE_ALLERGY_FORECAST as TYPE_ALLERGY_FORECAST, TYPE_ALLERGY_OUTLOOK as TYPE_ALLERGY_OUTLOOK
from .coordinator import IqviaConfigEntry as IqviaConfigEntry, IqviaUpdateCoordinator as IqviaUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.core import callback as callback
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class IQVIAEntity(CoordinatorEntity[IqviaUpdateCoordinator]):
    _attr_has_entity_name: bool
    _attr_extra_state_attributes: Incomplete
    _attr_unique_id: Incomplete
    _entry: Incomplete
    entity_description: Incomplete
    def __init__(self, coordinator: IqviaUpdateCoordinator, entry: IqviaConfigEntry, description: EntityDescription) -> None: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @callback
    def update_from_latest_data(self) -> None: ...
