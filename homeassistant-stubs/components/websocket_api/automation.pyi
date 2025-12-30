from _typeshed import Incomplete
from collections.abc import Mapping
from dataclasses import dataclass
from enum import StrEnum
from homeassistant.const import CONF_TARGET as CONF_TARGET
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import entity_sources as entity_sources, get_device_class as get_device_class, get_supported_features as get_supported_features
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.util.hass_dict import HassKey as HassKey
from typing import Any, Self

_LOGGER: Incomplete
FLATTENED_SERVICE_DESCRIPTIONS_CACHE: HassKey[tuple[dict[str, dict[str, Any]], dict[str, dict[str, Any]]]]
AUTOMATION_COMPONENT_LOOKUP_CACHE: HassKey[dict[AutomationComponentType, tuple[Mapping[str, Any], _AutomationComponentLookupTable]]]

class AutomationComponentType(StrEnum):
    TRIGGERS = 'triggers'
    CONDITIONS = 'conditions'
    SERVICES = 'services'

@dataclass(slots=True, kw_only=True)
class _EntityFilter:
    integration: str | None
    domains: set[str]
    device_classes: set[str]
    supported_features: set[int]
    def matches(self, hass: HomeAssistant, entity_id: str, domain: str, integration: str) -> bool: ...

@dataclass(slots=True, kw_only=True)
class _AutomationComponentLookupData:
    component: str
    filters: list[_EntityFilter]
    @classmethod
    def create(cls, component: str, target_description: dict[str, Any]) -> Self: ...
    def matches(self, hass: HomeAssistant, entity_id: str, domain: str, integration: str) -> bool: ...

@dataclass(slots=True, kw_only=True)
class _AutomationComponentLookupTable:
    domain_components: dict[str | None, list[_AutomationComponentLookupData]]
    component_count: int

def _get_automation_component_domains(target_description: dict[str, Any]) -> set[str | None]: ...
def _get_automation_component_lookup_table(hass: HomeAssistant, component_type: AutomationComponentType, component_descriptions: Mapping[str, Mapping[str, Any] | None]) -> _AutomationComponentLookupTable: ...
def _async_get_automation_components_for_target(hass: HomeAssistant, component_type: AutomationComponentType, target_selection: ConfigType, expand_group: bool, component_descriptions: Mapping[str, Mapping[str, Any] | None]) -> set[str]: ...
async def async_get_triggers_for_target(hass: HomeAssistant, target_selector: ConfigType, expand_group: bool) -> set[str]: ...
async def async_get_conditions_for_target(hass: HomeAssistant, target_selector: ConfigType, expand_group: bool) -> set[str]: ...
async def async_get_services_for_target(hass: HomeAssistant, target_selector: ConfigType, expand_group: bool) -> set[str]: ...
