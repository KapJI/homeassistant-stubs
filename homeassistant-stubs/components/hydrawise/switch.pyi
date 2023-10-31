from .const import ALLOWED_WATERING_TIME as ALLOWED_WATERING_TIME, CONF_WATERING_TIME as CONF_WATERING_TIME, DEFAULT_WATERING_TIME as DEFAULT_WATERING_TIME, DOMAIN as DOMAIN
from .coordinator import HydrawiseDataUpdateCoordinator as HydrawiseDataUpdateCoordinator
from .entity import HydrawiseEntity as HydrawiseEntity
from _typeshed import Incomplete
from homeassistant.components.switch import PLATFORM_SCHEMA as PLATFORM_SCHEMA, SwitchDeviceClass as SwitchDeviceClass, SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_MONITORED_CONDITIONS as CONF_MONITORED_CONDITIONS
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

SWITCH_TYPES: tuple[SwitchEntityDescription, ...]
SWITCH_KEYS: list[str]

def setup_platform(hass: HomeAssistant, config: ConfigType, add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = ...) -> None: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class HydrawiseSwitch(HydrawiseEntity, SwitchEntity):
    _default_watering_timer: Incomplete
    def __init__(self, *, data: dict[str, Any], coordinator: HydrawiseDataUpdateCoordinator, description: SwitchEntityDescription, default_watering_timer: int) -> None: ...
    def turn_on(self, **kwargs: Any) -> None: ...
    def turn_off(self, **kwargs: Any) -> None: ...
    _attr_is_on: Incomplete
    def _update_attrs(self) -> None: ...
