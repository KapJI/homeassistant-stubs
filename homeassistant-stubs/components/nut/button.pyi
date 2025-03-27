from . import NutConfigEntry as NutConfigEntry
from .entity import NUTBaseEntity as NUTBaseEntity
from _typeshed import Incomplete
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

_LOGGER: Incomplete
PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, config_entry: NutConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class NUTButton(NUTBaseEntity, ButtonEntity):
    async def async_press(self) -> None: ...
