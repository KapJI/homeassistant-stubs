from . import AbodeConfigEntry as AbodeConfigEntry
from .entity import AbodeDevice as AbodeDevice
from _typeshed import Incomplete
from homeassistant.components.alarm_control_panel import AlarmControlPanelEntity as AlarmControlPanelEntity, AlarmControlPanelEntityFeature as AlarmControlPanelEntityFeature, AlarmControlPanelState as AlarmControlPanelState
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from jaraco.abode.devices.alarm import Alarm as Alarm
from typing import override

async def async_setup_entry(hass: HomeAssistant, entry: AbodeConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class AbodeAlarm(AbodeDevice, AlarmControlPanelEntity):
    _attr_name: Incomplete
    _attr_code_arm_required: bool
    _attr_supported_features: Incomplete
    _device: Alarm
    @property
    @override
    def alarm_state(self) -> AlarmControlPanelState | None: ...
    @override
    def alarm_disarm(self, code: str | None = None) -> None: ...
    @override
    def alarm_arm_home(self, code: str | None = None) -> None: ...
    @override
    def alarm_arm_away(self, code: str | None = None) -> None: ...
    @property
    @override
    def extra_state_attributes(self) -> dict[str, str]: ...
