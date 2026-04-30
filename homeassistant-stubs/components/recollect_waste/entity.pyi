from .const import CONF_PLACE_ID as CONF_PLACE_ID, CONF_SERVICE_ID as CONF_SERVICE_ID, DOMAIN as DOMAIN
from .coordinator import ReCollectWasteDataUpdateCoordinator as ReCollectWasteDataUpdateCoordinator, RecollectWasteConfigEntry as RecollectWasteConfigEntry
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class ReCollectWasteEntity(CoordinatorEntity[ReCollectWasteDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    _identifier: Incomplete
    _attr_device_info: Incomplete
    _attr_extra_state_attributes: Incomplete
    _entry: Incomplete
    def __init__(self, coordinator: ReCollectWasteDataUpdateCoordinator, entry: RecollectWasteConfigEntry) -> None: ...
    async def async_added_to_hass(self) -> None: ...
