from . import BrotherDataUpdateCoordinator as BrotherDataUpdateCoordinator
from .const import ATTRS_MAP as ATTRS_MAP, ATTR_COUNTER as ATTR_COUNTER, ATTR_MANUFACTURER as ATTR_MANUFACTURER, ATTR_REMAINING_PAGES as ATTR_REMAINING_PAGES, ATTR_UPTIME as ATTR_UPTIME, DATA_CONFIG_ENTRY as DATA_CONFIG_ENTRY, DOMAIN as DOMAIN, SENSOR_TYPES as SENSOR_TYPES
from homeassistant.components.sensor import SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class BrotherPrinterSensor(CoordinatorEntity, SensorEntity):
    _attrs: Any
    _attr_device_info: Any
    _attr_name: Any
    _attr_unique_id: Any
    entity_description: Any
    def __init__(self, coordinator: BrotherDataUpdateCoordinator, description: SensorEntityDescription, device_info: DeviceInfo) -> None: ...
    @property
    def state(self) -> StateType: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
