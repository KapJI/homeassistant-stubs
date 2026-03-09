from . import VeluxConfigEntry as VeluxConfigEntry
from .entity import VeluxEntity as VeluxEntity, wrap_pyvlx_call_exceptions as wrap_pyvlx_call_exceptions
from _typeshed import Incomplete
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ColorMode as ColorMode, LightEntity as LightEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pyvlx import DimmableDevice as DimmableDevice
from typing import Any

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, config_entry: VeluxConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class VeluxOnOffLight(VeluxEntity, LightEntity):
    _attr_supported_color_modes: Incomplete
    _attr_color_mode: Incomplete
    _attr_name: Incomplete
    node: DimmableDevice
    @property
    def is_on(self) -> bool: ...
    @wrap_pyvlx_call_exceptions
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @wrap_pyvlx_call_exceptions
    async def async_turn_off(self, **kwargs: Any) -> None: ...

class VeluxDimmableLight(VeluxOnOffLight):
    _attr_supported_color_modes: Incomplete
    _attr_color_mode: Incomplete
    _attr_name: Incomplete
    @property
    def brightness(self) -> int: ...
    @wrap_pyvlx_call_exceptions
    async def async_turn_on(self, **kwargs: Any) -> None: ...
