from .const import ATTR_ELEMENT as ATTR_ELEMENT, ATTR_MODALITY as ATTR_MODALITY, DOMAIN as DOMAIN, ELEMENT_AIR as ELEMENT_AIR, ELEMENT_EARTH as ELEMENT_EARTH, ELEMENT_FIRE as ELEMENT_FIRE, ELEMENT_WATER as ELEMENT_WATER, MODALITY_CARDINAL as MODALITY_CARDINAL, MODALITY_FIXED as MODALITY_FIXED, MODALITY_MUTABLE as MODALITY_MUTABLE, SIGN_AQUARIUS as SIGN_AQUARIUS, SIGN_ARIES as SIGN_ARIES, SIGN_CANCER as SIGN_CANCER, SIGN_CAPRICORN as SIGN_CAPRICORN, SIGN_GEMINI as SIGN_GEMINI, SIGN_LEO as SIGN_LEO, SIGN_LIBRA as SIGN_LIBRA, SIGN_PISCES as SIGN_PISCES, SIGN_SAGITTARIUS as SIGN_SAGITTARIUS, SIGN_SCORPIO as SIGN_SCORPIO, SIGN_TAURUS as SIGN_TAURUS, SIGN_VIRGO as SIGN_VIRGO
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from homeassistant.util.dt import as_local as as_local, utcnow as utcnow

ZODIAC_BY_DATE: Incomplete
ZODIAC_ICONS: Incomplete

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = ...) -> None: ...

class ZodiacSensor(SensorEntity):
    _attr_name: str
    _attr_device_class: Incomplete
    _attr_options: Incomplete
    _attr_translation_key: str
    _attr_unique_id = DOMAIN
    _attr_native_value: Incomplete
    _attr_icon: Incomplete
    _attr_extra_state_attributes: Incomplete
    async def async_update(self) -> None: ...
