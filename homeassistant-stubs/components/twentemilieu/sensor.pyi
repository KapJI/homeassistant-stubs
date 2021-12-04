from .const import DOMAIN as DOMAIN
from datetime import date
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_ID as CONF_ID
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator
from twentemilieu import WasteType
from typing import Any

class TwenteMilieuSensorDescriptionMixin:
    waste_type: WasteType

class TwenteMilieuSensorDescription(SensorEntityDescription, TwenteMilieuSensorDescriptionMixin): ...

SENSORS: tuple[TwenteMilieuSensorDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class TwenteMilieuSensor(CoordinatorEntity, SensorEntity):
    entity_description: TwenteMilieuSensorDescription
    coordinator: DataUpdateCoordinator[dict[WasteType, Union[date, None]]]
    _attr_unique_id: Any
    _attr_device_info: Any
    def __init__(self, coordinator: DataUpdateCoordinator, description: TwenteMilieuSensorDescription, entry: ConfigEntry) -> None: ...
    @property
    def native_value(self) -> Union[date, None]: ...
