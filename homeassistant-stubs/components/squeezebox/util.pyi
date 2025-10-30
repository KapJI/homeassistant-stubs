from .const import DOMAIN as DOMAIN
from collections.abc import Awaitable, Callable as Callable
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from typing import Any

async def safe_library_call(method: Callable[..., Awaitable[Any]], *args: Any, translation_key: str, translation_placeholders: dict[str, Any] | None = None, **kwargs: Any) -> Any: ...
