import abc
from .const import CONF_CONNECTIONS as CONF_CONNECTIONS, CONF_COORDINATOR as CONF_COORDINATOR, DOMAIN as DOMAIN, LOGGER as LOGGER, PLATFORMS as PLATFORMS
from .coordinator import FritzboxDataUpdateCoordinator as FritzboxDataUpdateCoordinator
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.device_registry import DeviceEntry as DeviceEntry, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.entity_registry import RegistryEntry as RegistryEntry, async_migrate_entries as async_migrate_entries
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from pyfritzhome import FritzhomeDevice as FritzhomeDevice
from pyfritzhome.devicetypes.fritzhomeentitybase import FritzhomeEntityBase as FritzhomeEntityBase

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_remove_config_entry_device(hass: HomeAssistant, entry: ConfigEntry, device: DeviceEntry) -> bool: ...

class FritzBoxEntity(CoordinatorEntity[FritzboxDataUpdateCoordinator], ABC, metaclass=abc.ABCMeta):
    ain: Incomplete
    _attr_has_entity_name: bool
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    _attr_name: Incomplete
    def __init__(self, coordinator: FritzboxDataUpdateCoordinator, ain: str, entity_description: EntityDescription | None = ...) -> None: ...
    @property
    @abstractmethod
    def data(self) -> FritzhomeEntityBase: ...

class FritzBoxDeviceEntity(FritzBoxEntity):
    @property
    def available(self) -> bool: ...
    @property
    def data(self) -> FritzhomeDevice: ...
    @property
    def device_info(self) -> DeviceInfo: ...
