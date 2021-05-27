from . import SynoApi as SynoApi, SynologyDSMBaseEntity as SynologyDSMBaseEntity, SynologyDSMDeviceEntity as SynologyDSMDeviceEntity
from .const import COORDINATOR_CENTRAL as COORDINATOR_CENTRAL, DOMAIN as DOMAIN, SECURITY_BINARY_SENSORS as SECURITY_BINARY_SENSORS, STORAGE_DISK_BINARY_SENSORS as STORAGE_DISK_BINARY_SENSORS, SYNO_API as SYNO_API, UPGRADE_BINARY_SENSORS as UPGRADE_BINARY_SENSORS
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_DISKS as CONF_DISKS
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SynoDSMSecurityBinarySensor(SynologyDSMBaseEntity, BinarySensorEntity):
    @property
    def is_on(self) -> bool: ...
    @property
    def available(self) -> bool: ...
    @property
    def extra_state_attributes(self) -> dict[str, str]: ...

class SynoDSMStorageBinarySensor(SynologyDSMDeviceEntity, BinarySensorEntity):
    @property
    def is_on(self) -> bool: ...

class SynoDSMUpgradeBinarySensor(SynologyDSMBaseEntity, BinarySensorEntity):
    @property
    def is_on(self) -> bool: ...
    @property
    def available(self) -> bool: ...
