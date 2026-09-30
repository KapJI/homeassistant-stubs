from .const import BinarySensorDeviceClass as BinarySensorDeviceClass, DEVICE_CLASSES_SCHEMA as DEVICE_CLASSES_SCHEMA, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory, STATE_OFF as STATE_OFF, STATE_ON as STATE_ON
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity import Entity as Entity, EntityDescription as EntityDescription
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.util.hass_dict import HassKey as HassKey
from propcache.api import cached_property
from typing import Literal, final, override

_LOGGER: Incomplete
DATA_COMPONENT: HassKey[EntityComponent[BinarySensorEntity]]
ENTITY_ID_FORMAT: Incomplete
PLATFORM_SCHEMA: Incomplete
PLATFORM_SCHEMA_BASE: Incomplete
SCAN_INTERVAL: Incomplete
DEVICE_CLASSES: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class BinarySensorEntityDescription(EntityDescription, frozen_or_thawed=True):
    device_class: BinarySensorDeviceClass | None = ...

CACHED_PROPERTIES_WITH_ATTR_: Incomplete

class BinarySensorEntity(Entity, cached_properties=CACHED_PROPERTIES_WITH_ATTR_):
    entity_description: BinarySensorEntityDescription
    _attr_device_class: BinarySensorDeviceClass | None
    _attr_is_on: bool | None
    _attr_state: None
    @override
    async def async_internal_added_to_hass(self) -> None: ...
    @override
    def _default_to_device_class_name(self) -> bool: ...
    @cached_property
    @override
    def device_class(self) -> BinarySensorDeviceClass | None: ...
    @cached_property
    def is_on(self) -> bool | None: ...
    @final
    @property
    @override
    def state(self) -> Literal['on', 'off'] | None: ...
