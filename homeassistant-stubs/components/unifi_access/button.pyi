from .const import DOMAIN as DOMAIN
from .coordinator import UnifiAccessConfigEntry as UnifiAccessConfigEntry, UnifiAccessCoordinator as UnifiAccessCoordinator
from .entity import UnifiAccessEntity as UnifiAccessEntity
from homeassistant.components.button import ButtonEntity as ButtonEntity
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from unifi_access_api import Door as Door

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: UnifiAccessConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class UnifiAccessUnlockButton(UnifiAccessEntity, ButtonEntity):
    _attr_translation_key: str
    def __init__(self, coordinator: UnifiAccessCoordinator, door: Door) -> None: ...
    async def async_press(self) -> None: ...
