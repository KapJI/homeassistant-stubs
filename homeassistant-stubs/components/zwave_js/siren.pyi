from .const import DATA_CLIENT as DATA_CLIENT, DOMAIN as DOMAIN
from .discovery import ZwaveDiscoveryInfo as ZwaveDiscoveryInfo
from .entity import ZWaveBaseEntity as ZWaveBaseEntity
from _typeshed import Incomplete
from homeassistant.components.siren import SirenEntity as SirenEntity, SirenEntityFeature as SirenEntityFeature
from homeassistant.components.siren.const import ATTR_TONE as ATTR_TONE, ATTR_VOLUME_LEVEL as ATTR_VOLUME_LEVEL
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any
from zwave_js_server.client import Client as ZwaveClient

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ZwaveSirenEntity(ZWaveBaseEntity, SirenEntity):
    _attr_available_tones: Incomplete
    _attr_supported_features: Incomplete
    def __init__(self, config_entry: ConfigEntry, client: ZwaveClient, info: ZwaveDiscoveryInfo) -> None: ...
    @property
    def is_on(self) -> Union[bool, None]: ...
    async def async_set_value(self, new_value: int, options: Union[dict[str, Any], None] = ...) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
