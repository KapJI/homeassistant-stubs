from . import BrotherDataUpdateCoordinator as BrotherDataUpdateCoordinator
from .const import ATTRS_MAP as ATTRS_MAP, ATTR_COUNTER as ATTR_COUNTER, ATTR_ENABLED as ATTR_ENABLED, ATTR_LABEL as ATTR_LABEL, ATTR_MANUFACTURER as ATTR_MANUFACTURER, ATTR_REMAINING_PAGES as ATTR_REMAINING_PAGES, ATTR_UNIT as ATTR_UNIT, ATTR_UPTIME as ATTR_UPTIME, DATA_CONFIG_ENTRY as DATA_CONFIG_ENTRY, DOMAIN as DOMAIN, SENSOR_TYPES as SENSOR_TYPES
from homeassistant.components.sensor import ATTR_STATE_CLASS as ATTR_STATE_CLASS, SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_DEVICE_CLASS as ATTR_DEVICE_CLASS, ATTR_ICON as ATTR_ICON
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class BrotherPrinterSensor(CoordinatorEntity, SensorEntity):
    _attrs: Any
    _attr_device_class: Any
    _attr_device_info: Any
    _attr_entity_registry_enabled_default: Any
    _attr_icon: Any
    _attr_name: Any
    _attr_state_class: Any
    _attr_unique_id: Any
    _attr_unit_of_measurement: Any
    kind: Any
    def __init__(self, coordinator: BrotherDataUpdateCoordinator, kind: str, device_info: DeviceInfo) -> None: ...
    @property
    def state(self) -> Any: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
