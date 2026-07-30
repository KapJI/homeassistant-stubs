from . import AquaLogicConfigEntry as AquaLogicConfigEntry, AquaLogicProcessor as AquaLogicProcessor
from .const import UPDATE_TOPIC as UPDATE_TOPIC
from _typeshed import Incomplete
from aqualogic.core import States
from homeassistant.components.switch import SwitchEntity as SwitchEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any, override

_SWITCH_MAP: dict[str, tuple[str, States]]

async def async_setup_entry(hass: HomeAssistant, entry: AquaLogicConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class AquaLogicSwitch(SwitchEntity):
    _attr_should_poll: bool
    _processor: Incomplete
    _state_name: Incomplete
    _attr_name: Incomplete
    def __init__(self, processor: AquaLogicProcessor, switch_type: str) -> None: ...
    @property
    @override
    def is_on(self) -> bool: ...
    @override
    def turn_on(self, **kwargs: Any) -> None: ...
    @override
    def turn_off(self, **kwargs: Any) -> None: ...
    @override
    async def async_added_to_hass(self) -> None: ...
