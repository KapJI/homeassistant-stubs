from .coordinator import MikrotikConfigEntry as MikrotikConfigEntry, mikrotik_config_entry_errors as mikrotik_config_entry_errors
from .entity import MikrotikDeviceEntity as MikrotikDeviceEntity
from _typeshed import Incomplete
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Final, override

PARALLEL_UPDATES: int
OPTION_TO_KEY: Final[Incomplete]
KEY_TO_OPTION: Final[Incomplete]
SELECTS: Final[Incomplete]

async def async_setup_entry(hass: HomeAssistant, entry: MikrotikConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class MikrotikSelectEntity(MikrotikDeviceEntity, SelectEntity):
    @property
    @override
    def current_option(self) -> str | None: ...
    @override
    async def async_select_option(self, option: str) -> None: ...
