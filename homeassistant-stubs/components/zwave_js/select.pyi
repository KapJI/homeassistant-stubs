from .const import DATA_CLIENT as DATA_CLIENT, DOMAIN as DOMAIN
from .discovery import ZwaveDiscoveryInfo as ZwaveDiscoveryInfo
from .entity import ZWaveBaseEntity as ZWaveBaseEntity
from homeassistant.components.select import SelectEntity as SelectEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any
from zwave_js_server.client import Client as ZwaveClient

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ZwaveSelectEntity(ZWaveBaseEntity, SelectEntity):
    _attr_entity_category: Any
    _attr_name: Any
    _attr_options: Any
    def __init__(self, config_entry: ConfigEntry, client: ZwaveClient, info: ZwaveDiscoveryInfo) -> None: ...
    @property
    def current_option(self) -> Union[str, None]: ...
    async def async_select_option(self, option: Union[str, int]) -> None: ...

class ZwaveDefaultToneSelectEntity(ZWaveBaseEntity, SelectEntity):
    _attr_entity_category: Any
    _tones_value: Any
    _attr_name: Any
    def __init__(self, config_entry: ConfigEntry, client: ZwaveClient, info: ZwaveDiscoveryInfo) -> None: ...
    @property
    def options(self) -> list[str]: ...
    @property
    def current_option(self) -> Union[str, None]: ...
    async def async_select_option(self, option: Union[str, int]) -> None: ...

class ZwaveMultilevelSwitchSelectEntity(ZWaveBaseEntity, SelectEntity):
    _target_value: Any
    _lookup_map: Any
    _attr_options: Any
    def __init__(self, config_entry: ConfigEntry, client: ZwaveClient, info: ZwaveDiscoveryInfo) -> None: ...
    @property
    def current_option(self) -> Union[str, None]: ...
    async def async_select_option(self, option: str) -> None: ...
