from .common import setup_home_connect_entry as setup_home_connect_entry
from .const import DOMAIN as DOMAIN
from .coordinator import HomeConnectApplianceCoordinator as HomeConnectApplianceCoordinator, HomeConnectConfigEntry as HomeConnectConfigEntry
from .utils import get_dict_from_home_connect_error as get_dict_from_home_connect_error
from _typeshed import Incomplete
from homeassistant.components.image import Image as Image, ImageEntity as ImageEntity, ImageEntityDescription as ImageEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import override

PARALLEL_UPDATES: int
IMAGES: Incomplete

def _get_entities_for_appliance(appliance_coordinator: HomeConnectApplianceCoordinator) -> list[HomeConnectImageEntity]: ...
async def async_setup_entry(hass: HomeAssistant, entry: HomeConnectConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class HomeConnectImageEntity(ImageEntity):
    _attr_has_entity_name: bool
    _last_image_key_fetched: str | None
    appliance: Incomplete
    entity_description: Incomplete
    appliance_coordinator: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, appliance_coordinator: HomeConnectApplianceCoordinator, desc: ImageEntityDescription) -> None: ...
    @override
    async def async_added_to_hass(self) -> None: ...
    async def async_update(self) -> None: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
    _attr_image_last_updated: Incomplete
    _cached_image: Incomplete
    async def async_fetch_image(self) -> None: ...
