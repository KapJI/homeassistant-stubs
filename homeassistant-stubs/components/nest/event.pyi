from .const import DATA_DEVICE_MANAGER as DATA_DEVICE_MANAGER, DOMAIN as DOMAIN
from .device_info import NestDeviceInfo as NestDeviceInfo
from .events import EVENT_CAMERA_MOTION as EVENT_CAMERA_MOTION, EVENT_CAMERA_PERSON as EVENT_CAMERA_PERSON, EVENT_CAMERA_SOUND as EVENT_CAMERA_SOUND, EVENT_DOORBELL_CHIME as EVENT_DOORBELL_CHIME, EVENT_NAME_MAP as EVENT_NAME_MAP
from _typeshed import Incomplete
from dataclasses import dataclass
from google_nest_sdm.device import Device as Device
from google_nest_sdm.device_manager import DeviceManager as DeviceManager
from google_nest_sdm.event import EventMessage as EventMessage, EventType
from google_nest_sdm.traits import TraitType
from homeassistant.components.event import EventDeviceClass as EventDeviceClass, EventEntity as EventEntity, EventEntityDescription as EventEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

_LOGGER: Incomplete

@dataclass(kw_only=True, frozen=True)
class NestEventEntityDescription(EventEntityDescription):
    trait_types: list[TraitType]
    api_event_types: list[EventType]
    event_types: list[str]
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., event_types, trait_types, api_event_types) -> None: ...

ENTITY_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class NestTraitEventEntity(EventEntity):
    entity_description: NestEventEntityDescription
    _attr_has_entity_name: bool
    _device: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, entity_description: NestEventEntityDescription, device: Device) -> None: ...
    async def _async_handle_event(self, event_message: EventMessage) -> None: ...
    async def async_added_to_hass(self) -> None: ...
