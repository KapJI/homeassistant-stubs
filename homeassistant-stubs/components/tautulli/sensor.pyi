from .coordinator import TautulliDataUpdateCoordinator as TautulliDataUpdateCoordinator
from homeassistant.components.sensor import PLATFORM_SCHEMA as PLATFORM_SCHEMA, SensorEntity as SensorEntity
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_HOST as CONF_HOST, CONF_MONITORED_CONDITIONS as CONF_MONITORED_CONDITIONS, CONF_NAME as CONF_NAME, CONF_PATH as CONF_PATH, CONF_PORT as CONF_PORT, CONF_SSL as CONF_SSL, CONF_VERIFY_SSL as CONF_VERIFY_SSL
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType, StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

CONF_MONITORED_USERS: str
DEFAULT_NAME: str
DEFAULT_PORT: str
DEFAULT_PATH: str
DEFAULT_SSL: bool
DEFAULT_VERIFY_SSL: bool

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: Union[DiscoveryInfoType, None] = ...) -> None: ...

class TautulliSensor(CoordinatorEntity, SensorEntity):
    coordinator: TautulliDataUpdateCoordinator
    monitored_conditions: Any
    usernames: Any
    _name: Any
    def __init__(self, coordinator: TautulliDataUpdateCoordinator, name: str, monitored_conditions: list[str], usernames: list[str]) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def native_value(self) -> StateType: ...
    @property
    def icon(self) -> str: ...
    @property
    def native_unit_of_measurement(self) -> str: ...
    @property
    def extra_state_attributes(self) -> Union[dict[str, Any], None]: ...
