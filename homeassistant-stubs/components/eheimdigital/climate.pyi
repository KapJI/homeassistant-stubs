from .const import HEATER_BIO_MODE as HEATER_BIO_MODE, HEATER_PRESET_TO_HEATER_MODE as HEATER_PRESET_TO_HEATER_MODE, HEATER_SMART_MODE as HEATER_SMART_MODE
from .coordinator import EheimDigitalConfigEntry as EheimDigitalConfigEntry, EheimDigitalUpdateCoordinator as EheimDigitalUpdateCoordinator
from .entity import EheimDigitalEntity as EheimDigitalEntity
from _typeshed import Incomplete
from eheimdigital.device import EheimDigitalDevice as EheimDigitalDevice
from eheimdigital.heater import EheimDigitalHeater
from homeassistant.components.climate import ClimateEntity as ClimateEntity, ClimateEntityFeature as ClimateEntityFeature, HVACAction as HVACAction, HVACMode as HVACMode, PRESET_NONE as PRESET_NONE
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, PRECISION_HALVES as PRECISION_HALVES, PRECISION_TENTHS as PRECISION_TENTHS, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: EheimDigitalConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class EheimDigitalHeaterClimate(EheimDigitalEntity[EheimDigitalHeater], ClimateEntity):
    _attr_hvac_modes: Incomplete
    _attr_hvac_mode: Incomplete
    _attr_precision = PRECISION_TENTHS
    _attr_supported_features: Incomplete
    _attr_target_temperature_step = PRECISION_HALVES
    _attr_preset_modes: Incomplete
    _attr_temperature_unit: Incomplete
    _attr_preset_mode = PRESET_NONE
    _attr_translation_key: str
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: EheimDigitalUpdateCoordinator, device: EheimDigitalHeater) -> None: ...
    async def async_set_preset_mode(self, preset_mode: str) -> None: ...
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    _attr_min_temp: int
    _attr_max_temp: int
    _attr_current_temperature: Incomplete
    _attr_target_temperature: Incomplete
    _attr_hvac_action: Incomplete
    def _async_update_attrs(self) -> None: ...
