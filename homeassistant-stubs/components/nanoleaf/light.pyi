from . import NanoleafEntryData as NanoleafEntryData
from .const import DOMAIN as DOMAIN
from .entity import NanoleafEntity as NanoleafEntity
from aionanoleaf import Nanoleaf as Nanoleaf
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ATTR_COLOR_TEMP as ATTR_COLOR_TEMP, ATTR_EFFECT as ATTR_EFFECT, ATTR_HS_COLOR as ATTR_HS_COLOR, ATTR_TRANSITION as ATTR_TRANSITION, LightEntity as LightEntity, PLATFORM_SCHEMA as PLATFORM_SCHEMA, SUPPORT_BRIGHTNESS as SUPPORT_BRIGHTNESS, SUPPORT_COLOR as SUPPORT_COLOR, SUPPORT_COLOR_TEMP as SUPPORT_COLOR_TEMP, SUPPORT_EFFECT as SUPPORT_EFFECT, SUPPORT_TRANSITION as SUPPORT_TRANSITION
from homeassistant.config_entries import ConfigEntry as ConfigEntry, SOURCE_IMPORT as SOURCE_IMPORT
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_NAME as CONF_NAME, CONF_TOKEN as CONF_TOKEN
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from typing import Any

RESERVED_EFFECTS: Any
DEFAULT_NAME: str
_LOGGER: Any

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: Union[DiscoveryInfoType, None] = ...) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class NanoleafLight(NanoleafEntity, LightEntity):
    _attr_unique_id: Any
    _attr_name: Any
    _attr_min_mireds: Any
    _attr_max_mireds: Any
    def __init__(self, nanoleaf: Nanoleaf, coordinator: DataUpdateCoordinator) -> None: ...
    @property
    def brightness(self) -> int: ...
    @property
    def color_temp(self) -> int: ...
    @property
    def effect(self) -> Union[str, None]: ...
    @property
    def effect_list(self) -> list[str]: ...
    @property
    def icon(self) -> str: ...
    @property
    def is_on(self) -> bool: ...
    @property
    def hs_color(self) -> tuple[int, int]: ...
    @property
    def supported_features(self) -> int: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
