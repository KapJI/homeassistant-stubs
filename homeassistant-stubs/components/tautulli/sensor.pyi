from . import TautulliEntity as TautulliEntity
from .const import CONF_MONITORED_USERS as CONF_MONITORED_USERS, DEFAULT_NAME as DEFAULT_NAME, DEFAULT_PATH as DEFAULT_PATH, DEFAULT_PORT as DEFAULT_PORT, DEFAULT_SSL as DEFAULT_SSL, DEFAULT_VERIFY_SSL as DEFAULT_VERIFY_SSL, DOMAIN as DOMAIN
from .coordinator import TautulliDataUpdateCoordinator as TautulliDataUpdateCoordinator
from homeassistant.components.sensor import PLATFORM_SCHEMA as PLATFORM_SCHEMA, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry, SOURCE_IMPORT as SOURCE_IMPORT
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_HOST as CONF_HOST, CONF_MONITORED_CONDITIONS as CONF_MONITORED_CONDITIONS, CONF_NAME as CONF_NAME, CONF_PATH as CONF_PATH, CONF_PORT as CONF_PORT, CONF_SSL as CONF_SSL, CONF_VERIFY_SSL as CONF_VERIFY_SSL
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType, StateType as StateType
from typing import Any

SENSOR_TYPES: tuple[SensorEntityDescription, ...]

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: Union[DiscoveryInfoType, None] = ...) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class TautulliSensor(TautulliEntity, SensorEntity):
    @property
    def native_value(self) -> StateType: ...
    @property
    def extra_state_attributes(self) -> Union[dict[str, Any], None]: ...
