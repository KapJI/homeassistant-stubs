from .const import CONF_SYNC_STATE as CONF_SYNC_STATE, DOMAIN as DOMAIN, FanConf as FanConf, KNX_ADDRESS as KNX_ADDRESS, KNX_MODULE_KEY as KNX_MODULE_KEY
from .entity import KnxUiEntity as KnxUiEntity, KnxUiEntityPlatformController as KnxUiEntityPlatformController, KnxYamlEntity as KnxYamlEntity
from .knx_module import KNXModule as KNXModule
from .schema import FanSchema as FanSchema
from .storage.const import CONF_ENTITY as CONF_ENTITY, CONF_GA_OSCILLATION as CONF_GA_OSCILLATION, CONF_GA_SPEED as CONF_GA_SPEED, CONF_GA_STEP as CONF_GA_STEP, CONF_GA_SWITCH as CONF_GA_SWITCH, CONF_SPEED as CONF_SPEED
from .storage.util import ConfigExtractor as ConfigExtractor
from _typeshed import Incomplete
from homeassistant import config_entries as config_entries
from homeassistant.components.fan import FanEntity as FanEntity, FanEntityFeature as FanEntityFeature
from homeassistant.const import CONF_ENTITY_CATEGORY as CONF_ENTITY_CATEGORY, CONF_NAME as CONF_NAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback, async_get_current_platform as async_get_current_platform
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.util.percentage import percentage_to_ranged_value as percentage_to_ranged_value, ranged_value_to_percentage as ranged_value_to_percentage
from homeassistant.util.scaling import int_states_in_range as int_states_in_range
from propcache.api import cached_property
from typing import Any
from xknx.devices import Fan as XknxFan

async def async_setup_entry(hass: HomeAssistant, config_entry: config_entries.ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class _KnxFan(FanEntity):
    _device: XknxFan
    _step_range: tuple[int, int] | None
    def _get_knx_speed(self, percentage: int) -> int: ...
    async def async_set_percentage(self, percentage: int) -> None: ...
    @cached_property
    def supported_features(self) -> FanEntityFeature: ...
    @property
    def percentage(self) -> int | None: ...
    @cached_property
    def speed_count(self) -> int: ...
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, percentage: int | None = None, preset_mode: str | None = None, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_oscillate(self, oscillating: bool) -> None: ...
    @property
    def oscillating(self) -> bool | None: ...

class KnxYamlFan(_KnxFan, KnxYamlEntity):
    _device: XknxFan
    _step_range: tuple[int, int] | None
    _attr_entity_category: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, knx_module: KNXModule, config: ConfigType) -> None: ...

class KnxUiFan(_KnxFan, KnxUiEntity):
    _device: XknxFan
    _step_range: tuple[int, int] | None
    def __init__(self, knx_module: KNXModule, unique_id: str, config: dict[str, Any]) -> None: ...
