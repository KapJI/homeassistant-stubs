from . import FytaConfigEntry as FytaConfigEntry
from .coordinator import FytaCoordinator as FytaCoordinator
from .entity import FytaPlantEntity as FytaPlantEntity
from _typeshed import Incomplete
from homeassistant.components.image import ImageEntity as ImageEntity, ImageEntityDescription as ImageEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, entry: FytaConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class FytaPlantImageEntity(FytaPlantEntity, ImageEntity):
    entity_description: ImageEntityDescription
    _attr_name: Incomplete
    def __init__(self, coordinator: FytaCoordinator, entry: ConfigEntry, description: ImageEntityDescription, plant_id: int) -> None: ...
    _attr_image_last_updated: Incomplete
    @property
    def image_url(self) -> str: ...
