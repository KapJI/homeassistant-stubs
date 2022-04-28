from homeassistant.components.climate import ClimateEntity as ClimateEntity
from homeassistant.components.climate.const import ClimateEntityFeature as ClimateEntityFeature, HVACMode as HVACMode, PRESET_COMFORT as PRESET_COMFORT, PRESET_ECO as PRESET_ECO, PRESET_NONE as PRESET_NONE
from homeassistant.components.overkiz.entity import OverkizEntity as OverkizEntity
from homeassistant.const import TEMP_CELSIUS as TEMP_CELSIUS
from typing import Any

PRESET_FROST_PROTECTION: str
OVERKIZ_TO_HVAC_MODES: dict[str, HVACMode]
HVAC_MODES_TO_OVERKIZ: Any
OVERKIZ_TO_PRESET_MODES: dict[str, str]
PRESET_MODES_TO_OVERKIZ: Any

class AtlanticElectricalHeater(OverkizEntity, ClimateEntity):
    _attr_hvac_modes: Any
    _attr_preset_modes: Any
    _attr_supported_features: Any
    _attr_temperature_unit: Any
    @property
    def hvac_mode(self) -> HVACMode: ...
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    @property
    def preset_mode(self) -> Union[str, None]: ...
    async def async_set_preset_mode(self, preset_mode: str) -> None: ...
