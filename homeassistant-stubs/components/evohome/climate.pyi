import evohomeasync2 as evo
from . import EVOHOME_KEY as EVOHOME_KEY
from .const import ATTR_DURATION as ATTR_DURATION, ATTR_DURATION_UNTIL as ATTR_DURATION_UNTIL, ATTR_PERIOD as ATTR_PERIOD, ATTR_SETPOINT as ATTR_SETPOINT, EvoService as EvoService
from .coordinator import EvoDataUpdateCoordinator as EvoDataUpdateCoordinator
from .entity import EvoChild as EvoChild, EvoEntity as EvoEntity
from _typeshed import Incomplete
from datetime import datetime
from evohomeasync2.schemas.const import SystemMode as EvoSystemMode
from homeassistant.components.climate import ClimateEntity as ClimateEntity, ClimateEntityFeature as ClimateEntityFeature, HVACMode as HVACMode, PRESET_AWAY as PRESET_AWAY, PRESET_ECO as PRESET_ECO, PRESET_HOME as PRESET_HOME, PRESET_NONE as PRESET_NONE
from homeassistant.const import ATTR_MODE as ATTR_MODE, PRECISION_TENTHS as PRECISION_TENTHS, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

_LOGGER: Incomplete
PRESET_RESET: str
PRESET_CUSTOM: str
TCS_PRESET_TO_HA: Incomplete
HA_PRESET_TO_TCS: Incomplete
EVO_PRESET_TO_HA: Incomplete
HA_PRESET_TO_EVO: Incomplete

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...

class EvoClimateEntity(EvoEntity, ClimateEntity):
    _attr_hvac_modes: Incomplete
    _attr_temperature_unit: Incomplete

class EvoZone(EvoChild, EvoClimateEntity):
    _attr_preset_modes: Incomplete
    _evo_device: evo.Zone
    _evo_id_attr: str
    _evo_state_attr_names: Incomplete
    _evo_id: Incomplete
    _attr_unique_id: Incomplete
    _attr_precision: Incomplete
    _attr_supported_features: Incomplete
    def __init__(self, coordinator: EvoDataUpdateCoordinator, evo_device: evo.Zone) -> None: ...
    async def async_zone_svc_request(self, service: str, data: dict[str, Any]) -> None: ...
    @property
    def name(self) -> str | None: ...
    @property
    def hvac_mode(self) -> HVACMode | None: ...
    @property
    def target_temperature(self) -> float | None: ...
    @property
    def preset_mode(self) -> str | None: ...
    @property
    def min_temp(self) -> float: ...
    @property
    def max_temp(self) -> float: ...
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    async def async_set_preset_mode(self, preset_mode: str) -> None: ...

class EvoController(EvoClimateEntity):
    _attr_icon: str
    _attr_precision = PRECISION_TENTHS
    _evo_device: evo.ControlSystem
    _evo_id_attr: str
    _evo_state_attr_names: Incomplete
    _evo_id: Incomplete
    _attr_unique_id: Incomplete
    _attr_name: Incomplete
    _evo_modes: Incomplete
    _attr_preset_modes: Incomplete
    _attr_supported_features: Incomplete
    def __init__(self, coordinator: EvoDataUpdateCoordinator, evo_device: evo.ControlSystem) -> None: ...
    async def async_tcs_svc_request(self, service: str, data: dict[str, Any]) -> None: ...
    async def _set_tcs_mode(self, mode: EvoSystemMode, until: datetime | None = None) -> None: ...
    @property
    def hvac_mode(self) -> HVACMode: ...
    @property
    def current_temperature(self) -> float | None: ...
    @property
    def preset_mode(self) -> str | None: ...
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    async def async_set_preset_mode(self, preset_mode: str) -> None: ...
    _device_state_attrs: Incomplete
    @callback
    def _handle_coordinator_update(self) -> None: ...
    async def update_attrs(self) -> None: ...
