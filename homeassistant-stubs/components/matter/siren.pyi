from .entity import MatterEntity as MatterEntity, MatterEntityDescription as MatterEntityDescription
from .helpers import MatterConfigEntry as MatterConfigEntry
from .models import MatterDiscoverySchema as MatterDiscoverySchema
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.siren import SirenEntity as SirenEntity, SirenEntityDescription as SirenEntityDescription, SirenEntityFeature as SirenEntityFeature
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, config_entry: MatterConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

@dataclass(frozen=True, kw_only=True)
class MatterSirenEntityDescription(SirenEntityDescription, MatterEntityDescription): ...

class MatterSiren(MatterEntity, SirenEntity):
    entity_description: MatterSirenEntityDescription
    _attr_supported_features: Incomplete
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    _attr_is_on: Incomplete
    @callback
    def _update_from_device(self) -> None: ...

DISCOVERY_SCHEMAS: Incomplete
