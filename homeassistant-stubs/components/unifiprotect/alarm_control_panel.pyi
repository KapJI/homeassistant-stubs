from .const import DOMAIN as DOMAIN
from .data import ProtectData as ProtectData, ProtectDeviceType as ProtectDeviceType, UFPConfigEntry as UFPConfigEntry
from .entity import ProtectNVREntity as ProtectNVREntity
from .utils import async_ufp_instance_command as async_ufp_instance_command
from _typeshed import Incomplete
from homeassistant.components.alarm_control_panel import AlarmControlPanelEntity as AlarmControlPanelEntity, AlarmControlPanelEntityFeature as AlarmControlPanelEntityFeature, AlarmControlPanelState as AlarmControlPanelState
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from uiprotect.data import NVR as NVR, NvrArmModeStatus

PARALLEL_UPDATES: int
_UIPROTECT_TO_HA: dict[NvrArmModeStatus, AlarmControlPanelState]

async def async_setup_entry(hass: HomeAssistant, entry: UFPConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class ProtectNVRAlarmControlPanel(ProtectNVREntity, AlarmControlPanelEntity):
    _attr_code_arm_required: bool
    _attr_supported_features: Incomplete
    _attr_translation_key: str
    _state_attrs: Incomplete
    def __init__(self, data: ProtectData, device: NVR) -> None: ...
    _attr_available: bool
    _attr_alarm_state: Incomplete
    @callback
    def _refresh_alarm_state(self) -> None: ...
    @callback
    def _async_update_device_from_protect(self, device: ProtectDeviceType) -> None: ...
    @async_ufp_instance_command
    async def async_alarm_disarm(self, code: str | None = None) -> None: ...
    @async_ufp_instance_command
    async def async_alarm_arm_away(self, code: str | None = None) -> None: ...
