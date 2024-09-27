from . import TPLinkConfigEntry as TPLinkConfigEntry
from .entity import CoordinatedTPLinkFeatureEntity as CoordinatedTPLinkFeatureEntity, TPLinkDataUpdateCoordinator as TPLinkDataUpdateCoordinator, TPLinkFeatureEntityDescription as TPLinkFeatureEntityDescription, async_refresh_after as async_refresh_after
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.number import NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription, NumberMode as NumberMode
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from kasa import Device as Device, Feature
from typing import Final

_LOGGER: Incomplete

@dataclass(frozen=True, kw_only=True)
class TPLinkNumberEntityDescription(NumberEntityDescription, TPLinkFeatureEntityDescription):
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., deprecated_info=..., max_value=..., min_value=..., mode=..., native_max_value=..., native_min_value=..., native_step=..., native_unit_of_measurement=..., step=...) -> None: ...

NUMBER_DESCRIPTIONS: Final[Incomplete]
NUMBER_DESCRIPTIONS_MAP: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: TPLinkConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class TPLinkNumberEntity(CoordinatedTPLinkFeatureEntity, NumberEntity):
    entity_description: TPLinkNumberEntityDescription
    _attr_native_min_value: Incomplete
    _attr_native_max_value: Incomplete
    def __init__(self, device: Device, coordinator: TPLinkDataUpdateCoordinator, *, feature: Feature, description: TPLinkFeatureEntityDescription, parent: Device | None = None) -> None: ...
    async def async_set_native_value(self, value: float) -> None: ...
    _attr_native_value: Incomplete
    def _async_update_attrs(self) -> None: ...
