from . import NextDnsConfigEntry as NextDnsConfigEntry
from .const import DOMAIN as DOMAIN
from .coordinator import NextDnsUpdateCoordinator as NextDnsUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.components.button import ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from nextdns import AnalyticsStatus

PARALLEL_UPDATES: int
CLEAR_LOGS_BUTTON: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: NextDnsConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class NextDnsButton(CoordinatorEntity[NextDnsUpdateCoordinator[AnalyticsStatus]], ButtonEntity):
    _attr_has_entity_name: bool
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    entity_description: Incomplete
    def __init__(self, coordinator: NextDnsUpdateCoordinator[AnalyticsStatus], description: ButtonEntityDescription) -> None: ...
    async def async_press(self) -> None: ...
