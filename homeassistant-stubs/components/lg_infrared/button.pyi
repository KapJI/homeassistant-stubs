from .const import CONF_DEVICE_TYPE as CONF_DEVICE_TYPE, CONF_INFRARED_ENTITY_ID as CONF_INFRARED_ENTITY_ID, LGDeviceType as LGDeviceType
from .entity import LgIrEntity as LgIrEntity
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.button import ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.components.infrared import InfraredEmitterConsumerEntity as InfraredEmitterConsumerEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from infrared_protocols.codes.lg.ac import LGACCode
from infrared_protocols.codes.lg.tv import LGTVCode
from typing import override

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class LgIrButtonEntityDescription(ButtonEntityDescription):
    command_code: LGTVCode | LGACCode

TV_BUTTON_DESCRIPTIONS: tuple[LgIrButtonEntityDescription, ...]
AC_BUTTON_DESCRIPTIONS: tuple[LgIrButtonEntityDescription, ...]
_DEVICE_BUTTONS: dict[LGDeviceType, tuple[LgIrButtonEntityDescription, ...]]
_DEVICE_NAMES: dict[LGDeviceType, str]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LgIrButton(LgIrEntity, InfraredEmitterConsumerEntity, ButtonEntity):
    entity_description: LgIrButtonEntityDescription
    _infrared_emitter_entity_id: Incomplete
    def __init__(self, entry: ConfigEntry, infrared_entity_id: str, description: LgIrButtonEntityDescription, device_name: str) -> None: ...
    @override
    async def async_press(self) -> None: ...
