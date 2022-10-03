from ..coordinator import OverkizDataUpdateCoordinator as OverkizDataUpdateCoordinator
from ..entity import OverkizEntity as OverkizEntity
from _typeshed import Incomplete
from homeassistant.components.climate import ClimateEntity as ClimateEntity, ClimateEntityFeature as ClimateEntityFeature, HVACMode as HVACMode, PRESET_BOOST as PRESET_BOOST, PRESET_NONE as PRESET_NONE
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, TEMP_CELSIUS as TEMP_CELSIUS
from typing import Any

PRESET_DRYING: str
OVERKIZ_TO_HVAC_MODE: dict[str, str]
HVAC_MODE_TO_OVERKIZ: Incomplete
OVERKIZ_TO_PRESET_MODE: dict[str, str]
PRESET_MODE_TO_OVERKIZ: Incomplete
TEMPERATURE_SENSOR_DEVICE_INDEX: int

class AtlanticElectricalTowelDryer(OverkizEntity, ClimateEntity):
    _attr_hvac_modes: Incomplete
    _attr_preset_modes: Incomplete
    _attr_temperature_unit: Incomplete
    temperature_device: Incomplete
    _attr_supported_features: Incomplete
    def __init__(self, device_url: str, coordinator: OverkizDataUpdateCoordinator) -> None: ...
    @property
    def hvac_mode(self) -> str: ...
    async def async_set_hvac_mode(self, hvac_mode: str) -> None: ...
    @property
    def target_temperature(self) -> None: ...
    @property
    def current_temperature(self) -> Union[float, None]: ...
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    @property
    def preset_mode(self) -> Union[str, None]: ...
    async def async_set_preset_mode(self, preset_mode: str) -> None: ...
