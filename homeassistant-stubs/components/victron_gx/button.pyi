from .entity import VictronBaseEntity as VictronBaseEntity
from .hub import VictronGxConfigEntry as VictronGxConfigEntry
from _typeshed import Incomplete
from homeassistant.components.button import ButtonEntity as ButtonEntity
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any, override

_LOGGER: Incomplete
PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, config_entry: VictronGxConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class VictronButton(VictronBaseEntity, ButtonEntity):
    @callback
    @override
    def _on_update_cb(self, _value: Any) -> None: ...
    @override
    async def async_press(self) -> None: ...
