from . import TPLinkConfigEntry as TPLinkConfigEntry
from .entity import CoordinatedTPLinkFeatureEntity as CoordinatedTPLinkFeatureEntity, TPLinkFeatureEntityDescription as TPLinkFeatureEntityDescription, async_refresh_after as async_refresh_after
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

_LOGGER: Incomplete

@dataclass(frozen=True, kw_only=True)
class TPLinkSwitchEntityDescription(SwitchEntityDescription, TPLinkFeatureEntityDescription):
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., deprecated_info=...) -> None: ...

SWITCH_DESCRIPTIONS: tuple[TPLinkSwitchEntityDescription, ...]
SWITCH_DESCRIPTIONS_MAP: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: TPLinkConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class TPLinkSwitch(CoordinatedTPLinkFeatureEntity, SwitchEntity):
    entity_description: TPLinkSwitchEntityDescription
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    _attr_is_on: Incomplete
    def _async_update_attrs(self) -> None: ...
