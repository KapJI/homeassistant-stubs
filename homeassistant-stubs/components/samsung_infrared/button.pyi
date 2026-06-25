from .const import CONF_DEVICE_TYPE as CONF_DEVICE_TYPE, CONF_INFRARED_EMITTER_ENTITY_ID as CONF_INFRARED_EMITTER_ENTITY_ID, SamsungDeviceType as SamsungDeviceType
from .entity import SamsungIrEntity as SamsungIrEntity
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.button import ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.components.infrared import InfraredEmitterConsumerEntity as InfraredEmitterConsumerEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from infrared_protocols.codes.samsung.tv import SamsungTVCode
from typing import override

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class SamsungIrButtonEntityDescription(ButtonEntityDescription):
    command_code: SamsungTVCode

TV_BUTTON_DESCRIPTIONS: tuple[SamsungIrButtonEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class SamsungIrButton(SamsungIrEntity, InfraredEmitterConsumerEntity, ButtonEntity):
    entity_description: SamsungIrButtonEntityDescription
    _infrared_emitter_entity_id: Incomplete
    def __init__(self, entry: ConfigEntry, infrared_emitter_entity_id: str, description: SamsungIrButtonEntityDescription) -> None: ...
    @override
    async def async_press(self) -> None: ...
