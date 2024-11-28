from .entity import ReolinkChannelCoordinatorEntity as ReolinkChannelCoordinatorEntity, ReolinkChannelEntityDescription as ReolinkChannelEntityDescription
from .util import ReolinkConfigEntry as ReolinkConfigEntry, ReolinkData as ReolinkData
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.siren import ATTR_DURATION as ATTR_DURATION, ATTR_VOLUME_LEVEL as ATTR_VOLUME_LEVEL, SirenEntity as SirenEntity, SirenEntityDescription as SirenEntityDescription, SirenEntityFeature as SirenEntityFeature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, ServiceValidationError as ServiceValidationError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

PARALLEL_UPDATES: int

@dataclass(frozen=True)
class ReolinkSirenEntityDescription(SirenEntityDescription, ReolinkChannelEntityDescription):
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., cmd_key=..., cmd_id=..., supported=..., available_tones=...) -> None: ...

SIREN_ENTITIES: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ReolinkConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ReolinkSirenEntity(ReolinkChannelCoordinatorEntity, SirenEntity):
    _attr_supported_features: Incomplete
    entity_description: ReolinkSirenEntityDescription
    def __init__(self, reolink_data: ReolinkData, channel: int, entity_description: ReolinkSirenEntityDescription) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
