from .const import CONF_LEGACY_SETPOINT_STATUS as CONF_LEGACY_SETPOINT_STATUS, DOMAIN as DOMAIN
from .coordinator import InComfortConfigEntry as InComfortConfigEntry, InComfortDataCoordinator as InComfortDataCoordinator
from .entity import IncomfortEntity as IncomfortEntity
from _typeshed import Incomplete
from homeassistant.components.climate import ClimateEntity as ClimateEntity, ClimateEntityFeature as ClimateEntityFeature, HVACAction as HVACAction, HVACMode as HVACMode
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from incomfortclient import Heater as InComfortHeater, Room as InComfortRoom
from typing import Any

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: InComfortConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class InComfortClimate(IncomfortEntity, ClimateEntity):
    _attr_min_temp: float
    _attr_max_temp: float
    _attr_name: Incomplete
    _attr_hvac_mode: Incomplete
    _attr_hvac_modes: Incomplete
    _attr_supported_features: Incomplete
    _attr_temperature_unit: Incomplete
    _heater: Incomplete
    _room: Incomplete
    _legacy_setpoint_status: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: InComfortDataCoordinator, heater: InComfortHeater, room: InComfortRoom, legacy_setpoint_status: bool) -> None: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
    @property
    def current_temperature(self) -> float | None: ...
    @property
    def hvac_action(self) -> HVACAction | None: ...
    @property
    def target_temperature(self) -> float | None: ...
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
