from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import Entity as Entity
from mozart_api.mozart_client import MozartClient as MozartClient

class BangOlufsenBase:
    _client: Incomplete
    entry: Incomplete
    _host: Incomplete
    _name: Incomplete
    _unique_id: Incomplete
    _playback_metadata: Incomplete
    _playback_progress: Incomplete
    _playback_source: Incomplete
    _playback_state: Incomplete
    _source_change: Incomplete
    _volume: Incomplete
    def __init__(self, entry: ConfigEntry, client: MozartClient) -> None: ...

class BangOlufsenEntity(Entity, BangOlufsenBase):
    _attr_has_entity_name: bool
    _attr_device_info: Incomplete
    _attr_device_class: Incomplete
    _attr_entity_category: Incomplete
    _attr_should_poll: bool
    def __init__(self, entry: ConfigEntry, client: MozartClient) -> None: ...
    _attr_available: Incomplete
    async def _update_connection_state(self, connection_state: bool) -> None: ...
