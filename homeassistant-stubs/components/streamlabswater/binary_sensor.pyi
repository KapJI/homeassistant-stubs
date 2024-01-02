from . import StreamlabsCoordinator as StreamlabsCoordinator
from .const import DOMAIN as DOMAIN
from .coordinator import StreamlabsData as StreamlabsData
from _typeshed import Incomplete
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

NAME_AWAY_MODE: str

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class StreamlabsAwayMode(CoordinatorEntity[StreamlabsCoordinator], BinarySensorEntity):
    _location_id: Incomplete
    def __init__(self, coordinator: StreamlabsCoordinator, location_id: str) -> None: ...
    @property
    def location_data(self) -> StreamlabsData: ...
    @property
    def name(self) -> str: ...
    @property
    def is_on(self) -> bool: ...
