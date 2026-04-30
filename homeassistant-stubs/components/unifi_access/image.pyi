from .coordinator import UnifiAccessConfigEntry as UnifiAccessConfigEntry, UnifiAccessCoordinator as UnifiAccessCoordinator
from .entity import UnifiAccessEntity as UnifiAccessEntity
from _typeshed import Incomplete
from homeassistant.components.image import ImageEntity as ImageEntity
from homeassistant.const import CONF_VERIFY_SSL as CONF_VERIFY_SSL
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from unifi_access_api import Door as Door

_LOGGER: Incomplete
PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: UnifiAccessConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class UnifiAccessDoorImageEntity(UnifiAccessEntity, ImageEntity):
    _attr_translation_key: str
    _attr_image_last_updated: Incomplete
    def __init__(self, coordinator: UnifiAccessCoordinator, hass: HomeAssistant, verify_ssl: bool, door: Door) -> None: ...
    async def async_image(self) -> bytes | None: ...
    def _handle_coordinator_update(self) -> None: ...
