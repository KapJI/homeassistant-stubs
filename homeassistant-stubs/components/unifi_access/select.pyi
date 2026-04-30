from .const import DOMAIN as DOMAIN
from .coordinator import UnifiAccessConfigEntry as UnifiAccessConfigEntry, UnifiAccessCoordinator as UnifiAccessCoordinator
from .entity import UnifiAccessEntity as UnifiAccessEntity
from homeassistant.components.select import SelectEntity as SelectEntity
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from unifi_access_api import Door as Door

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: UnifiAccessConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class UnifiAccessDoorLockRuleSelectEntity(UnifiAccessEntity, SelectEntity):
    _attr_translation_key: str
    def __init__(self, coordinator: UnifiAccessCoordinator, door: Door) -> None: ...
    @property
    def current_option(self) -> str | None: ...
    @property
    def options(self) -> list[str]: ...
    @property
    def available(self) -> bool: ...
    async def async_select_option(self, option: str) -> None: ...
