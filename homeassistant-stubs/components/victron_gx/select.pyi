from .entity import VictronBaseEntity as VictronBaseEntity
from .hub import VictronGxConfigEntry as VictronGxConfigEntry
from _typeshed import Incomplete
from homeassistant.components.select import SelectEntity as SelectEntity
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any
from victron_mqtt import Device as VictronVenusDevice, WritableMetric as VictronVenusWritableMetric

_LOGGER: Incomplete
PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, config_entry: VictronGxConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class VictronSelect(VictronBaseEntity, SelectEntity):
    _attr_options: Incomplete
    _attr_current_option: Incomplete
    def __init__(self, device: VictronVenusDevice, metric: VictronVenusWritableMetric, device_info: DeviceInfo, installation_id: str) -> None: ...
    @callback
    def _on_update_cb(self, value: Any) -> None: ...
    async def async_select_option(self, option: str) -> None: ...
    @staticmethod
    def _normalize_value(value: Any) -> Any: ...
