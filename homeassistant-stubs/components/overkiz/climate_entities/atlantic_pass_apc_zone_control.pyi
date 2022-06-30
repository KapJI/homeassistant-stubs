from _typeshed import Incomplete
from homeassistant.components.climate import ClimateEntity as ClimateEntity
from homeassistant.components.climate.const import HVACMode as HVACMode
from homeassistant.components.overkiz.entity import OverkizEntity as OverkizEntity
from homeassistant.const import TEMP_CELSIUS as TEMP_CELSIUS

OVERKIZ_TO_HVAC_MODE: dict[str, str]
HVAC_MODE_TO_OVERKIZ: Incomplete

class AtlanticPassAPCZoneControl(OverkizEntity, ClimateEntity):
    _attr_hvac_modes: Incomplete
    _attr_temperature_unit: Incomplete
    @property
    def hvac_mode(self) -> str: ...
    async def async_set_hvac_mode(self, hvac_mode: str) -> None: ...
