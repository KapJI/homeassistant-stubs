from .const import DATA_ELGATO_CLIENT as DATA_ELGATO_CLIENT, DOMAIN as DOMAIN, SERVICE_IDENTIFY as SERVICE_IDENTIFY
from elgato import Elgato as Elgato, Info as Info, Settings as Settings, State as State
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ATTR_COLOR_TEMP as ATTR_COLOR_TEMP, ATTR_HS_COLOR as ATTR_HS_COLOR, COLOR_MODE_COLOR_TEMP as COLOR_MODE_COLOR_TEMP, COLOR_MODE_HS as COLOR_MODE_HS, LightEntity as LightEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_IDENTIFIERS as ATTR_IDENTIFIERS, ATTR_MANUFACTURER as ATTR_MANUFACTURER, ATTR_MODEL as ATTR_MODEL, ATTR_NAME as ATTR_NAME, ATTR_SW_VERSION as ATTR_SW_VERSION
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback, async_get_current_platform as async_get_current_platform
from typing import Any

_LOGGER: Any
PARALLEL_UPDATES: int
SCAN_INTERVAL: Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ElgatoLight(LightEntity):
    _info: Any
    _settings: Any
    _state: Any
    elgato: Any
    _attr_max_mireds: Any
    _attr_min_mireds: Any
    _attr_name: Any
    _attr_supported_color_modes: Any
    _attr_unique_id: Any
    def __init__(self, elgato: Elgato, info: Info, settings: Settings) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def brightness(self) -> Union[int, None]: ...
    @property
    def color_temp(self) -> Union[int, None]: ...
    @property
    def color_mode(self) -> Union[str, None]: ...
    @property
    def hs_color(self) -> Union[tuple[float, float], None]: ...
    @property
    def is_on(self) -> bool: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_update(self) -> None: ...
    @property
    def device_info(self) -> DeviceInfo: ...
    async def async_identify(self) -> None: ...
