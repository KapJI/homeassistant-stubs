from .const import CONF_RESPOND_TO_READ as CONF_RESPOND_TO_READ, CONF_STATE_ADDRESS as CONF_STATE_ADDRESS, CONF_SYNC_STATE as CONF_SYNC_STATE, DATA_KNX_CONFIG as DATA_KNX_CONFIG, DOMAIN as DOMAIN, KNX_ADDRESS as KNX_ADDRESS
from .knx_entity import KnxEntity as KnxEntity
from _typeshed import Incomplete
from datetime import date as dt_date
from homeassistant import config_entries as config_entries
from homeassistant.components.date import DateEntity as DateEntity
from homeassistant.const import CONF_ENTITY_CATEGORY as CONF_ENTITY_CATEGORY, CONF_NAME as CONF_NAME, Platform as Platform, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Final
from xknx import XKNX as XKNX
from xknx.devices import DateTime as XknxDateTime

_DATE_TRANSLATION_FORMAT: Final[str]

async def async_setup_entry(hass: HomeAssistant, config_entry: config_entries.ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
def _create_xknx_device(xknx: XKNX, config: ConfigType) -> XknxDateTime: ...

class KNXDate(KnxEntity, DateEntity, RestoreEntity):
    _device: XknxDateTime
    _attr_entity_category: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, xknx: XKNX, config: ConfigType) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @property
    def native_value(self) -> dt_date | None: ...
    async def async_set_value(self, value: dt_date) -> None: ...
