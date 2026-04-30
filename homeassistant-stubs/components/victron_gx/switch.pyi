from .binary_sensor import VictronBinarySensor as VictronBinarySensor
from .const import BINARY_SENSOR_OFF_ID as BINARY_SENSOR_OFF_ID, BINARY_SENSOR_ON_ID as BINARY_SENSOR_ON_ID
from .entity import VictronBaseEntity as VictronBaseEntity
from .hub import VictronGxConfigEntry as VictronGxConfigEntry
from _typeshed import Incomplete
from homeassistant.components.switch import SwitchEntity as SwitchEntity
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any
from victron_mqtt import Device as VictronVenusDevice, WritableMetric as VictronVenusWritableMetric

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, config_entry: VictronGxConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class VictronSwitch(VictronBaseEntity, SwitchEntity):
    _attr_is_on: Incomplete
    def __init__(self, device: VictronVenusDevice, metric: VictronVenusWritableMetric, device_info: DeviceInfo, installation_id: str) -> None: ...
    @callback
    def _on_update_cb(self, value: Any) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
