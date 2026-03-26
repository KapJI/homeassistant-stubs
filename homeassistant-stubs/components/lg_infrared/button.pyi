from .const import CONF_DEVICE_TYPE as CONF_DEVICE_TYPE, CONF_INFRARED_ENTITY_ID as CONF_INFRARED_ENTITY_ID, LGDeviceType as LGDeviceType
from .entity import LgIrEntity as LgIrEntity
from dataclasses import dataclass
from homeassistant.components.button import ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from infrared_protocols.codes.lg.tv import LGTVCode

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class LgIrButtonEntityDescription(ButtonEntityDescription):
    command_code: LGTVCode

TV_BUTTON_DESCRIPTIONS: tuple[LgIrButtonEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LgIrButton(LgIrEntity, ButtonEntity):
    entity_description: LgIrButtonEntityDescription
    def __init__(self, entry: ConfigEntry, infrared_entity_id: str, description: LgIrButtonEntityDescription) -> None: ...
    async def async_press(self) -> None: ...
