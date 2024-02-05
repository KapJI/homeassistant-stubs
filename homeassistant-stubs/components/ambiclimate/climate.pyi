from .const import ATTR_VALUE as ATTR_VALUE, DOMAIN as DOMAIN, SERVICE_COMFORT_FEEDBACK as SERVICE_COMFORT_FEEDBACK, SERVICE_COMFORT_MODE as SERVICE_COMFORT_MODE, SERVICE_TEMPERATURE_MODE as SERVICE_TEMPERATURE_MODE, STORAGE_KEY as STORAGE_KEY, STORAGE_VERSION as STORAGE_VERSION
from _typeshed import Incomplete
from ambiclimate import AmbiclimateDevice as AmbiclimateDevice
from homeassistant.components.climate import ClimateEntity as ClimateEntity, ClimateEntityFeature as ClimateEntityFeature, HVACMode as HVACMode
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_NAME as ATTR_NAME, ATTR_TEMPERATURE as ATTR_TEMPERATURE, CONF_CLIENT_ID as CONF_CLIENT_ID, CONF_CLIENT_SECRET as CONF_CLIENT_SECRET, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.storage import Store as Store
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

_LOGGER: Incomplete
SEND_COMFORT_FEEDBACK_SCHEMA: Incomplete
SET_COMFORT_MODE_SCHEMA: Incomplete
SET_TEMPERATURE_MODE_SCHEMA: Incomplete

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AmbiclimateEntity(ClimateEntity):
    _attr_temperature_unit: Incomplete
    _attr_target_temperature_step: int
    _attr_supported_features: Incomplete
    _attr_hvac_modes: Incomplete
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    _enable_turn_on_off_backwards_compatibility: bool
    _heater: Incomplete
    _store: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, heater: AmbiclimateDevice, store: Store[dict[str, Any]]) -> None: ...
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    _attr_min_temp: Incomplete
    _attr_max_temp: Incomplete
    _attr_target_temperature: Incomplete
    _attr_current_temperature: Incomplete
    _attr_current_humidity: Incomplete
    _attr_hvac_mode: Incomplete
    async def async_update(self) -> None: ...
