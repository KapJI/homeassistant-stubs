from .const import DATA_COORDINATOR as DATA_COORDINATOR, DOMAIN as DOMAIN
from .coordinator import CanaryDataUpdateCoordinator as CanaryDataUpdateCoordinator
from canary.api import Location as Location
from homeassistant.components.alarm_control_panel import AlarmControlPanelEntity as AlarmControlPanelEntity
from homeassistant.components.alarm_control_panel.const import SUPPORT_ALARM_ARM_AWAY as SUPPORT_ALARM_ARM_AWAY, SUPPORT_ALARM_ARM_HOME as SUPPORT_ALARM_ARM_HOME, SUPPORT_ALARM_ARM_NIGHT as SUPPORT_ALARM_ARM_NIGHT
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import STATE_ALARM_ARMED_AWAY as STATE_ALARM_ARMED_AWAY, STATE_ALARM_ARMED_HOME as STATE_ALARM_ARMED_HOME, STATE_ALARM_ARMED_NIGHT as STATE_ALARM_ARMED_NIGHT, STATE_ALARM_DISARMED as STATE_ALARM_DISARMED
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class CanaryAlarm(CoordinatorEntity, AlarmControlPanelEntity):
    coordinator: CanaryDataUpdateCoordinator
    _attr_supported_features: Any
    _location_id: Any
    _attr_name: Any
    _attr_unique_id: Any
    def __init__(self, coordinator: CanaryDataUpdateCoordinator, location: Location) -> None: ...
    @property
    def location(self) -> Location: ...
    @property
    def state(self) -> Union[str, None]: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
    def alarm_disarm(self, code: Union[str, None] = ...) -> None: ...
    def alarm_arm_home(self, code: Union[str, None] = ...) -> None: ...
    def alarm_arm_away(self, code: Union[str, None] = ...) -> None: ...
    def alarm_arm_night(self, code: Union[str, None] = ...) -> None: ...
