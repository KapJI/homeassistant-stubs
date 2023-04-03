from .const import ATTR_COUNTER as ATTR_COUNTER, ATTR_SOURCE as ATTR_SOURCE, DATA_KNX_CONFIG as DATA_KNX_CONFIG, DOMAIN as DOMAIN
from .knx_entity import KnxEntity as KnxEntity
from .schema import BinarySensorSchema as BinarySensorSchema
from _typeshed import Incomplete
from homeassistant import config_entries as config_entries
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity
from homeassistant.const import CONF_DEVICE_CLASS as CONF_DEVICE_CLASS, CONF_ENTITY_CATEGORY as CONF_ENTITY_CATEGORY, CONF_NAME as CONF_NAME, Platform as Platform, STATE_ON as STATE_ON, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any
from xknx import XKNX as XKNX
from xknx.devices import BinarySensor as XknxBinarySensor

async def async_setup_entry(hass: HomeAssistant, config_entry: config_entries.ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class KNXBinarySensor(KnxEntity, BinarySensorEntity, RestoreEntity):
    _device: XknxBinarySensor
    _attr_entity_category: Incomplete
    _attr_device_class: Incomplete
    _attr_force_update: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, xknx: XKNX, config: ConfigType) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @property
    def is_on(self) -> bool: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any] | None: ...
