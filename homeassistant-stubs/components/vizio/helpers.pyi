from .const import DOMAIN as DOMAIN
from collections.abc import Coroutine
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from typing import Any

async def async_device_command[T](coro: Coroutine[Any, Any, T]) -> T: ...
