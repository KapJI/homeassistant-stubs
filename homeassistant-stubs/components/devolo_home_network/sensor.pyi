from .const import CONNECTED_PLC_DEVICES as CONNECTED_PLC_DEVICES, CONNECTED_WIFI_CLIENTS as CONNECTED_WIFI_CLIENTS, DOMAIN as DOMAIN, NEIGHBORING_WIFI_NETWORKS as NEIGHBORING_WIFI_NETWORKS
from .entity import DevoloEntity as DevoloEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from devolo_plc_api.device import Device as Device
from homeassistant.components.sensor import SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from typing import Any

class DevoloSensorRequiredKeysMixin:
    value_func: Callable[[dict[str, Any]], int]
    def __init__(self, value_func) -> None: ...

class DevoloSensorEntityDescription(SensorEntityDescription, DevoloSensorRequiredKeysMixin):
    def __init__(self, value_func, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, unit_of_measurement, last_reset, native_unit_of_measurement, state_class) -> None: ...

SENSOR_TYPES: dict[str, DevoloSensorEntityDescription]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DevoloSensorEntity(DevoloEntity, SensorEntity):
    entity_description: Incomplete
    def __init__(self, coordinator: DataUpdateCoordinator, description: DevoloSensorEntityDescription, device: Device, device_name: str) -> None: ...
    @property
    def native_value(self) -> int: ...
