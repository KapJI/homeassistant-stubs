from .const import DOMAIN as DOMAIN
from .controller import EcovacsController as EcovacsController
from .entity import EcovacsCapabilityEntityDescription as EcovacsCapabilityEntityDescription, EcovacsDescriptionEntity as EcovacsDescriptionEntity, EcovacsEntity as EcovacsEntity
from .util import get_supported_entitites as get_supported_entitites
from dataclasses import dataclass
from deebot_client.capabilities import CapabilitySetEnable
from deebot_client.events import EnableEvent as EnableEvent
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

@dataclass(kw_only=True, frozen=True)
class EcovacsSwitchEntityDescription(SwitchEntityDescription, EcovacsCapabilityEntityDescription):
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, capability_fn) -> None: ...

ENTITY_DESCRIPTIONS: tuple[EcovacsSwitchEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class EcovacsSwitchEntity(EcovacsDescriptionEntity[CapabilitySetEnable], SwitchEntity):
    entity_description: EcovacsSwitchEntityDescription
    _attr_is_on: bool
    async def async_added_to_hass(self) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
