from .const import DOMAIN as DOMAIN
from .coordinator import OneDriveConfigEntry as OneDriveConfigEntry, OneDriveUpdateCoordinator as OneDriveUpdateCoordinator
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory, UnitOfInformation as UnitOfInformation
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from onedrive_personal_sdk.models.items import DriveQuota as DriveQuota

PARALLEL_UPDATES: int

@dataclass(kw_only=True, frozen=True)
class OneDriveSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[DriveQuota], StateType]

DRIVE_STATE_ENTITIES: tuple[OneDriveSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: OneDriveConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class OneDriveDriveStateSensor(CoordinatorEntity[OneDriveUpdateCoordinator], SensorEntity):
    entity_description: OneDriveSensorEntityDescription
    _attr_has_entity_name: bool
    _attr_translation_key: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: OneDriveUpdateCoordinator, description: OneDriveSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> StateType: ...
    @property
    def available(self) -> bool: ...
