from . import VeluxConfigEntry as VeluxConfigEntry
from .const import DOMAIN as DOMAIN
from .entity import wrap_pyvlx_call_exceptions as wrap_pyvlx_call_exceptions
from _typeshed import Incomplete
from homeassistant.components.scene import Scene as Scene
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pyvlx import Scene as PyVLXScene
from typing import Any

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, config_entry: VeluxConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class VeluxScene(Scene):
    _attr_has_entity_name: bool
    scene: Incomplete
    _attr_unique_id: Incomplete
    _attr_name: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, config_entry_id: str, scene: PyVLXScene) -> None: ...
    @wrap_pyvlx_call_exceptions
    async def async_activate(self, **kwargs: Any) -> None: ...
