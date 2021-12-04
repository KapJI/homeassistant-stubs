from .const import CONF_RESPOND_TO_READ as CONF_RESPOND_TO_READ, CONF_STATE_ADDRESS as CONF_STATE_ADDRESS, DATA_KNX_CONFIG as DATA_KNX_CONFIG, DOMAIN as DOMAIN, KNX_ADDRESS as KNX_ADDRESS
from .knx_entity import KnxEntity as KnxEntity
from .schema import NumberSchema as NumberSchema
from homeassistant import config_entries as config_entries
from homeassistant.components.number import NumberEntity as NumberEntity
from homeassistant.const import CONF_ENTITY_CATEGORY as CONF_ENTITY_CATEGORY, CONF_MODE as CONF_MODE, CONF_NAME as CONF_NAME, CONF_TYPE as CONF_TYPE, Platform as Platform, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any
from xknx import XKNX as XKNX
from xknx.devices import NumericValue

async def async_setup_entry(hass: HomeAssistant, config_entry: config_entries.ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
def _create_numeric_value(xknx: XKNX, config: ConfigType) -> NumericValue: ...

class KNXNumber(KnxEntity, NumberEntity, RestoreEntity):
    _device: NumericValue
    _attr_max_value: Any
    _attr_min_value: Any
    _attr_mode: Any
    _attr_step: Any
    _attr_entity_category: Any
    _attr_unique_id: Any
    _attr_unit_of_measurement: Any
    def __init__(self, xknx: XKNX, config: ConfigType) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @property
    def value(self) -> float: ...
    async def async_set_value(self, value: float) -> None: ...
