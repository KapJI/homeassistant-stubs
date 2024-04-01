from .const import DOMAIN as DOMAIN
from .controller import EcovacsController as EcovacsController
from .entity import EcovacsEntity as EcovacsEntity
from _typeshed import Incomplete
from deebot_client.capabilities import Capabilities, CapabilityEvent
from deebot_client.device import Device as Device
from deebot_client.events import ReportStatsEvent
from homeassistant.components.event import EventEntity as EventEntity, EventEntityDescription as EventEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class EcovacsLastJobEventEntity(EcovacsEntity[Capabilities, CapabilityEvent[ReportStatsEvent]], EventEntity):
    entity_description: Incomplete
    def __init__(self, device: Device[Capabilities]) -> None: ...
    async def async_added_to_hass(self) -> None: ...
