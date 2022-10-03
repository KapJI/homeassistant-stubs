from .const import API_TEMPERATURE_STEP as API_TEMPERATURE_STEP, DOMAIN as DOMAIN, TEMP_UNIT_LIB_TO_HASS as TEMP_UNIT_LIB_TO_HASS
from .coordinator import AirzoneUpdateCoordinator as AirzoneUpdateCoordinator
from .entity import AirzoneZoneEntity as AirzoneZoneEntity
from _typeshed import Incomplete
from aioairzone.common import OperationMode
from homeassistant.components.climate import ClimateEntity as ClimateEntity, ClimateEntityFeature as ClimateEntityFeature, HVACAction as HVACAction, HVACMode as HVACMode
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any, Final

_LOGGER: Incomplete
HVAC_ACTION_LIB_TO_HASS: Final[dict[OperationMode, HVACAction]]
HVAC_MODE_LIB_TO_HASS: Final[dict[OperationMode, HVACMode]]
HVAC_MODE_HASS_TO_LIB: Final[dict[HVACMode, OperationMode]]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AirzoneClimate(AirzoneZoneEntity, ClimateEntity):
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    _attr_supported_features: Incomplete
    _attr_target_temperature_step: Incomplete
    _attr_max_temp: Incomplete
    _attr_min_temp: Incomplete
    _attr_temperature_unit: Incomplete
    _attr_hvac_modes: Incomplete
    def __init__(self, coordinator: AirzoneUpdateCoordinator, entry: ConfigEntry, system_zone_id: str, zone_data: dict) -> None: ...
    async def _async_update_hvac_params(self, params: dict[str, Any]) -> None: ...
    async def async_turn_on(self) -> None: ...
    async def async_turn_off(self) -> None: ...
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    def _handle_coordinator_update(self) -> None: ...
    _attr_current_temperature: Incomplete
    _attr_current_humidity: Incomplete
    _attr_hvac_mode: Incomplete
    _attr_hvac_action: Incomplete
    _attr_target_temperature: Incomplete
    def _async_update_attrs(self) -> None: ...
