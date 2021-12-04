from .const import CONNECTED_PLC_DEVICES as CONNECTED_PLC_DEVICES, CONNECTED_WIFI_CLIENTS as CONNECTED_WIFI_CLIENTS, DOMAIN as DOMAIN, NEIGHBORING_WIFI_NETWORKS as NEIGHBORING_WIFI_NETWORKS
from .entity import DevoloEntity as DevoloEntity
from collections.abc import Callable as Callable
from devolo_plc_api.device import Device as Device
from homeassistant.components.sensor import STATE_CLASS_MEASUREMENT as STATE_CLASS_MEASUREMENT, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ENTITY_CATEGORY_DIAGNOSTIC as ENTITY_CATEGORY_DIAGNOSTIC
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from typing import Any

class DevoloSensorRequiredKeysMixin:
    value_func: Callable[[dict[str, Any]], int]

class DevoloSensorEntityDescription(SensorEntityDescription, DevoloSensorRequiredKeysMixin): ...

SENSOR_TYPES: dict[str, DevoloSensorEntityDescription]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DevoloSensorEntity(DevoloEntity, SensorEntity):
    entity_description: Any
    def __init__(self, coordinator: DataUpdateCoordinator, description: DevoloSensorEntityDescription, device: Device, device_name: str) -> None: ...
    @property
    def native_value(self) -> int: ...
