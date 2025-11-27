from .const import ATTR_VALUE as ATTR_VALUE, DOMAIN as DOMAIN
from .entity import NewZwaveDiscoveryInfo as NewZwaveDiscoveryInfo, ZWaveBaseEntity as ZWaveBaseEntity
from .models import NewZWaveDiscoverySchema as NewZWaveDiscoverySchema, ZWaveValueDiscoverySchema as ZWaveValueDiscoverySchema, ZwaveJSConfigEntry as ZwaveJSConfigEntry
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.event import EventEntity as EventEntity, EventEntityDescription as EventEntityDescription
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from zwave_js_server.model.driver import Driver as Driver
from zwave_js_server.model.value import Value as Value, ValueNotification as ValueNotification

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class ValueNotificationZWaveJSEntityDescription(EventEntityDescription): ...

async def async_setup_entry(hass: HomeAssistant, config_entry: ZwaveJSConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...
def _cc_and_label(value: Value) -> str: ...

class ZwaveEventEntity(ZWaveBaseEntity, EventEntity):
    states: dict[int, str]
    _attr_event_types: Incomplete
    _attr_name: Incomplete
    def __init__(self, config_entry: ZwaveJSConfigEntry, driver: Driver, info: NewZwaveDiscoveryInfo) -> None: ...
    @callback
    def _async_handle_event(self, value_notification: ValueNotification) -> None: ...
    async def async_added_to_hass(self) -> None: ...

DISCOVERY_SCHEMAS: list[NewZWaveDiscoverySchema]
