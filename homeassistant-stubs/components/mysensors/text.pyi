from . import setup_mysensors_platform as setup_mysensors_platform
from .const import DiscoveryInfo as DiscoveryInfo, MYSENSORS_DISCOVERY as MYSENSORS_DISCOVERY
from .entity import MySensorsChildEntity as MySensorsChildEntity
from .models import MySensorsConfigEntry as MySensorsConfigEntry
from homeassistant.components.text import TextEntity as TextEntity
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import override

async def async_setup_entry(hass: HomeAssistant, config_entry: MySensorsConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class MySensorsText(MySensorsChildEntity, TextEntity):
    _attr_native_max: int
    @property
    @override
    def native_value(self) -> str | None: ...
    @override
    async def async_set_value(self, value: str) -> None: ...
