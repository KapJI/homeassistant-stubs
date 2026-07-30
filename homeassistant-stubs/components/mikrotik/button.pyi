from .const import MIKROTIK_SERVICES as MIKROTIK_SERVICES
from .coordinator import MikrotikConfigEntry as MikrotikConfigEntry, mikrotik_config_entry_errors as mikrotik_config_entry_errors
from .entity import MikrotikEntity as MikrotikEntity
from _typeshed import Incomplete
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import override

PARALLEL_UPDATES: int
BUTTON_TYPES: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: MikrotikConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class MikrotikButtonEntity(MikrotikEntity, ButtonEntity):
    @override
    async def async_press(self) -> None: ...
