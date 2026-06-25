from .coordinator import SkybellConfigEntry as SkybellConfigEntry
from .entity import SkybellEntity as SkybellEntity
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any, override

SWITCH_TYPES: tuple[SwitchEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: SkybellConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class SkybellSwitch(SkybellEntity, SwitchEntity):
    @override
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @override
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @property
    @override
    def is_on(self) -> bool: ...
