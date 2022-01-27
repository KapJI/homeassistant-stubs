from . import KrakenData as KrakenData
from .const import CONF_TRACKED_ASSET_PAIRS as CONF_TRACKED_ASSET_PAIRS, DISPATCH_CONFIG_UPDATED as DISPATCH_CONFIG_UPDATED, DOMAIN as DOMAIN, KrakenResponse as KrakenResponse, KrakenSensorEntityDescription as KrakenSensorEntityDescription, SENSOR_TYPES as SENSOR_TYPES
from homeassistant.components.sensor import SensorEntity as SensorEntity, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import device_registry as device_registry
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any, Optional

_LOGGER: Any

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class KrakenSensor(CoordinatorEntity[Optional[KrakenResponse]], SensorEntity):
    entity_description: KrakenSensorEntityDescription
    tracked_asset_pair_wsname: Any
    _target_asset: Any
    _attr_native_unit_of_measurement: Any
    _device_name: Any
    _attr_name: Any
    _attr_unique_id: Any
    _received_data_at_least_once: bool
    _available: bool
    _attr_state_class: Any
    _attr_device_info: Any
    def __init__(self, kraken_data: KrakenData, tracked_asset_pair: str, description: KrakenSensorEntityDescription) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    def _handle_coordinator_update(self) -> None: ...
    _attr_native_value: Any
    def _update_internal_state(self) -> None: ...
    @property
    def icon(self) -> str: ...
    @property
    def available(self) -> bool: ...

def create_device_name(tracked_asset_pair: str) -> str: ...
