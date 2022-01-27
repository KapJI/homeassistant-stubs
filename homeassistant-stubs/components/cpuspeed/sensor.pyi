from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from homeassistant.components.sensor import PLATFORM_SCHEMA as PLATFORM_SCHEMA, SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry, SOURCE_IMPORT as SOURCE_IMPORT
from homeassistant.const import CONF_NAME as CONF_NAME, FREQUENCY_GIGAHERTZ as FREQUENCY_GIGAHERTZ
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

ATTR_BRAND: str
ATTR_HZ: str
ATTR_ARCH: str
HZ_ACTUAL: str
HZ_ADVERTISED: str
DEFAULT_NAME: str

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: Union[DiscoveryInfoType, None] = ...) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class CPUSpeedSensor(SensorEntity):
    _attr_icon: str
    _attr_name: str
    _attr_native_unit_of_measurement: Any
    _attr_unique_id: Any
    def __init__(self, entry: ConfigEntry) -> None: ...
    _attr_native_value: Any
    _attr_extra_state_attributes: Any
    def update(self) -> None: ...
