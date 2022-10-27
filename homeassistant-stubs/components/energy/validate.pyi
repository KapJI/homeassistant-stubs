from . import data as data
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Mapping, Sequence
from homeassistant.components import recorder as recorder, sensor as sensor
from homeassistant.const import ATTR_DEVICE_CLASS as ATTR_DEVICE_CLASS, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN, UnitOfEnergy as UnitOfEnergy, VOLUME_CUBIC_FEET as VOLUME_CUBIC_FEET, VOLUME_CUBIC_METERS as VOLUME_CUBIC_METERS, VOLUME_GALLONS as VOLUME_GALLONS, VOLUME_LITERS as VOLUME_LITERS
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback, valid_entity_id as valid_entity_id
from typing import Any

ENERGY_USAGE_DEVICE_CLASSES: Incomplete
ENERGY_USAGE_UNITS: Incomplete
ENERGY_PRICE_UNITS: Incomplete
ENERGY_UNIT_ERROR: str
ENERGY_PRICE_UNIT_ERROR: str
GAS_USAGE_DEVICE_CLASSES: Incomplete
GAS_USAGE_UNITS: Incomplete
GAS_PRICE_UNITS: Incomplete
GAS_UNIT_ERROR: str
GAS_PRICE_UNIT_ERROR: str
WATER_USAGE_DEVICE_CLASSES: Incomplete
WATER_USAGE_UNITS: Incomplete
WATER_PRICE_UNITS: Incomplete
WATER_UNIT_ERROR: str
WATER_PRICE_UNIT_ERROR: str

class ValidationIssue:
    type: str
    identifier: str
    value: Union[Any, None]
    def __init__(self, type, identifier, value) -> None: ...

class EnergyPreferencesValidation:
    energy_sources: list[list[ValidationIssue]]
    device_consumption: list[list[ValidationIssue]]
    def as_dict(self) -> dict: ...
    def __init__(self, energy_sources, device_consumption) -> None: ...

def _async_validate_usage_stat(hass: HomeAssistant, metadata: dict[str, tuple[int, recorder.models.StatisticMetaData]], stat_id: str, allowed_device_classes: Sequence[str], allowed_units: Mapping[str, Sequence[str]], unit_error: str, result: list[ValidationIssue]) -> None: ...
def _async_validate_price_entity(hass: HomeAssistant, entity_id: str, result: list[ValidationIssue], allowed_units: tuple[str, ...], unit_error: str) -> None: ...
def _async_validate_cost_stat(hass: HomeAssistant, metadata: dict[str, tuple[int, recorder.models.StatisticMetaData]], stat_id: str, result: list[ValidationIssue]) -> None: ...
def _async_validate_auto_generated_cost_entity(hass: HomeAssistant, energy_entity_id: str, result: list[ValidationIssue]) -> None: ...
async def async_validate(hass: HomeAssistant) -> EnergyPreferencesValidation: ...
