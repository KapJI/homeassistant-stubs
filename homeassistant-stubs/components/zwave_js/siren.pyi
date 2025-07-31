from .const import DOMAIN as DOMAIN
from .discovery import ZwaveDiscoveryInfo as ZwaveDiscoveryInfo
from .entity import ZWaveBaseEntity as ZWaveBaseEntity
from .models import ZwaveJSConfigEntry as ZwaveJSConfigEntry
from _typeshed import Incomplete
from homeassistant.components.siren import ATTR_TONE as ATTR_TONE, ATTR_VOLUME_LEVEL as ATTR_VOLUME_LEVEL, SirenEntity as SirenEntity, SirenEntityFeature as SirenEntityFeature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any
from zwave_js_server.model.driver import Driver as Driver

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, config_entry: ZwaveJSConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class ZwaveSirenEntity(ZWaveBaseEntity, SirenEntity):
    _attr_available_tones: Incomplete
    _attr_supported_features: Incomplete
    _attr_name: Incomplete
    def __init__(self, config_entry: ZwaveJSConfigEntry, driver: Driver, info: ZwaveDiscoveryInfo) -> None: ...
    @property
    def is_on(self) -> bool | None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
