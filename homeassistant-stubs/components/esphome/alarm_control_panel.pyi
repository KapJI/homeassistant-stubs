from .entity import EsphomeEntity as EsphomeEntity, convert_api_error_ha_error as convert_api_error_ha_error, esphome_state_property as esphome_state_property, platform_async_setup_entry as platform_async_setup_entry
from .enum_mapper import EsphomeEnumMapper as EsphomeEnumMapper
from _typeshed import Incomplete
from aioesphomeapi import APIIntEnum, AlarmControlPanelEntityState, AlarmControlPanelInfo, AlarmControlPanelState, EntityInfo as EntityInfo
from homeassistant.components.alarm_control_panel import AlarmControlPanelEntity as AlarmControlPanelEntity, AlarmControlPanelEntityFeature as AlarmControlPanelEntityFeature, CodeFormat as CodeFormat
from homeassistant.const import STATE_ALARM_ARMED_AWAY as STATE_ALARM_ARMED_AWAY, STATE_ALARM_ARMED_CUSTOM_BYPASS as STATE_ALARM_ARMED_CUSTOM_BYPASS, STATE_ALARM_ARMED_HOME as STATE_ALARM_ARMED_HOME, STATE_ALARM_ARMED_NIGHT as STATE_ALARM_ARMED_NIGHT, STATE_ALARM_ARMED_VACATION as STATE_ALARM_ARMED_VACATION, STATE_ALARM_ARMING as STATE_ALARM_ARMING, STATE_ALARM_DISARMED as STATE_ALARM_DISARMED, STATE_ALARM_DISARMING as STATE_ALARM_DISARMING, STATE_ALARM_PENDING as STATE_ALARM_PENDING, STATE_ALARM_TRIGGERED as STATE_ALARM_TRIGGERED
from homeassistant.core import callback as callback

_ESPHOME_ACP_STATE_TO_HASS_STATE: EsphomeEnumMapper[AlarmControlPanelState, str]

class EspHomeACPFeatures(APIIntEnum):
    ARM_HOME: int
    ARM_AWAY: int
    ARM_NIGHT: int
    TRIGGER: int
    ARM_CUSTOM_BYPASS: int
    ARM_VACATION: int

class EsphomeAlarmControlPanel(EsphomeEntity[AlarmControlPanelInfo, AlarmControlPanelEntityState], AlarmControlPanelEntity):
    _attr_supported_features: Incomplete
    _attr_code_format: Incomplete
    _attr_code_arm_required: Incomplete
    def _on_static_info_update(self, static_info: EntityInfo) -> None: ...
    @property
    def state(self) -> str | None: ...
    async def async_alarm_disarm(self, code: str | None = None) -> None: ...
    async def async_alarm_arm_home(self, code: str | None = None) -> None: ...
    async def async_alarm_arm_away(self, code: str | None = None) -> None: ...
    async def async_alarm_arm_night(self, code: str | None = None) -> None: ...
    async def async_alarm_arm_custom_bypass(self, code: str | None = None) -> None: ...
    async def async_alarm_arm_vacation(self, code: str | None = None) -> None: ...
    async def async_alarm_trigger(self, code: str | None = None) -> None: ...

async_setup_entry: Incomplete
