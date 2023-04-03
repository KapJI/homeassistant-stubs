from . import data as data
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Mapping, Sequence
from homeassistant.components import recorder as recorder, sensor as sensor
from homeassistant.const import ATTR_DEVICE_CLASS as ATTR_DEVICE_CLASS, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN, UnitOfEnergy as UnitOfEnergy, UnitOfVolume as UnitOfVolume
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback, valid_entity_id as valid_entity_id

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

def _get_placeholders(hass: HomeAssistant, issue_type: str) -> dict[str, str] | None: ...

class ValidationIssue:
    type: str
    affected_entities: set[tuple[str, float | str | None]]
    translation_placeholders: dict[str, str] | None
    def __init__(self, type, affected_entities, translation_placeholders) -> None: ...

class ValidationIssues:
    issues: dict[str, ValidationIssue]
    def __init__(self) -> None: ...
    def add_issue(self, hass: HomeAssistant, issue_type: str, affected_entity: str, detail: float | str | None = ...) -> None: ...

class EnergyPreferencesValidation:
    energy_sources: list[ValidationIssues]
    device_consumption: list[ValidationIssues]
    def as_dict(self) -> dict: ...
    def __init__(self, energy_sources, device_consumption) -> None: ...

def _async_validate_usage_stat(hass: HomeAssistant, metadata: dict[str, tuple[int, recorder.models.StatisticMetaData]], stat_id: str, allowed_device_classes: Sequence[str], allowed_units: Mapping[str, Sequence[str]], unit_error: str, issues: ValidationIssues) -> None: ...
def _async_validate_price_entity(hass: HomeAssistant, entity_id: str, issues: ValidationIssues, allowed_units: tuple[str, ...], unit_error: str) -> None: ...
def _async_validate_cost_stat(hass: HomeAssistant, metadata: dict[str, tuple[int, recorder.models.StatisticMetaData]], stat_id: str, issues: ValidationIssues) -> None: ...
def _async_validate_auto_generated_cost_entity(hass: HomeAssistant, energy_entity_id: str, issues: ValidationIssues) -> None: ...
async def async_validate(hass: HomeAssistant) -> EnergyPreferencesValidation: ...
