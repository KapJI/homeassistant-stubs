from .const import DOMAIN as DOMAIN, IMAGE_GUEST_WIFI as IMAGE_GUEST_WIFI, SWITCH_GUEST_WIFI as SWITCH_GUEST_WIFI
from .entity import DevoloCoordinatorEntity as DevoloCoordinatorEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from devolo_plc_api import Device as Device
from devolo_plc_api.device_api import WifiGuestAccessGet
from homeassistant.components.image import ImageEntity as ImageEntity, ImageEntityDescription as ImageEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator

@dataclass
class DevoloImageRequiredKeysMixin:
    image_func: Callable[[WifiGuestAccessGet], bytes]
    def __init__(self, image_func) -> None: ...

@dataclass
class DevoloImageEntityDescription(ImageEntityDescription, DevoloImageRequiredKeysMixin):
    def __init__(self, image_func, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement) -> None: ...

IMAGE_TYPES: dict[str, DevoloImageEntityDescription]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DevoloImageEntity(DevoloCoordinatorEntity[WifiGuestAccessGet], ImageEntity):
    _attr_content_type: str
    entity_description: Incomplete
    _attr_image_last_updated: Incomplete
    _data: Incomplete
    def __init__(self, entry: ConfigEntry, coordinator: DataUpdateCoordinator[WifiGuestAccessGet], description: DevoloImageEntityDescription, device: Device) -> None: ...
    def _handle_coordinator_update(self) -> None: ...
    async def async_image(self) -> bytes | None: ...
