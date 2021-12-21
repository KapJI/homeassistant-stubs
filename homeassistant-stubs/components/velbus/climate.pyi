from . import VelbusEntity as VelbusEntity
from .const import DOMAIN as DOMAIN, PRESET_MODES as PRESET_MODES
from homeassistant.components.climate import ClimateEntity as ClimateEntity
from homeassistant.components.climate.const import HVAC_MODE_HEAT as HVAC_MODE_HEAT, SUPPORT_PRESET_MODE as SUPPORT_PRESET_MODE, SUPPORT_TARGET_TEMPERATURE as SUPPORT_TARGET_TEMPERATURE
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, TEMP_CELSIUS as TEMP_CELSIUS
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any
from velbusaio.channels import Temperature as VelbusTemp

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class VelbusClimate(VelbusEntity, ClimateEntity):
    _channel: VelbusTemp
    _attr_supported_features: Any
    _attr_temperature_unit: Any
    _attr_hvac_mode: Any
    _attr_hvac_modes: Any
    _attr_preset_modes: Any
    @property
    def target_temperature(self) -> Union[float, None]: ...
    @property
    def preset_mode(self) -> Union[str, None]: ...
    @property
    def current_temperature(self) -> Union[int, None]: ...
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    async def async_set_preset_mode(self, preset_mode: str) -> None: ...
