from . import MastodonConfigEntry as MastodonConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

async def async_get_config_entry_diagnostics(hass: HomeAssistant, config_entry: MastodonConfigEntry) -> dict[str, Any]: ...
def get_diagnostics(config_entry: MastodonConfigEntry) -> tuple[dict, dict]: ...