from .coordinator import BackupConfigEntry as BackupConfigEntry, BackupCoordinatorData as BackupCoordinatorData
from .entity import BackupManagerEntity as BackupManagerEntity
from .manager import BackupManagerState as BackupManagerState
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

@dataclass(kw_only=True, frozen=True)
class BackupSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[BackupCoordinatorData], str | datetime | None]

BACKUP_MANAGER_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: BackupConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class BackupManagerSensor(BackupManagerEntity, SensorEntity):
    entity_description: BackupSensorEntityDescription
    @property
    def native_value(self) -> str | datetime | None: ...
