from .const import DOMAIN as DOMAIN
from .coordinator import AutomowerDataUpdateCoordinator as AutomowerDataUpdateCoordinator
from .entity import AutomowerControlEntity as AutomowerControlEntity
from _typeshed import Incomplete
from homeassistant.components.lawn_mower import LawnMowerActivity as LawnMowerActivity, LawnMowerEntity as LawnMowerEntity, LawnMowerEntityFeature as LawnMowerEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

SUPPORT_STATE_SERVICES: Incomplete
DOCKED_ACTIVITIES: Incomplete
MOWING_ACTIVITIES: Incomplete
PAUSED_STATES: Incomplete
_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AutomowerLawnMowerEntity(AutomowerControlEntity, LawnMowerEntity):
    _attr_name: Incomplete
    _attr_supported_features = SUPPORT_STATE_SERVICES
    _attr_unique_id: Incomplete
    def __init__(self, mower_id: str, coordinator: AutomowerDataUpdateCoordinator) -> None: ...
    @property
    def activity(self) -> LawnMowerActivity: ...
    async def async_start_mowing(self) -> None: ...
    async def async_pause(self) -> None: ...
    async def async_dock(self) -> None: ...
