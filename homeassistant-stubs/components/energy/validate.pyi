from . import data as data
from .const import DOMAIN as DOMAIN
from homeassistant.components import recorder as recorder, sensor as sensor
from homeassistant.const import ENERGY_KILO_WATT_HOUR as ENERGY_KILO_WATT_HOUR, ENERGY_WATT_HOUR as ENERGY_WATT_HOUR, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback, valid_entity_id as valid_entity_id
from typing import Any

class ValidationIssue:
    type: str
    identifier: str
    value: Union[Any, None]

class EnergyPreferencesValidation:
    energy_sources: list[list[ValidationIssue]]
    device_consumption: list[list[ValidationIssue]]
    def as_dict(self) -> dict: ...

def _async_validate_energy_stat(hass: HomeAssistant, stat_value: str, result: list[ValidationIssue]) -> None: ...
def _async_validate_price_entity(hass: HomeAssistant, entity_id: str, result: list[ValidationIssue]) -> None: ...
def _async_validate_cost_stat(hass: HomeAssistant, stat_id: str, result: list[ValidationIssue]) -> None: ...
def _async_validate_cost_entity(hass: HomeAssistant, entity_id: str, result: list[ValidationIssue]) -> None: ...
async def async_validate(hass: HomeAssistant) -> EnergyPreferencesValidation: ...
