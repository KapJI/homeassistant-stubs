from . import SynoApi as SynoApi
from .coordinator import SynologyDSMCentralUpdateCoordinator as SynologyDSMCentralUpdateCoordinator, SynologyDSMConfigEntry as SynologyDSMConfigEntry
from .entity import SynologyDSMBaseEntity as SynologyDSMBaseEntity, SynologyDSMDeviceEntity as SynologyDSMDeviceEntity, SynologyDSMEntityDescription as SynologyDSMEntityDescription
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import CONF_DISKS as CONF_DISKS, EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

@dataclass(frozen=True, kw_only=True)
class SynologyDSMBinarySensorEntityDescription(BinarySensorEntityDescription, SynologyDSMEntityDescription): ...

SECURITY_BINARY_SENSORS: tuple[SynologyDSMBinarySensorEntityDescription, ...]
STORAGE_DISK_BINARY_SENSORS: tuple[SynologyDSMBinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: SynologyDSMConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class SynoDSMBinarySensor(SynologyDSMBaseEntity[SynologyDSMCentralUpdateCoordinator], BinarySensorEntity):
    entity_description: SynologyDSMBinarySensorEntityDescription
    def __init__(self, api: SynoApi, coordinator: SynologyDSMCentralUpdateCoordinator, description: SynologyDSMBinarySensorEntityDescription) -> None: ...

class SynoDSMSecurityBinarySensor(SynoDSMBinarySensor):
    @property
    def is_on(self) -> bool: ...
    @property
    def available(self) -> bool: ...
    @property
    def extra_state_attributes(self) -> dict[str, str]: ...

class SynoDSMStorageBinarySensor(SynologyDSMDeviceEntity, SynoDSMBinarySensor):
    entity_description: SynologyDSMBinarySensorEntityDescription
    def __init__(self, api: SynoApi, coordinator: SynologyDSMCentralUpdateCoordinator, description: SynologyDSMBinarySensorEntityDescription, device_id: str | None = None) -> None: ...
    @property
    def is_on(self) -> bool: ...
