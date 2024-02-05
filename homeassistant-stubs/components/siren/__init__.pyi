from .const import ATTR_AVAILABLE_TONES as ATTR_AVAILABLE_TONES, ATTR_DURATION as ATTR_DURATION, ATTR_TONE as ATTR_TONE, ATTR_VOLUME_LEVEL as ATTR_VOLUME_LEVEL, DOMAIN as DOMAIN, SirenEntityFeature as SirenEntityFeature, _DEPRECATED_SUPPORT_DURATION as _DEPRECATED_SUPPORT_DURATION, _DEPRECATED_SUPPORT_TONES as _DEPRECATED_SUPPORT_TONES, _DEPRECATED_SUPPORT_TURN_OFF as _DEPRECATED_SUPPORT_TURN_OFF, _DEPRECATED_SUPPORT_TURN_ON as _DEPRECATED_SUPPORT_TURN_ON, _DEPRECATED_SUPPORT_VOLUME_SET as _DEPRECATED_SUPPORT_VOLUME_SET
from _typeshed import Incomplete
from functools import cached_property as cached_property
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import SERVICE_TOGGLE as SERVICE_TOGGLE, SERVICE_TURN_OFF as SERVICE_TURN_OFF, SERVICE_TURN_ON as SERVICE_TURN_ON
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall
from homeassistant.helpers.config_validation import PLATFORM_SCHEMA as PLATFORM_SCHEMA, PLATFORM_SCHEMA_BASE as PLATFORM_SCHEMA_BASE
from homeassistant.helpers.deprecation import all_with_deprecated_constants as all_with_deprecated_constants, check_if_deprecated_constant as check_if_deprecated_constant, dir_with_deprecated_constants as dir_with_deprecated_constants
from homeassistant.helpers.entity import ToggleEntity as ToggleEntity, ToggleEntityDescription as ToggleEntityDescription
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any, TypedDict

_LOGGER: Incomplete
SCAN_INTERVAL: Incomplete
TURN_ON_SCHEMA: Incomplete

class SirenTurnOnServiceParameters(TypedDict, total=False):
    tone: int | str
    duration: int
    volume_level: float

def process_turn_on_params(siren: SirenEntity, params: SirenTurnOnServiceParameters) -> SirenTurnOnServiceParameters: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class SirenEntityDescription(ToggleEntityDescription, frozen_or_thawed=True):
    available_tones: list[int | str] | dict[int, str] | None
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, available_tones) -> None: ...

CACHED_PROPERTIES_WITH_ATTR_: Incomplete

class SirenEntity(ToggleEntity, cached_properties=CACHED_PROPERTIES_WITH_ATTR_):
    _entity_component_unrecorded_attributes: Incomplete
    entity_description: SirenEntityDescription
    _attr_available_tones: list[int | str] | dict[int, str] | None
    _attr_supported_features: SirenEntityFeature
    @property
    def capability_attributes(self) -> dict[str, Any] | None: ...
    @cached_property
    def available_tones(self) -> list[int | str] | dict[int, str] | None: ...
    @cached_property
    def supported_features(self) -> SirenEntityFeature: ...

__getattr__: Incomplete
__dir__: Incomplete
__all__: Incomplete
