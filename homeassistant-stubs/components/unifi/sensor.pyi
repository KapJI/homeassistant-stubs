from .controller import UniFiController as UniFiController
from .entity import HandlerT as HandlerT, UnifiEntity as UnifiEntity, UnifiEntityDescription as UnifiEntityDescription, async_client_device_info_fn as async_client_device_info_fn, async_device_available_fn as async_device_available_fn, async_device_device_info_fn as async_device_device_info_fn, async_wlan_available_fn as async_wlan_available_fn, async_wlan_device_info_fn as async_wlan_device_info_fn
from _typeshed import Incomplete
from aiounifi.interfaces.api_handlers import ItemEvent as ItemEvent
from aiounifi.models.api import ApiItemT
from aiounifi.models.client import Client
from aiounifi.models.device import Device
from aiounifi.models.wlan import Wlan
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass, UnitOfTemperature as UnitOfTemperature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory, UnitOfDataRate as UnitOfDataRate, UnitOfPower as UnitOfPower
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Generic

def async_bandwidth_sensor_allowed_fn(controller: UniFiController, obj_id: str) -> bool: ...
def async_uptime_sensor_allowed_fn(controller: UniFiController, obj_id: str) -> bool: ...
def async_client_rx_value_fn(controller: UniFiController, client: Client) -> float: ...
def async_client_tx_value_fn(controller: UniFiController, client: Client) -> float: ...
def async_client_uptime_value_fn(controller: UniFiController, client: Client) -> datetime: ...
def async_wlan_client_value_fn(controller: UniFiController, wlan: Wlan) -> int: ...
def async_device_uptime_value_fn(controller: UniFiController, device: Device) -> datetime: ...
def async_device_outlet_power_supported_fn(controller: UniFiController, obj_id: str) -> bool: ...
def async_device_outlet_supported_fn(controller: UniFiController, obj_id: str) -> bool: ...

@dataclass
class UnifiSensorEntityDescriptionMixin(Generic[HandlerT, ApiItemT]):
    value_fn: Callable[[UniFiController, ApiItemT], datetime | float | str | None]
    def __init__(self, value_fn) -> None: ...

@dataclass
class UnifiSensorEntityDescription(SensorEntityDescription, UnifiEntityDescription[HandlerT, ApiItemT], UnifiSensorEntityDescriptionMixin[HandlerT, ApiItemT]):
    def __init__(self, value_fn, allowed_fn, api_handler_fn, available_fn, device_info_fn, event_is_on, event_to_subscribe, name_fn, object_fn, should_poll, supported_fn, unique_id_fn, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement) -> None: ...

ENTITY_DESCRIPTIONS: tuple[UnifiSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class UnifiSensorEntity(UnifiEntity[HandlerT, ApiItemT], SensorEntity):
    entity_description: UnifiSensorEntityDescription[HandlerT, ApiItemT]
    _attr_native_value: Incomplete
    def async_update_state(self, event: ItemEvent, obj_id: str) -> None: ...
