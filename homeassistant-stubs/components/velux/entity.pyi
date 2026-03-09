from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable, Coroutine
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import Entity as Entity
from pyvlx import Node as Node
from typing import Any, ParamSpec

_LOGGER: Incomplete
P = ParamSpec('P')

def wrap_pyvlx_call_exceptions(func: Callable[P, Coroutine[Any, Any, None]]) -> Callable[P, Coroutine[Any, Any, None]]: ...

class VeluxEntity(Entity):
    _attr_should_poll: bool
    _attr_has_entity_name: bool
    update_callback: Callable[[Node], Awaitable[None]] | None
    _attr_available: bool
    _unavailable_logged: bool
    node: Incomplete
    _attr_unique_id: Incomplete
    unsubscribe: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, node: Node, config_entry_id: str) -> None: ...
    async def after_update_callback(self, _: Node) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
