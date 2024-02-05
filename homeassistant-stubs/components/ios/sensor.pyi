from .. import ios as ios
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import PERCENTAGE as PERCENTAGE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.icon import icon_for_battery_level as icon_for_battery_level
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

SENSOR_TYPES: tuple[SensorEntityDescription, ...]
DEFAULT_ICON_LEVEL: str
DEFAULT_ICON_STATE: str

def setup_platform(hass: HomeAssistant, config: ConfigType, add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class IOSSensor(SensorEntity):
    _attr_should_poll: bool
    _attr_has_entity_name: bool
    entity_description: Incomplete
    _device: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, device_name: str, device: dict[str, Any], description: SensorEntityDescription) -> None: ...
    @property
    def device_info(self) -> DeviceInfo: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
    @property
    def icon(self) -> str: ...
    _attr_native_value: Incomplete
    def _update(self, device: dict[str, Any]) -> None: ...
    async def async_added_to_hass(self) -> None: ...
