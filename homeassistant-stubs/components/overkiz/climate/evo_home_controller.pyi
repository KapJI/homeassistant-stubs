from ..entity import OverkizDataUpdateCoordinator as OverkizDataUpdateCoordinator, OverkizEntity as OverkizEntity
from _typeshed import Incomplete
from homeassistant.components.climate import ClimateEntity as ClimateEntity, ClimateEntityFeature as ClimateEntityFeature, HVACMode as HVACMode, PRESET_NONE as PRESET_NONE
from homeassistant.const import UnitOfTemperature as UnitOfTemperature

PRESET_DAY_OFF: str
PRESET_HOLIDAYS: str
OVERKIZ_TO_HVAC_MODES: dict[str, HVACMode]
HVAC_MODES_TO_OVERKIZ: Incomplete
OVERKIZ_TO_PRESET_MODES: dict[str, str]
PRESET_MODES_TO_OVERKIZ: Incomplete

class EvoHomeController(OverkizEntity, ClimateEntity):
    _attr_hvac_modes: Incomplete
    _attr_preset_modes: Incomplete
    _attr_supported_features: Incomplete
    _attr_temperature_unit: Incomplete
    def __init__(self, device_url: str, coordinator: OverkizDataUpdateCoordinator) -> None: ...
    @property
    def hvac_mode(self) -> HVACMode: ...
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    @property
    def preset_mode(self) -> str | None: ...
    async def async_set_preset_mode(self, preset_mode: str) -> None: ...
