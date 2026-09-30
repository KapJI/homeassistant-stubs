from .const import ATTR_DEVICES as ATTR_DEVICES, DOMAIN as DOMAIN, DevId as DevId, DiscoveryInfo as DiscoveryInfo, PLATFORMS as PLATFORMS, SensorType as SensorType
from .entity import MySensorsChildEntity as MySensorsChildEntity
from .gateway import finish_setup as finish_setup, gw_stop as gw_stop, setup_gateway as setup_gateway
from .helpers import remove_node_dev_ids as remove_node_dev_ids
from .models import MySensorsConfigEntry as MySensorsConfigEntry, MySensorsData as MySensorsData
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import AnyDeviceEntry as AnyDeviceEntry, DeviceEntry as DeviceEntry
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: MySensorsConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: MySensorsConfigEntry) -> bool: ...
async def async_remove_config_entry_device(hass: HomeAssistant, config_entry: MySensorsConfigEntry, device_entry: AnyDeviceEntry) -> bool: ...
@callback
def setup_mysensors_platform(config_entry: MySensorsConfigEntry, domain: Platform, discovery_info: DiscoveryInfo, device_class: type[MySensorsChildEntity] | Mapping[SensorType, type[MySensorsChildEntity]], async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...
