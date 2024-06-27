from . import EcovacsConfigEntry as EcovacsConfigEntry
from .const import SUPPORTED_LIFESPANS as SUPPORTED_LIFESPANS
from .entity import EcovacsCapabilityEntityDescription as EcovacsCapabilityEntityDescription, EcovacsDescriptionEntity as EcovacsDescriptionEntity, EcovacsEntity as EcovacsEntity
from .util import get_supported_entitites as get_supported_entitites
from _typeshed import Incomplete
from dataclasses import dataclass
from deebot_client.capabilities import CapabilityExecute, CapabilityLifeSpan
from deebot_client.events import LifeSpan as LifeSpan
from homeassistant.components.button import ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

@dataclass(kw_only=True, frozen=True)
class EcovacsButtonEntityDescription(ButtonEntityDescription, EcovacsCapabilityEntityDescription):
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, capability_fn) -> None: ...

@dataclass(kw_only=True, frozen=True)
class EcovacsLifespanButtonEntityDescription(ButtonEntityDescription):
    component: LifeSpan
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, component) -> None: ...

ENTITY_DESCRIPTIONS: tuple[EcovacsButtonEntityDescription, ...]
LIFESPAN_ENTITY_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: EcovacsConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class EcovacsButtonEntity(EcovacsDescriptionEntity[CapabilityExecute], ButtonEntity):
    entity_description: EcovacsLifespanButtonEntityDescription
    async def async_press(self) -> None: ...

class EcovacsResetLifespanButtonEntity(EcovacsDescriptionEntity[CapabilityLifeSpan], ButtonEntity):
    entity_description: EcovacsLifespanButtonEntityDescription
    async def async_press(self) -> None: ...
