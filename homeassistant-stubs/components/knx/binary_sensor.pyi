from . import KNXModule as KNXModule
from .const import ATTR_COUNTER as ATTR_COUNTER, ATTR_SOURCE as ATTR_SOURCE, CONF_CONTEXT_TIMEOUT as CONF_CONTEXT_TIMEOUT, CONF_IGNORE_INTERNAL_STATE as CONF_IGNORE_INTERNAL_STATE, CONF_INVERT as CONF_INVERT, CONF_RESET_AFTER as CONF_RESET_AFTER, CONF_STATE_ADDRESS as CONF_STATE_ADDRESS, CONF_SYNC_STATE as CONF_SYNC_STATE, DOMAIN as DOMAIN, KNX_MODULE_KEY as KNX_MODULE_KEY
from .entity import KnxUiEntity as KnxUiEntity, KnxUiEntityPlatformController as KnxUiEntityPlatformController, KnxYamlEntity as KnxYamlEntity
from .storage.const import CONF_ENTITY as CONF_ENTITY, CONF_GA_PASSIVE as CONF_GA_PASSIVE, CONF_GA_SENSOR as CONF_GA_SENSOR, CONF_GA_STATE as CONF_GA_STATE
from _typeshed import Incomplete
from homeassistant import config_entries as config_entries
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity
from homeassistant.const import CONF_DEVICE_CLASS as CONF_DEVICE_CLASS, CONF_ENTITY_CATEGORY as CONF_ENTITY_CATEGORY, CONF_NAME as CONF_NAME, Platform as Platform, STATE_ON as STATE_ON, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback, async_get_current_platform as async_get_current_platform
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any
from xknx.devices import BinarySensor as XknxBinarySensor

async def async_setup_entry(hass: HomeAssistant, config_entry: config_entries.ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class _KnxBinarySensor(BinarySensorEntity, RestoreEntity):
    _device: XknxBinarySensor
    async def async_added_to_hass(self) -> None: ...
    @property
    def is_on(self) -> bool: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any] | None: ...

class KnxYamlBinarySensor(_KnxBinarySensor, KnxYamlEntity):
    _device: XknxBinarySensor
    _attr_entity_category: Incomplete
    _attr_device_class: Incomplete
    _attr_force_update: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, knx_module: KNXModule, config: ConfigType) -> None: ...

class KnxUiBinarySensor(_KnxBinarySensor, KnxUiEntity):
    _device: XknxBinarySensor
    _attr_force_update: Incomplete
    def __init__(self, knx_module: KNXModule, unique_id: str, config: dict[str, Any]) -> None: ...
