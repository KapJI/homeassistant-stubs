from . import EcovacsConfigEntry as EcovacsConfigEntry
from .entity import EcovacsCapabilityEntityDescription as EcovacsCapabilityEntityDescription, EcovacsDescriptionEntity as EcovacsDescriptionEntity
from .util import get_supported_entities as get_supported_entities
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from deebot_client.capabilities import CapabilityEvent
from deebot_client.events.base import Event as Event
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

@dataclass(kw_only=True, frozen=True)
class EcovacsBinarySensorEntityDescription[EventT: Event](BinarySensorEntityDescription, EcovacsCapabilityEntityDescription):
    value_fn: Callable[[EventT], bool | None]

ENTITY_DESCRIPTIONS: tuple[EcovacsBinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: EcovacsConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class EcovacsBinarySensor[EventT: Event](EcovacsDescriptionEntity[CapabilityEvent[EventT]], BinarySensorEntity):
    entity_description: EcovacsBinarySensorEntityDescription
    _attr_is_on: Incomplete
    async def async_added_to_hass(self) -> None: ...
