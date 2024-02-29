from .const import DOMAIN as DOMAIN
from .controller import EcovacsController as EcovacsController
from .entity import EcovacsEntity as EcovacsEntity
from _typeshed import Incomplete
from deebot_client.capabilities import CapabilityMap, VacuumCapabilities
from deebot_client.device import Device as Device
from deebot_client.events.map import CachedMapInfoEvent as CachedMapInfoEvent, MapChangedEvent as MapChangedEvent
from homeassistant.components.image import ImageEntity as ImageEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class EcovacsMap(EcovacsEntity[VacuumCapabilities, CapabilityMap], ImageEntity):
    _attr_content_type: str
    _attr_extra_state_attributes: Incomplete
    def __init__(self, device: Device, capability: CapabilityMap, hass: HomeAssistant) -> None: ...
    entity_description: Incomplete
    def image(self) -> bytes | None: ...
    _attr_image_last_updated: Incomplete
    async def async_added_to_hass(self) -> None: ...
    async def async_update(self) -> None: ...
