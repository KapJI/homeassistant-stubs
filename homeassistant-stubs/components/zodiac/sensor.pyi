from .const import ATTR_ELEMENT as ATTR_ELEMENT, ATTR_MODALITY as ATTR_MODALITY, DOMAIN as DOMAIN, ELEMENT_AIR as ELEMENT_AIR, ELEMENT_EARTH as ELEMENT_EARTH, ELEMENT_FIRE as ELEMENT_FIRE, ELEMENT_WATER as ELEMENT_WATER, MODALITY_CARDINAL as MODALITY_CARDINAL, MODALITY_FIXED as MODALITY_FIXED, MODALITY_MUTABLE as MODALITY_MUTABLE, SIGN_AQUARIUS as SIGN_AQUARIUS, SIGN_ARIES as SIGN_ARIES, SIGN_CANCER as SIGN_CANCER, SIGN_CAPRICORN as SIGN_CAPRICORN, SIGN_GEMINI as SIGN_GEMINI, SIGN_LEO as SIGN_LEO, SIGN_LIBRA as SIGN_LIBRA, SIGN_PISCES as SIGN_PISCES, SIGN_SAGITTARIUS as SIGN_SAGITTARIUS, SIGN_SCORPIO as SIGN_SCORPIO, SIGN_TAURUS as SIGN_TAURUS, SIGN_VIRGO as SIGN_VIRGO
from homeassistant.components.sensor import SensorEntity as SensorEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from homeassistant.util.dt import as_local as as_local, utcnow as utcnow
from typing import Any

ZODIAC_BY_DATE: Any
ZODIAC_ICONS: Any

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: Union[DiscoveryInfoType, None] = ...) -> None: ...

class ZodiacSensor(SensorEntity):
    _attrs: Any
    _state: str
    def __init__(self) -> None: ...
    @property
    def unique_id(self) -> str: ...
    @property
    def name(self) -> str: ...
    @property
    def device_class(self) -> str: ...
    @property
    def state(self) -> str: ...
    @property
    def icon(self) -> Union[str, None]: ...
    @property
    def extra_state_attributes(self) -> dict[str, str]: ...
    async def async_update(self) -> None: ...
