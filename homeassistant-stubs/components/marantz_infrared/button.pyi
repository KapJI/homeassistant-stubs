from . import MarantzIrConfigEntry as MarantzIrConfigEntry
from .const import CONF_INFRARED_EMITTER_ENTITY_ID as CONF_INFRARED_EMITTER_ENTITY_ID, MODELS as MODELS
from .entity import MarantzIrEntity as MarantzIrEntity
from dataclasses import dataclass
from homeassistant.components.button import ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.const import CONF_MODEL as CONF_MODEL
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from infrared_protocols.codes.marantz.audio import MarantzAudioCode
from typing import override

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class MarantzIrButtonEntityDescription(ButtonEntityDescription):
    command_code: MarantzAudioCode

BUTTON_DESCRIPTIONS: tuple[MarantzIrButtonEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: MarantzIrConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class MarantzIrButton(MarantzIrEntity, ButtonEntity):
    entity_description: MarantzIrButtonEntityDescription
    def __init__(self, entry: MarantzIrConfigEntry, infrared_entity_id: str, description: MarantzIrButtonEntityDescription) -> None: ...
    @override
    async def async_press(self) -> None: ...
