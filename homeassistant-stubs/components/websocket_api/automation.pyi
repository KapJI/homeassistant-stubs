from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.const import CONF_TARGET as CONF_TARGET
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import entity_sources as entity_sources, get_device_class as get_device_class, get_supported_features as get_supported_features
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any, Self

_LOGGER: Incomplete

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

def _get_automation_component_domains(target_description: dict[str, Any]) -> set[str | None]: ...
def _async_get_automation_components_for_target(hass: HomeAssistant, target_selection: ConfigType, expand_group: bool, component_descriptions: dict[str, dict[str, Any] | None]) -> set[str]: ...
async def async_get_triggers_for_target(hass: HomeAssistant, target_selector: ConfigType, expand_group: bool) -> set[str]: ...
async def async_get_conditions_for_target(hass: HomeAssistant, target_selector: ConfigType, expand_group: bool) -> set[str]: ...
async def async_get_services_for_target(hass: HomeAssistant, target_selector: ConfigType, expand_group: bool) -> set[str]: ...
