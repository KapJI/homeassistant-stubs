from . import BSBLanConfigEntry as BSBLanConfigEntry, BSBLanData as BSBLanData
from .const import ATTR_TARGET_TEMPERATURE as ATTR_TARGET_TEMPERATURE, DOMAIN as DOMAIN
from .entity import BSBLanEntity as BSBLanEntity
from _typeshed import Incomplete
from homeassistant.components.climate import ATTR_HVAC_MODE as ATTR_HVAC_MODE, ATTR_PRESET_MODE as ATTR_PRESET_MODE, ClimateEntity as ClimateEntity, ClimateEntityFeature as ClimateEntityFeature, HVACAction as HVACAction, HVACMode as HVACMode, PRESET_ECO as PRESET_ECO, PRESET_NONE as PRESET_NONE
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.device_registry import format_mac as format_mac
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any, Final

PARALLEL_UPDATES: int
HVAC_MODES: Incomplete
PRESET_MODES: Incomplete
HA_TO_BSBLAN_HVAC_MODE: Final[dict[HVACMode, int]]
BSBLAN_TO_HA_HVAC_MODE: Final[dict[int, HVACMode]]

async def async_setup_entry(hass: HomeAssistant, entry: BSBLanConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class BSBLANClimate(BSBLanEntity, ClimateEntity):
    _attr_name: Incomplete
    _attr_supported_features: Incomplete
    _attr_preset_modes = PRESET_MODES
    _attr_hvac_modes = HVAC_MODES
    _attr_unique_id: Incomplete
    _attr_min_temp: Incomplete
    _attr_max_temp: Incomplete
    _attr_temperature_unit: Incomplete
    def __init__(self, data: BSBLanData) -> None: ...
    @property
    def current_temperature(self) -> float | None: ...
    @property
    def target_temperature(self) -> float | None: ...
    @property
    def _hvac_mode_value(self) -> int | None: ...
    @property
    def hvac_mode(self) -> HVACMode | None: ...
    @property
    def hvac_action(self) -> HVACAction | None: ...
    @property
    def preset_mode(self) -> str | None: ...
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    async def async_set_preset_mode(self, preset_mode: str) -> None: ...
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    async def async_set_data(self, **kwargs: Any) -> None: ...
