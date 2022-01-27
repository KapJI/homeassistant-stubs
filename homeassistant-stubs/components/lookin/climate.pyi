from .const import DOMAIN as DOMAIN, TYPE_TO_PLATFORM as TYPE_TO_PLATFORM
from .coordinator import LookinDataUpdateCoordinator as LookinDataUpdateCoordinator
from .entity import LookinCoordinatorEntity as LookinCoordinatorEntity
from .models import LookinData as LookinData
from aiolookin import Climate, MeteoSensor as MeteoSensor
from aiolookin.models import UDPEvent as UDPEvent
from homeassistant.components.climate import ClimateEntity as ClimateEntity
from homeassistant.components.climate.const import ATTR_HVAC_MODE as ATTR_HVAC_MODE, FAN_AUTO as FAN_AUTO, FAN_HIGH as FAN_HIGH, FAN_LOW as FAN_LOW, FAN_MIDDLE as FAN_MIDDLE, HVAC_MODE_AUTO as HVAC_MODE_AUTO, HVAC_MODE_COOL as HVAC_MODE_COOL, HVAC_MODE_DRY as HVAC_MODE_DRY, HVAC_MODE_FAN_ONLY as HVAC_MODE_FAN_ONLY, HVAC_MODE_HEAT as HVAC_MODE_HEAT, HVAC_MODE_OFF as HVAC_MODE_OFF, SUPPORT_FAN_MODE as SUPPORT_FAN_MODE, SUPPORT_SWING_MODE as SUPPORT_SWING_MODE, SUPPORT_TARGET_TEMPERATURE as SUPPORT_TARGET_TEMPERATURE, SWING_BOTH as SWING_BOTH, SWING_OFF as SWING_OFF
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, PRECISION_WHOLE as PRECISION_WHOLE, Platform as Platform, TEMP_CELSIUS as TEMP_CELSIUS
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any, Final

SUPPORT_FLAGS: int
LOOKIN_FAN_MODE_IDX_TO_HASS: Final[Any]
LOOKIN_SWING_MODE_IDX_TO_HASS: Final[Any]
LOOKIN_HVAC_MODE_IDX_TO_HASS: Final[Any]
HASS_TO_LOOKIN_HVAC_MODE: dict[str, int]
HASS_TO_LOOKIN_FAN_MODE: dict[str, int]
HASS_TO_LOOKIN_SWING_MODE: dict[str, int]
MIN_TEMP: Final[int]
MAX_TEMP: Final[int]
LOGGER: Any

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ConditionerEntity(LookinCoordinatorEntity, ClimateEntity):
    _attr_current_humidity: Union[float, None]
    _attr_temperature_unit: Any
    _attr_supported_features: int
    _attr_fan_modes: list[str]
    _attr_swing_modes: list[str]
    _attr_hvac_modes: list[str]
    _attr_min_temp: Any
    _attr_max_temp: Any
    _attr_target_temperature_step: Any
    def __init__(self, uuid: str, device: Climate, lookin_data: LookinData, coordinator: LookinDataUpdateCoordinator) -> None: ...
    @property
    def _climate(self) -> Climate: ...
    async def async_set_hvac_mode(self, hvac_mode: str) -> None: ...
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    async def async_set_fan_mode(self, fan_mode: str) -> None: ...
    async def async_set_swing_mode(self, swing_mode: str) -> None: ...
    async def _async_update_conditioner(self) -> None: ...
    _attr_current_temperature: Any
    _attr_target_temperature: Any
    _attr_fan_mode: Any
    _attr_swing_mode: Any
    _attr_hvac_mode: Any
    def _async_update_from_data(self) -> None: ...
    def _async_update_meteo_from_value(self, event: UDPEvent) -> None: ...
    def _handle_coordinator_update(self) -> None: ...
    def _async_push_update(self, event: UDPEvent) -> None: ...
    async def async_added_to_hass(self) -> None: ...
