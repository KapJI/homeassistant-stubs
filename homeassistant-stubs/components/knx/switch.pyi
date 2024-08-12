from . import KNXModule as KNXModule
from .const import CONF_INVERT as CONF_INVERT, CONF_RESPOND_TO_READ as CONF_RESPOND_TO_READ, CONF_SYNC_STATE as CONF_SYNC_STATE, DATA_KNX_CONFIG as DATA_KNX_CONFIG, DOMAIN as DOMAIN, KNX_ADDRESS as KNX_ADDRESS
from .knx_entity import KnxEntity as KnxEntity
from .schema import SwitchSchema as SwitchSchema
from .storage.const import CONF_DEVICE_INFO as CONF_DEVICE_INFO, CONF_ENTITY as CONF_ENTITY, CONF_GA_PASSIVE as CONF_GA_PASSIVE, CONF_GA_STATE as CONF_GA_STATE, CONF_GA_SWITCH as CONF_GA_SWITCH, CONF_GA_WRITE as CONF_GA_WRITE
from _typeshed import Incomplete
from homeassistant import config_entries as config_entries
from homeassistant.components.switch import SwitchEntity as SwitchEntity
from homeassistant.const import CONF_DEVICE_CLASS as CONF_DEVICE_CLASS, CONF_ENTITY_CATEGORY as CONF_ENTITY_CATEGORY, CONF_NAME as CONF_NAME, Platform as Platform, STATE_ON as STATE_ON, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any
from xknx import XKNX as XKNX
from xknx.devices import Switch as XknxSwitch

async def async_setup_entry(hass: HomeAssistant, config_entry: config_entries.ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class _KnxSwitch(KnxEntity, SwitchEntity, RestoreEntity):
    _device: XknxSwitch
    async def async_added_to_hass(self) -> None: ...
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...

class KnxYamlSwitch(_KnxSwitch):
    _attr_entity_category: Incomplete
    _attr_device_class: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, xknx: XKNX, config: ConfigType) -> None: ...

class KnxUiSwitch(_KnxSwitch):
    _attr_has_entity_name: bool
    _attr_entity_category: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, knx_module: KNXModule, unique_id: str, config: dict[str, Any]) -> None: ...
