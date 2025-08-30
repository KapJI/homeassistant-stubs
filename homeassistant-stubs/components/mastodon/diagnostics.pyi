from .coordinator import MastodonConfigEntry as MastodonConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from mastodon.Mastodon import Account as Account, Instance as Instance, InstanceV2 as InstanceV2
from typing import Any

async def async_get_config_entry_diagnostics(hass: HomeAssistant, config_entry: MastodonConfigEntry) -> dict[str, Any]: ...
def get_diagnostics(config_entry: MastodonConfigEntry) -> tuple[InstanceV2 | Instance, Account]: ...
