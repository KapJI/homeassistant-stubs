from . import KrakenData as KrakenData
from .const import CONF_TRACKED_ASSET_PAIRS as CONF_TRACKED_ASSET_PAIRS, DISPATCH_CONFIG_UPDATED as DISPATCH_CONFIG_UPDATED, DOMAIN as DOMAIN, SENSOR_TYPES as SENSOR_TYPES, SensorType as SensorType
from homeassistant.components.sensor import SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import device_registry as device_registry
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

_LOGGER: Any

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class KrakenSensor(CoordinatorEntity, SensorEntity):
    tracked_asset_pair_wsname: Any
    _source_asset: Any
    _target_asset: Any
    _sensor_type: Any
    _enabled_by_default: Any
    _unit_of_measurement: Any
    _device_name: Any
    _name: Any
    _received_data_at_least_once: bool
    _available: bool
    _state: Any
    def __init__(self, kraken_data: KrakenData, tracked_asset_pair: str, sensor_type: SensorType) -> None: ...
    @property
    def entity_registry_enabled_default(self) -> bool: ...
    @property
    def name(self) -> str: ...
    @property
    def unique_id(self) -> str: ...
    @property
    def state(self) -> StateType: ...
    async def async_added_to_hass(self) -> None: ...
    def _handle_coordinator_update(self) -> None: ...
    def _update_internal_state(self) -> None: ...
    @property
    def icon(self) -> str: ...
    @property
    def unit_of_measurement(self) -> Union[str, None]: ...
    @property
    def available(self) -> bool: ...
    @property
    def device_info(self) -> DeviceInfo: ...

def create_device_name(tracked_asset_pair: str) -> str: ...
