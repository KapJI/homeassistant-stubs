from .const import DOMAIN as DOMAIN, PRESET_MODES as PRESET_MODES
from .entity import VelbusEntity as VelbusEntity, api_call as api_call
from _typeshed import Incomplete
from homeassistant.components.climate import ClimateEntity as ClimateEntity, ClimateEntityFeature as ClimateEntityFeature, HVACMode as HVACMode
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any
from velbusaio.channels import Temperature as VelbusTemp

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class VelbusClimate(VelbusEntity, ClimateEntity):
    _channel: VelbusTemp
    _attr_supported_features: Incomplete
    _attr_temperature_unit: Incomplete
    _attr_hvac_mode: Incomplete
    _attr_hvac_modes: Incomplete
    _attr_preset_modes: Incomplete
    @property
    def target_temperature(self) -> float | None: ...
    @property
    def preset_mode(self) -> str | None: ...
    @property
    def current_temperature(self) -> int | None: ...
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    async def async_set_preset_mode(self, preset_mode: str) -> None: ...
