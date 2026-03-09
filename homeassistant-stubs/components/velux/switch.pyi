from . import VeluxConfigEntry as VeluxConfigEntry
from .entity import VeluxEntity as VeluxEntity, wrap_pyvlx_call_exceptions as wrap_pyvlx_call_exceptions
from _typeshed import Incomplete
from homeassistant.components.switch import SwitchEntity as SwitchEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pyvlx import OnOffSwitch
from typing import Any

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, config_entry: VeluxConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class VeluxOnOffSwitch(VeluxEntity, SwitchEntity):
    _attr_name: Incomplete
    node: OnOffSwitch
    @property
    def is_on(self) -> bool: ...
    @wrap_pyvlx_call_exceptions
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @wrap_pyvlx_call_exceptions
    async def async_turn_off(self, **kwargs: Any) -> None: ...
