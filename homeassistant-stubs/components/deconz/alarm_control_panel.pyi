from .deconz_device import DeconzDevice as DeconzDevice
from .gateway import DeconzGateway as DeconzGateway, get_gateway_from_config_entry as get_gateway_from_config_entry
from _typeshed import Incomplete
from homeassistant.components.alarm_control_panel import AlarmControlPanelEntity as AlarmControlPanelEntity, AlarmControlPanelEntityFeature as AlarmControlPanelEntityFeature, CodeFormat as CodeFormat, DOMAIN as DOMAIN
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import STATE_ALARM_ARMED_AWAY as STATE_ALARM_ARMED_AWAY, STATE_ALARM_ARMED_HOME as STATE_ALARM_ARMED_HOME, STATE_ALARM_ARMED_NIGHT as STATE_ALARM_ARMED_NIGHT, STATE_ALARM_ARMING as STATE_ALARM_ARMING, STATE_ALARM_DISARMED as STATE_ALARM_DISARMED, STATE_ALARM_PENDING as STATE_ALARM_PENDING, STATE_ALARM_TRIGGERED as STATE_ALARM_TRIGGERED
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pydeconz.models.alarm_system import AlarmSystem as AlarmSystem
from pydeconz.models.sensor.ancillary_control import AncillaryControl as AncillaryControl

DECONZ_TO_ALARM_STATE: Incomplete

def get_alarm_system_for_unique_id(gateway: DeconzGateway, unique_id: str) -> Union[AlarmSystem, None]: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DeconzAlarmControlPanel(DeconzDevice, AlarmControlPanelEntity):
    TYPE: Incomplete
    _device: AncillaryControl
    _attr_code_format: Incomplete
    _attr_supported_features: Incomplete
    alarm_system: Incomplete
    def __init__(self, device: AncillaryControl, gateway: DeconzGateway, alarm_system: AlarmSystem) -> None: ...
    def async_update_callback(self) -> None: ...
    @property
    def state(self) -> Union[str, None]: ...
    async def async_alarm_arm_away(self, code: Union[str, None] = ...) -> None: ...
    async def async_alarm_arm_home(self, code: Union[str, None] = ...) -> None: ...
    async def async_alarm_arm_night(self, code: Union[str, None] = ...) -> None: ...
    async def async_alarm_disarm(self, code: Union[str, None] = ...) -> None: ...
