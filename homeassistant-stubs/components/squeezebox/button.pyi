from . import SqueezeboxConfigEntry as SqueezeboxConfigEntry
from .const import SIGNAL_PLAYER_DISCOVERED as SIGNAL_PLAYER_DISCOVERED
from .coordinator import SqueezeBoxPlayerUpdateCoordinator as SqueezeBoxPlayerUpdateCoordinator
from .entity import SqueezeboxEntity as SqueezeboxEntity
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.button import ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import format_mac as format_mac
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

_LOGGER: Incomplete
HARDWARE_MODELS_WITH_SCREEN: Incomplete
HARDWARE_MODELS_WITH_TONE: Incomplete

@dataclass(frozen=True, kw_only=True)
class SqueezeboxButtonEntityDescription(ButtonEntityDescription):
    press_action: str

BUTTON_ENTITIES: tuple[SqueezeboxButtonEntityDescription, ...]
SCREEN_BUTTON_ENTITIES: tuple[SqueezeboxButtonEntityDescription, ...]
TONE_BUTTON_ENTITIES: tuple[SqueezeboxButtonEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: SqueezeboxConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class SqueezeboxButtonEntity(SqueezeboxEntity, ButtonEntity):
    entity_description: SqueezeboxButtonEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: SqueezeBoxPlayerUpdateCoordinator, entity_description: SqueezeboxButtonEntityDescription) -> None: ...
    async def async_press(self) -> None: ...
