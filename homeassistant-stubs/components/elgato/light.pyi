from . import HomeAssistantElgatoData as HomeAssistantElgatoData
from .const import DOMAIN as DOMAIN, LOGGER as LOGGER, SERVICE_IDENTIFY as SERVICE_IDENTIFY
from .entity import ElgatoEntity as ElgatoEntity
from elgato import Elgato as Elgato, Info as Info, Settings as Settings, State as State
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ATTR_COLOR_TEMP as ATTR_COLOR_TEMP, ATTR_HS_COLOR as ATTR_HS_COLOR, COLOR_MODE_COLOR_TEMP as COLOR_MODE_COLOR_TEMP, COLOR_MODE_HS as COLOR_MODE_HS, LightEntity as LightEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_MAC as CONF_MAC
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback, async_get_current_platform as async_get_current_platform
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator
from typing import Any

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ElgatoLight(ElgatoEntity, CoordinatorEntity, LightEntity):
    coordinator: DataUpdateCoordinator[State]
    _attr_max_mireds: Any
    _attr_min_mireds: Any
    _attr_name: Any
    _attr_supported_color_modes: Any
    _attr_unique_id: Any
    def __init__(self, coordinator: DataUpdateCoordinator, client: Elgato, info: Info, mac: Union[str, None], settings: Settings) -> None: ...
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
    async def async_identify(self) -> None: ...
