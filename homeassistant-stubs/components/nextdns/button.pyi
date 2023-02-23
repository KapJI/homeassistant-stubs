from . import NextDnsStatusUpdateCoordinator as NextDnsStatusUpdateCoordinator
from .const import ATTR_STATUS as ATTR_STATUS, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.button import ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

PARALLEL_UPDATES: int
CLEAR_LOGS_BUTTON: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class NextDnsButton(CoordinatorEntity[NextDnsStatusUpdateCoordinator], ButtonEntity):
    _attr_has_entity_name: bool
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    entity_description: Incomplete
    def __init__(self, coordinator: NextDnsStatusUpdateCoordinator, description: ButtonEntityDescription) -> None: ...
    async def async_press(self) -> None: ...
