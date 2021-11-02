from .const import CONF_RESPOND_TO_READ as CONF_RESPOND_TO_READ, CONF_STATE_ADDRESS as CONF_STATE_ADDRESS, CONF_SYNC_STATE as CONF_SYNC_STATE, DOMAIN as DOMAIN, KNX_ADDRESS as KNX_ADDRESS
from .knx_entity import KnxEntity as KnxEntity
from .schema import SelectSchema as SelectSchema
from homeassistant.components.select import SelectEntity as SelectEntity
from homeassistant.const import CONF_NAME as CONF_NAME, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any
from xknx import XKNX as XKNX
from xknx.devices import Device as XknxDevice, RawValue

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: Union[DiscoveryInfoType, None] = ...) -> None: ...
def _create_raw_value(xknx: XKNX, config: ConfigType) -> RawValue: ...

class KNXSelect(KnxEntity, SelectEntity, RestoreEntity):
    _device: RawValue
    _option_payloads: Any
    _attr_options: Any
    _attr_current_option: Any
    _attr_unique_id: Any
    def __init__(self, xknx: XKNX, config: ConfigType) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def after_update_callback(self, device: XknxDevice) -> None: ...
    def option_from_payload(self, payload: Union[int, None]) -> Union[str, None]: ...
    async def async_select_option(self, option: str) -> None: ...
