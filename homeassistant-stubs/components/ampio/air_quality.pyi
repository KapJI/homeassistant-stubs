from .const import ATTRIBUTION as ATTRIBUTION, CONF_STATION_ID as CONF_STATION_ID, SCAN_INTERVAL as SCAN_INTERVAL
from asmog import AmpioSmog
from homeassistant.components.air_quality import AirQualityEntity as AirQualityEntity
from homeassistant.const import CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from homeassistant.util import Throttle as Throttle
from typing import Any, Final

_LOGGER: Final[Any]
PLATFORM_SCHEMA: Final[Any]

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: Union[DiscoveryInfoType, None] = ...) -> None: ...

class AmpioSmogQuality(AirQualityEntity):
    _ampio: Any
    _station_id: Any
    _name: Any
    def __init__(self, api: AmpioSmogMapData, station_id: str, name: Union[str, None]) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def unique_id(self) -> str: ...
    @property
    def particulate_matter_2_5(self) -> Union[str, None]: ...
    @property
    def particulate_matter_10(self) -> Union[str, None]: ...
    @property
    def attribution(self) -> str: ...
    async def async_update(self) -> None: ...

class AmpioSmogMapData:
    api: Any
    def __init__(self, api: AmpioSmog) -> None: ...
    async def async_update(self) -> None: ...
