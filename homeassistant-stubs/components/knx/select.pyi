from .const import CONF_PAYLOAD_LENGTH as CONF_PAYLOAD_LENGTH, CONF_RESPOND_TO_READ as CONF_RESPOND_TO_READ, CONF_STATE_ADDRESS as CONF_STATE_ADDRESS, CONF_SYNC_STATE as CONF_SYNC_STATE, CONF_VALUE as CONF_VALUE, DOMAIN as DOMAIN, KNX_ADDRESS as KNX_ADDRESS, KNX_MODULE_KEY as KNX_MODULE_KEY, SelectConf as SelectConf
from .dpt import raw_payload_length as raw_payload_length
from .entity import KnxUiEntity as KnxUiEntity, KnxUiEntityPlatformController as KnxUiEntityPlatformController, KnxYamlEntity as KnxYamlEntity, build_yaml_unique_id as build_yaml_unique_id
from .knx_module import KNXModule as KNXModule
from .storage.const import CONF_ENTITY as CONF_ENTITY
from .storage.util import ConfigExtractor as ConfigExtractor
from _typeshed import Incomplete
from homeassistant import config_entries as config_entries
from homeassistant.components.select import SelectEntity as SelectEntity
from homeassistant.const import CONF_NAME as CONF_NAME, CONF_PAYLOAD as CONF_PAYLOAD, Platform as Platform, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback, async_get_current_platform as async_get_current_platform
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import override
from xknx.devices import RawValue
from xknx.dpt import DPTBase

_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: config_entries.ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...
def _payload_from_value(transcoder: type[DPTBase], value: object) -> int: ...
def _options_from_enum_dpt(dpt: str) -> tuple[dict[str, int], int]: ...
def _options_from_custom_config(options: list[ConfigType], dpt: str | None) -> tuple[dict[str, int], int]: ...

class _KNXSelect(SelectEntity, RestoreEntity):
    _device: RawValue
    _option_payloads: dict[str, int]
    @override
    async def async_added_to_hass(self) -> None: ...
    @property
    @override
    def current_option(self) -> str | None: ...
    def option_from_payload(self, payload: int | None) -> str | None: ...
    @override
    async def async_select_option(self, option: str) -> None: ...

class KnxYamlSelect(_KNXSelect, KnxYamlEntity):
    _device: RawValue
    _option_payloads: Incomplete
    _attr_options: Incomplete
    def __init__(self, knx_module: KNXModule, config: ConfigType) -> None: ...

class KnxUiSelect(_KNXSelect, KnxUiEntity):
    _device: RawValue
    _attr_options: Incomplete
    def __init__(self, knx_module: KNXModule, unique_id: str, config: ConfigType) -> None: ...
