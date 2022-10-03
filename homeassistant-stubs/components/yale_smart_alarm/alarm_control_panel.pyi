from .const import COORDINATOR as COORDINATOR, DOMAIN as DOMAIN, STATE_MAP as STATE_MAP, YALE_ALL_ERRORS as YALE_ALL_ERRORS
from .coordinator import YaleDataUpdateCoordinator as YaleDataUpdateCoordinator
from .entity import YaleAlarmEntity as YaleAlarmEntity
from _typeshed import Incomplete
from homeassistant.components.alarm_control_panel import AlarmControlPanelEntity as AlarmControlPanelEntity, AlarmControlPanelEntityFeature as AlarmControlPanelEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class YaleAlarmDevice(YaleAlarmEntity, AlarmControlPanelEntity):
    _attr_code_arm_required: bool
    _attr_supported_features: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: YaleDataUpdateCoordinator) -> None: ...
    async def async_alarm_disarm(self, code: Union[str, None] = ...) -> None: ...
    async def async_alarm_arm_home(self, code: Union[str, None] = ...) -> None: ...
    async def async_alarm_arm_away(self, code: Union[str, None] = ...) -> None: ...
    async def async_set_alarm(self, command: str, code: Union[str, None] = ...) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def state(self) -> StateType: ...
