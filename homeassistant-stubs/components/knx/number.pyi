from .const import CONF_RESPOND_TO_READ as CONF_RESPOND_TO_READ, CONF_STATE_ADDRESS as CONF_STATE_ADDRESS, CONF_SYNC_STATE as CONF_SYNC_STATE, DOMAIN as DOMAIN, KNX_ADDRESS as KNX_ADDRESS, KNX_MODULE_KEY as KNX_MODULE_KEY, NumberConf as NumberConf
from .dpt import get_supported_dpts as get_supported_dpts
from .entity import KnxUiEntity as KnxUiEntity, KnxUiEntityPlatformController as KnxUiEntityPlatformController, KnxYamlEntity as KnxYamlEntity
from .knx_module import KNXModule as KNXModule
from .storage.const import CONF_ENTITY as CONF_ENTITY, CONF_GA_SENSOR as CONF_GA_SENSOR
from .storage.util import ConfigExtractor as ConfigExtractor
from _typeshed import Incomplete
from homeassistant import config_entries as config_entries
from homeassistant.components.number import NumberDeviceClass as NumberDeviceClass, NumberMode as NumberMode, RestoreNumber as RestoreNumber
from homeassistant.const import CONF_DEVICE_CLASS as CONF_DEVICE_CLASS, CONF_ENTITY_CATEGORY as CONF_ENTITY_CATEGORY, CONF_MODE as CONF_MODE, CONF_NAME as CONF_NAME, CONF_TYPE as CONF_TYPE, CONF_UNIT_OF_MEASUREMENT as CONF_UNIT_OF_MEASUREMENT, Platform as Platform, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback, async_get_current_platform as async_get_current_platform
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.util.enum import try_parse_enum as try_parse_enum
from xknx.devices import NumericValue

async def async_setup_entry(hass: HomeAssistant, config_entry: config_entries.ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class _KnxNumber(RestoreNumber):
    _device: NumericValue
    async def async_added_to_hass(self) -> None: ...
    @property
    def native_value(self) -> float: ...
    async def async_set_native_value(self, value: float) -> None: ...

class KnxYamlNumber(_KnxNumber, KnxYamlEntity):
    _device: NumericValue
    _attr_native_max_value: Incomplete
    _attr_native_min_value: Incomplete
    _attr_mode: Incomplete
    _attr_native_step: Incomplete
    _attr_entity_category: Incomplete
    _attr_unique_id: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    def __init__(self, knx_module: KNXModule, config: ConfigType) -> None: ...

class KnxUiNumber(_KnxNumber, KnxUiEntity):
    _device: NumericValue
    _attr_device_class: Incomplete
    _attr_mode: Incomplete
    _attr_native_max_value: Incomplete
    _attr_native_min_value: Incomplete
    _attr_native_step: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    def __init__(self, knx_module: KNXModule, unique_id: str, config: ConfigType) -> None: ...
