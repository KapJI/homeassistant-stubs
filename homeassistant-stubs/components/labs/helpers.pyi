from .const import LABS_DATA as LABS_DATA
from .models import EventLabsUpdatedData as EventLabsUpdatedData
from collections.abc import Callable as Callable, Coroutine
from homeassistant.const import EVENT_LABS_UPDATED as EVENT_LABS_UPDATED
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.frame import report_usage as report_usage
from typing import Any

@callback
def async_is_preview_feature_enabled(hass: HomeAssistant, domain: str, preview_feature: str) -> bool: ...
@callback
def async_subscribe_preview_feature(hass: HomeAssistant, domain: str, preview_feature: str, listener: Callable[[EventLabsUpdatedData], Coroutine[Any, Any, None]]) -> Callable[[], None]: ...
@callback
def async_listen(hass: HomeAssistant, domain: str, preview_feature: str, listener: Callable[[], None]) -> Callable[[], None]: ...
async def async_update_preview_feature(hass: HomeAssistant, domain: str, preview_feature: str, enabled: bool) -> None: ...
