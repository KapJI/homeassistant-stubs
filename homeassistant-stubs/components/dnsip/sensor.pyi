from .const import CONF_HOSTNAME as CONF_HOSTNAME, CONF_IPV4 as CONF_IPV4, CONF_IPV6 as CONF_IPV6, CONF_RESOLVER as CONF_RESOLVER, CONF_RESOLVER_IPV6 as CONF_RESOLVER_IPV6, DEFAULT_HOSTNAME as DEFAULT_HOSTNAME, DEFAULT_IPV6 as DEFAULT_IPV6, DEFAULT_RESOLVER as DEFAULT_RESOLVER, DEFAULT_RESOLVER_IPV6 as DEFAULT_RESOLVER_IPV6, DOMAIN as DOMAIN
from homeassistant.components.sensor import SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry, SOURCE_IMPORT as SOURCE_IMPORT
from homeassistant.const import CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

_LOGGER: Any
SCAN_INTERVAL: Any
PLATFORM_SCHEMA: Any

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_devices: AddEntitiesCallback, discovery_info: Union[DiscoveryInfoType, None] = ...) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class WanIpSensor(SensorEntity):
    _attr_icon: str
    _attr_name: Any
    _attr_unique_id: Any
    hostname: Any
    resolver: Any
    querytype: Any
    _attr_extra_state_attributes: Any
    _attr_device_info: Any
    def __init__(self, name: str, hostname: str, resolver: str, ipv6: bool) -> None: ...
    _attr_native_value: Any
    _attr_available: bool
    async def async_update(self) -> None: ...
