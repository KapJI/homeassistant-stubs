from . import TPLinkConfigEntry as TPLinkConfigEntry
from .deprecate import DeprecatedInfo as DeprecatedInfo
from .entity import CoordinatedTPLinkFeatureEntity as CoordinatedTPLinkFeatureEntity, TPLinkFeatureEntityDescription as TPLinkFeatureEntityDescription
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Final

@dataclass(frozen=True, kw_only=True)
class TPLinkButtonEntityDescription(ButtonEntityDescription, TPLinkFeatureEntityDescription): ...

PARALLEL_UPDATES: int
BUTTON_DESCRIPTIONS: Final[Incomplete]
BUTTON_DESCRIPTIONS_MAP: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: TPLinkConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class TPLinkButtonEntity(CoordinatedTPLinkFeatureEntity, ButtonEntity):
    entity_description: TPLinkButtonEntityDescription
    async def async_press(self) -> None: ...
    def _async_update_attrs(self) -> bool: ...
