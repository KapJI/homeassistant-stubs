from . import SynoApi as SynoApi, SynologyDSMBaseEntity as SynologyDSMBaseEntity, SynologyDSMDeviceEntity as SynologyDSMDeviceEntity
from .const import COORDINATOR_CENTRAL as COORDINATOR_CENTRAL, DOMAIN as DOMAIN, SECURITY_BINARY_SENSORS as SECURITY_BINARY_SENSORS, STORAGE_DISK_BINARY_SENSORS as STORAGE_DISK_BINARY_SENSORS, SYNO_API as SYNO_API, SynologyDSMBinarySensorEntityDescription as SynologyDSMBinarySensorEntityDescription, UPGRADE_BINARY_SENSORS as UPGRADE_BINARY_SENSORS
from collections.abc import Mapping
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_DISKS as CONF_DISKS
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SynoDSMBinarySensor(SynologyDSMBaseEntity, BinarySensorEntity):
    entity_description: SynologyDSMBinarySensorEntityDescription
    def __init__(self, api: SynoApi, coordinator: DataUpdateCoordinator[dict[str, dict[str, Any]]], description: SynologyDSMBinarySensorEntityDescription) -> None: ...

class SynoDSMSecurityBinarySensor(SynoDSMBinarySensor):
    @property
    def is_on(self) -> bool: ...
    @property
    def available(self) -> bool: ...
    @property
    def extra_state_attributes(self) -> dict[str, str]: ...

class SynoDSMStorageBinarySensor(SynologyDSMDeviceEntity, SynoDSMBinarySensor):
    entity_description: SynologyDSMBinarySensorEntityDescription
    def __init__(self, api: SynoApi, coordinator: DataUpdateCoordinator[dict[str, dict[str, Any]]], description: SynologyDSMBinarySensorEntityDescription, device_id: Union[str, None] = ...) -> None: ...
    @property
    def is_on(self) -> bool: ...

class SynoDSMUpgradeBinarySensor(SynoDSMBinarySensor):
    @property
    def is_on(self) -> bool: ...
    @property
    def available(self) -> bool: ...
    @property
    def extra_state_attributes(self) -> Union[Mapping[str, Any], None]: ...
