from .const import DOMAIN as DOMAIN, LawnMowerActivity as LawnMowerActivity, LawnMowerEntityFeature as LawnMowerEntityFeature, SERVICE_DOCK as SERVICE_DOCK, SERVICE_PAUSE as SERVICE_PAUSE, SERVICE_START_MOWING as SERVICE_START_MOWING
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import Entity as Entity, EntityDescription as EntityDescription
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.util.hass_dict import HassKey as HassKey
from propcache import cached_property

_LOGGER: Incomplete
DATA_COMPONENT: HassKey[EntityComponent[LawnMowerEntity]]
PLATFORM_SCHEMA: Incomplete
PLATFORM_SCHEMA_BASE: Incomplete
SCAN_INTERVAL: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class LawnMowerEntityEntityDescription(EntityDescription, frozen_or_thawed=True):
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=...) -> None: ...

CACHED_PROPERTIES_WITH_ATTR_: Incomplete

class LawnMowerEntity(Entity, cached_properties=CACHED_PROPERTIES_WITH_ATTR_):
    entity_description: LawnMowerEntityEntityDescription
    _attr_activity: LawnMowerActivity | None
    _attr_supported_features: LawnMowerEntityFeature
    @property
    def state(self) -> str | None: ...
    @cached_property
    def activity(self) -> LawnMowerActivity | None: ...
    @cached_property
    def supported_features(self) -> LawnMowerEntityFeature: ...
    def start_mowing(self) -> None: ...
    async def async_start_mowing(self) -> None: ...
    def dock(self) -> None: ...
    async def async_dock(self) -> None: ...
    def pause(self) -> None: ...
    async def async_pause(self) -> None: ...
