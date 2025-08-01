import pypck
from .const import CONF_CLIMATES as CONF_CLIMATES, CONF_DOMAIN_DATA as CONF_DOMAIN_DATA, CONF_HARDWARE_SERIAL as CONF_HARDWARE_SERIAL, CONF_HARDWARE_TYPE as CONF_HARDWARE_TYPE, CONF_SCENES as CONF_SCENES, CONF_SOFTWARE_SERIAL as CONF_SOFTWARE_SERIAL, DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Iterable
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_ADDRESS as CONF_ADDRESS, CONF_BINARY_SENSORS as CONF_BINARY_SENSORS, CONF_COVERS as CONF_COVERS, CONF_DEVICES as CONF_DEVICES, CONF_DOMAIN as CONF_DOMAIN, CONF_ENTITIES as CONF_ENTITIES, CONF_LIGHTS as CONF_LIGHTS, CONF_NAME as CONF_NAME, CONF_SENSORS as CONF_SENSORS, CONF_SWITCHES as CONF_SWITCHES
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.typing import ConfigType as ConfigType
from pypck.connection import PchkConnectionManager as PchkConnectionManager

@dataclass
class LcnRuntimeData:
    connection: PchkConnectionManager
    device_connections: dict[str, DeviceConnectionType]
    add_entities_callbacks: dict[str, Callable[[Iterable[ConfigType]], None]]
type LcnConfigEntry = ConfigEntry[LcnRuntimeData]
type AddressType = tuple[int, int, bool]
type DeviceConnectionType = pypck.module.ModuleConnection | pypck.module.GroupConnection
type InputType = type[pypck.inputs.Input]

PATTERN_ADDRESS: Incomplete
DOMAIN_LOOKUP: Incomplete

def get_device_connection(hass: HomeAssistant, address: AddressType, config_entry: LcnConfigEntry) -> DeviceConnectionType: ...
def get_resource(domain_name: str, domain_data: ConfigType) -> str: ...
def generate_unique_id(entry_id: str, address: AddressType, resource: str | None = None) -> str: ...
def purge_entity_registry(hass: HomeAssistant, entry_id: str, imported_entry_data: ConfigType) -> None: ...
def purge_device_registry(hass: HomeAssistant, entry_id: str, imported_entry_data: ConfigType) -> None: ...
def register_lcn_host_device(hass: HomeAssistant, config_entry: LcnConfigEntry) -> None: ...
def register_lcn_address_devices(hass: HomeAssistant, config_entry: LcnConfigEntry) -> None: ...
async def async_update_device_config(device_connection: DeviceConnectionType, device_config: ConfigType) -> None: ...
async def async_update_config_entry(hass: HomeAssistant, config_entry: LcnConfigEntry) -> None: ...
def get_device_config(address: AddressType, config_entry: ConfigEntry) -> ConfigType | None: ...
def is_states_string(states_string: str) -> list[str]: ...
