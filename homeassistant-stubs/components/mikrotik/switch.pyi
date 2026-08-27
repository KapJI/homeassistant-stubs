from .coordinator import MikrotikConfigEntry as MikrotikConfigEntry, mikrotik_config_entry_errors as mikrotik_config_entry_errors
from .entity import MikrotikDeviceEntity as MikrotikDeviceEntity
from _typeshed import Incomplete
from homeassistant.components.switch import SwitchDeviceClass as SwitchDeviceClass, SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any, Final, override

PARALLEL_UPDATES: int
SENSORS: Final[Incomplete]

async def async_setup_entry(hass: HomeAssistant, entry: MikrotikConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class MikrotikSwitchEntity(MikrotikDeviceEntity, SwitchEntity):
    @property
    @override
    def is_on(self) -> bool | None: ...
    async def _set_state(self, action: str) -> None: ...
    @override
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @override
    async def async_turn_off(self, **kwargs: Any) -> None: ...
