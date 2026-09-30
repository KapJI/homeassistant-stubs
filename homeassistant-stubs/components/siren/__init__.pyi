from .const import ATTR_AVAILABLE_TONES as ATTR_AVAILABLE_TONES, ATTR_DURATION as ATTR_DURATION, ATTR_TONE as ATTR_TONE, ATTR_VOLUME_LEVEL as ATTR_VOLUME_LEVEL, DATA_COMPONENT as DATA_COMPONENT, DOMAIN as DOMAIN, SirenEntityCapabilityAttribute as SirenEntityCapabilityAttribute, SirenEntityFeature as SirenEntityFeature
from .services import SirenTurnOnServiceParameters as SirenTurnOnServiceParameters, TURN_ON_SCHEMA as TURN_ON_SCHEMA, async_setup_services as async_setup_services, process_turn_on_params as process_turn_on_params
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import SERVICE_TOGGLE as SERVICE_TOGGLE, SERVICE_TURN_OFF as SERVICE_TURN_OFF, SERVICE_TURN_ON as SERVICE_TURN_ON
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import ToggleEntity as ToggleEntity, ToggleEntityDescription as ToggleEntityDescription
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.typing import ConfigType as ConfigType
from propcache.api import cached_property
from typing import Any, final, override

_LOGGER: Incomplete
PLATFORM_SCHEMA: Incomplete
PLATFORM_SCHEMA_BASE: Incomplete
SCAN_INTERVAL: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class SirenEntityDescription(ToggleEntityDescription, frozen_or_thawed=True):
    available_tones: list[int | str] | dict[int, str] | None = ...

CACHED_PROPERTIES_WITH_ATTR_: Incomplete

class SirenEntity(ToggleEntity, cached_properties=CACHED_PROPERTIES_WITH_ATTR_):
    _entity_component_unrecorded_attributes: Incomplete
    entity_description: SirenEntityDescription
    _attr_available_tones: list[int | str] | dict[int, str] | None
    _attr_supported_features: SirenEntityFeature
    @final
    @property
    @override
    def capability_attributes(self) -> dict[str, Any] | None: ...
    @cached_property
    def available_tones(self) -> list[int | str] | dict[int, str] | None: ...
    @cached_property
    @override
    def supported_features(self) -> SirenEntityFeature: ...
