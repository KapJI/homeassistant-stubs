from . import HomeAssistantElgatoData as HomeAssistantElgatoData
from .const import DOMAIN as DOMAIN, SERVICE_IDENTIFY as SERVICE_IDENTIFY
from .entity import ElgatoEntity as ElgatoEntity
from _typeshed import Incomplete
from elgato import Elgato as Elgato, Info as Info, Settings as Settings, State
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ATTR_COLOR_TEMP as ATTR_COLOR_TEMP, ATTR_HS_COLOR as ATTR_HS_COLOR, ColorMode as ColorMode, LightEntity as LightEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_MAC as CONF_MAC
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback, async_get_current_platform as async_get_current_platform
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator
from typing import Any

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ElgatoLight(ElgatoEntity, CoordinatorEntity[DataUpdateCoordinator[State]], LightEntity):
    _attr_min_mireds: int
    _attr_max_mireds: int
    _attr_supported_color_modes: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: DataUpdateCoordinator[State], client: Elgato, info: Info, mac: Union[str, None], settings: Settings) -> None: ...
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
