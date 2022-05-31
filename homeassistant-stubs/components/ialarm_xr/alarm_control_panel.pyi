from . import IAlarmXRDataUpdateCoordinator as IAlarmXRDataUpdateCoordinator
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.alarm_control_panel import AlarmControlPanelEntity as AlarmControlPanelEntity, AlarmControlPanelEntityFeature as AlarmControlPanelEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import STATE_ALARM_ARMED_AWAY as STATE_ALARM_ARMED_AWAY, STATE_ALARM_ARMED_HOME as STATE_ALARM_ARMED_HOME, STATE_ALARM_DISARMED as STATE_ALARM_DISARMED, STATE_ALARM_TRIGGERED as STATE_ALARM_TRIGGERED
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import device_registry as device_registry
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

IALARMXR_TO_HASS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class IAlarmXRPanel(CoordinatorEntity[IAlarmXRDataUpdateCoordinator], AlarmControlPanelEntity):
    _attr_supported_features: Incomplete
    _attr_name: str
    _attr_icon: str
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: IAlarmXRDataUpdateCoordinator) -> None: ...
    @property
    def state(self) -> Union[str, None]: ...
    def alarm_disarm(self, code: Union[str, None] = ...) -> None: ...
    def alarm_arm_home(self, code: Union[str, None] = ...) -> None: ...
    def alarm_arm_away(self, code: Union[str, None] = ...) -> None: ...
