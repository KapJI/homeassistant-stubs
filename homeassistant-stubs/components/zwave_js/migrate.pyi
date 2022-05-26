from .const import DOMAIN as DOMAIN
from .discovery import ZwaveDiscoveryInfo as ZwaveDiscoveryInfo
from .helpers import get_unique_id as get_unique_id
from _typeshed import Incomplete
from homeassistant.const import STATE_UNAVAILABLE as STATE_UNAVAILABLE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceEntry as DeviceEntry
from homeassistant.helpers.entity_registry import EntityRegistry as EntityRegistry, RegistryEntry as RegistryEntry, async_entries_for_device as async_entries_for_device
from zwave_js_server.model.driver import Driver as Driver
from zwave_js_server.model.value import Value as ZwaveValue

_LOGGER: Incomplete

class ValueID:
    command_class: str
    endpoint: str
    property_: str
    property_key: Union[str, None]
    @staticmethod
    def from_unique_id(unique_id: str) -> ValueID: ...
    @staticmethod
    def from_string_id(value_id_str: str) -> ValueID: ...
    def is_same_value_different_endpoints(self, other: ValueID) -> bool: ...
    def __init__(self, command_class, endpoint, property_, property_key) -> None: ...

def async_migrate_old_entity(hass: HomeAssistant, ent_reg: EntityRegistry, registered_unique_ids: set[str], platform: str, device: DeviceEntry, unique_id: str) -> None: ...
def async_migrate_unique_id(ent_reg: EntityRegistry, platform: str, old_unique_id: str, new_unique_id: str) -> None: ...
def async_migrate_discovered_value(hass: HomeAssistant, ent_reg: EntityRegistry, registered_unique_ids: set[str], device: DeviceEntry, driver: Driver, disc_info: ZwaveDiscoveryInfo) -> None: ...
def get_old_value_ids(value: ZwaveValue) -> list[str]: ...
