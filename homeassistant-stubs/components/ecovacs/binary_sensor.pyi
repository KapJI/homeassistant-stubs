from .const import DOMAIN as DOMAIN
from .controller import EcovacsController as EcovacsController
from .entity import EcovacsCapabilityEntityDescription as EcovacsCapabilityEntityDescription, EcovacsDescriptionEntity as EcovacsDescriptionEntity, EventT as EventT
from .util import get_supported_entitites as get_supported_entitites
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from deebot_client.capabilities import CapabilityEvent
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Generic

@dataclass(kw_only=True, frozen=True)
class EcovacsBinarySensorEntityDescription(BinarySensorEntityDescription, EcovacsCapabilityEntityDescription, Generic[EventT]):
    value_fn: Callable[[EventT], bool | None]
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, capability_fn, value_fn) -> None: ...

ENTITY_DESCRIPTIONS: tuple[EcovacsBinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class EcovacsBinarySensor(EcovacsDescriptionEntity[CapabilityEvent[EventT]], BinarySensorEntity):
    entity_description: EcovacsBinarySensorEntityDescription
    _attr_is_on: Incomplete
    async def async_added_to_hass(self) -> None: ...
