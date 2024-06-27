from . import TPLinkConfigEntry as TPLinkConfigEntry
from .entity import CoordinatedTPLinkFeatureEntity as CoordinatedTPLinkFeatureEntity, TPLinkDataUpdateCoordinator as TPLinkDataUpdateCoordinator, TPLinkFeatureEntityDescription as TPLinkFeatureEntityDescription, async_refresh_after as async_refresh_after
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from kasa import Device as Device, Feature
from typing import Final

@dataclass(frozen=True, kw_only=True)
class TPLinkSelectEntityDescription(SelectEntityDescription, TPLinkFeatureEntityDescription):
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, options) -> None: ...

SELECT_DESCRIPTIONS: Final[Incomplete]
SELECT_DESCRIPTIONS_MAP: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: TPLinkConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class TPLinkSelectEntity(CoordinatedTPLinkFeatureEntity, SelectEntity):
    entity_description: TPLinkSelectEntityDescription
    _attr_options: Incomplete
    def __init__(self, device: Device, coordinator: TPLinkDataUpdateCoordinator, *, feature: Feature, description: TPLinkFeatureEntityDescription, parent: Device | None = None) -> None: ...
    async def async_select_option(self, option: str) -> None: ...
    _attr_current_option: Incomplete
    def _async_update_attrs(self) -> None: ...
