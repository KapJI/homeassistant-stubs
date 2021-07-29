from .const import ADD_TRACKING_SERVICE_SCHEMA as ADD_TRACKING_SERVICE_SCHEMA, ATTRIBUTION as ATTRIBUTION, ATTR_TRACKINGS as ATTR_TRACKINGS, BASE as BASE, CONF_SLUG as CONF_SLUG, CONF_TITLE as CONF_TITLE, CONF_TRACKING_NUMBER as CONF_TRACKING_NUMBER, DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN, ICON as ICON, MIN_TIME_BETWEEN_UPDATES as MIN_TIME_BETWEEN_UPDATES, REMOVE_TRACKING_SERVICE_SCHEMA as REMOVE_TRACKING_SERVICE_SCHEMA, SERVICE_ADD_TRACKING as SERVICE_ADD_TRACKING, SERVICE_REMOVE_TRACKING as SERVICE_REMOVE_TRACKING, UPDATE_TOPIC as UPDATE_TOPIC
from homeassistant.components.sensor import SensorEntity as SensorEntity
from homeassistant.const import ATTR_ATTRIBUTION as ATTR_ATTRIBUTION, CONF_API_KEY as CONF_API_KEY, CONF_NAME as CONF_NAME, HTTP_OK as HTTP_OK
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.service import ServiceCall as ServiceCall
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from homeassistant.util import Throttle as Throttle
from pyaftership.tracker import Tracking
from typing import Any, Final

_LOGGER: Final[Any]
PLATFORM_SCHEMA: Final[Any]

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: Union[DiscoveryInfoType, None] = ...) -> None: ...

class AfterShipSensor(SensorEntity):
    _attr_unit_of_measurement: str
    _attr_icon: str
    _attributes: Any
    _state: Any
    aftership: Any
    _attr_name: Any
    def __init__(self, aftership: Tracking, name: str) -> None: ...
    @property
    def state(self) -> Union[int, None]: ...
    @property
    def extra_state_attributes(self) -> dict[str, str]: ...
    async def async_added_to_hass(self) -> None: ...
    async def _force_update(self) -> None: ...
    async def async_update(self, **kwargs: Any) -> None: ...
