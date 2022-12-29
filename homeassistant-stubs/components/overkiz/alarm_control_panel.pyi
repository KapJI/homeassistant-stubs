from . import HomeAssistantOverkizData as HomeAssistantOverkizData
from .const import DOMAIN as DOMAIN
from .coordinator import OverkizDataUpdateCoordinator as OverkizDataUpdateCoordinator
from .entity import OverkizDescriptiveEntity as OverkizDescriptiveEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components.alarm_control_panel import AlarmControlPanelEntity as AlarmControlPanelEntity, AlarmControlPanelEntityDescription as AlarmControlPanelEntityDescription, AlarmControlPanelEntityFeature as AlarmControlPanelEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform, STATE_ALARM_ARMED_AWAY as STATE_ALARM_ARMED_AWAY, STATE_ALARM_ARMED_CUSTOM_BYPASS as STATE_ALARM_ARMED_CUSTOM_BYPASS, STATE_ALARM_ARMED_HOME as STATE_ALARM_ARMED_HOME, STATE_ALARM_ARMED_NIGHT as STATE_ALARM_ARMED_NIGHT, STATE_ALARM_DISARMED as STATE_ALARM_DISARMED, STATE_ALARM_PENDING as STATE_ALARM_PENDING, STATE_ALARM_TRIGGERED as STATE_ALARM_TRIGGERED
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pyoverkiz.types import StateType as OverkizStateType
from typing import Any

class OverkizAlarmDescriptionMixin:
    supported_features: AlarmControlPanelEntityFeature
    fn_state: Callable[[Callable[[str], OverkizStateType]], str]
    def __init__(self, supported_features, fn_state) -> None: ...

class OverkizAlarmDescription(AlarmControlPanelEntityDescription, OverkizAlarmDescriptionMixin):
    alarm_disarm: Union[str, None]
    alarm_disarm_args: Union[OverkizStateType, list[OverkizStateType]]
    alarm_arm_home: Union[str, None]
    alarm_arm_home_args: Union[OverkizStateType, list[OverkizStateType]]
    alarm_arm_night: Union[str, None]
    alarm_arm_night_args: Union[OverkizStateType, list[OverkizStateType]]
    alarm_arm_away: Union[str, None]
    alarm_arm_away_args: Union[OverkizStateType, list[OverkizStateType]]
    alarm_trigger: Union[str, None]
    alarm_trigger_args: Union[OverkizStateType, list[OverkizStateType]]
    def __init__(self, supported_features, fn_state, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, alarm_disarm, alarm_disarm_args, alarm_arm_home, alarm_arm_home_args, alarm_arm_night, alarm_arm_night_args, alarm_arm_away, alarm_arm_away_args, alarm_trigger, alarm_trigger_args) -> None: ...

MAP_INTERNAL_STATUS_STATE: dict[str, str]

def _state_tsk_alarm_controller(select_state: Callable[[str], OverkizStateType]) -> str: ...

MAP_CORE_ACTIVE_ZONES: dict[str, str]

def _state_stateful_alarm_controller(select_state: Callable[[str], OverkizStateType]) -> str: ...

MAP_MYFOX_STATUS_STATE: dict[str, str]

def _state_myfox_alarm_controller(select_state: Callable[[str], OverkizStateType]) -> str: ...

MAP_ARM_TYPE: dict[str, str]

def _state_alarm_panel_controller(select_state: Callable[[str], OverkizStateType]) -> str: ...

ALARM_DESCRIPTIONS: list[OverkizAlarmDescription]
SUPPORTED_DEVICES: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class OverkizAlarmControlPanel(OverkizDescriptiveEntity, AlarmControlPanelEntity):
    entity_description: OverkizAlarmDescription
    _attr_supported_features: Incomplete
    def __init__(self, device_url: str, coordinator: OverkizDataUpdateCoordinator, description: EntityDescription) -> None: ...
    @property
    def state(self) -> str: ...
    async def async_alarm_disarm(self, code: Union[str, None] = ...) -> None: ...
    async def async_alarm_arm_home(self, code: Union[str, None] = ...) -> None: ...
    async def async_alarm_arm_night(self, code: Union[str, None] = ...) -> None: ...
    async def async_alarm_arm_away(self, code: Union[str, None] = ...) -> None: ...
    async def async_alarm_trigger(self, code: Union[str, None] = ...) -> None: ...
    async def async_execute_command(self, command_name: str, args: Any) -> None: ...
