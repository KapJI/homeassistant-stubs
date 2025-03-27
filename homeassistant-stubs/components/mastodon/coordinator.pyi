from .const import LOGGER as LOGGER
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from mastodon import Mastodon as Mastodon
from mastodon.Mastodon import Account, Instance as Instance, InstanceV2 as InstanceV2

@dataclass
class MastodonData:
    client: Mastodon
    instance: InstanceV2 | Instance
    account: Account
    coordinator: MastodonCoordinator
type MastodonConfigEntry = ConfigEntry[MastodonData]

class MastodonCoordinator(DataUpdateCoordinator[Account]):
    config_entry: MastodonConfigEntry
    client: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: MastodonConfigEntry, client: Mastodon) -> None: ...
    async def _async_update_data(self) -> Account: ...
