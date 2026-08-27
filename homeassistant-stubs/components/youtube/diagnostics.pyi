from .const import ATTR_DESCRIPTION as ATTR_DESCRIPTION, ATTR_LATEST_SHORT as ATTR_LATEST_SHORT, ATTR_LATEST_VIDEO as ATTR_LATEST_VIDEO, ATTR_LATEST_VIDEO_NON_SHORT as ATTR_LATEST_VIDEO_NON_SHORT
from .coordinator import YouTubeConfigEntry as YouTubeConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: YouTubeConfigEntry) -> dict[str, Any]: ...
