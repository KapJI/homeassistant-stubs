from . import NASwebConfigEntry as NASwebConfigEntry
from .const import DOMAIN as DOMAIN, STATUS_UPDATE_MAX_TIME_INTERVAL as STATUS_UPDATE_MAX_TIME_INTERVAL
from _typeshed import Incomplete
from homeassistant.components.alarm_control_panel import AlarmControlPanelEntity as AlarmControlPanelEntity, AlarmControlPanelEntityFeature as AlarmControlPanelEntityFeature, AlarmControlPanelState as AlarmControlPanelState, CodeFormat as CodeFormat
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import DiscoveryInfoType as DiscoveryInfoType
from homeassistant.helpers.update_coordinator import BaseCoordinatorEntity as BaseCoordinatorEntity, BaseDataUpdateCoordinatorProtocol as BaseDataUpdateCoordinatorProtocol
from webio_api import Zone as NASwebZone

_LOGGER: Incomplete
ALARM_CONTROL_PANEL_TRANSLATION_KEY: str
NASWEB_STATE_TO_HA_STATE: Incomplete

async def async_setup_entry(hass: HomeAssistant, config: NASwebConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...

class ZoneEntity(AlarmControlPanelEntity, BaseCoordinatorEntity):
    _attr_has_entity_name: bool
    _attr_should_poll: bool
    _attr_translation_key = ALARM_CONTROL_PANEL_TRANSLATION_KEY
    _zone: Incomplete
    _attr_name: Incomplete
    _attr_translation_placeholders: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: BaseDataUpdateCoordinatorProtocol, nasweb_zone: NASwebZone) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    _attr_available: bool
    def _set_attr_available(self, entity_last_update: float, available: bool | None) -> None: ...
    _attr_alarm_state: Incomplete
    _attr_code_format: Incomplete
    _attr_code_arm_required: Incomplete
    @callback
    def _handle_coordinator_update(self) -> None: ...
    async def async_update(self) -> None: ...
    @property
    def supported_features(self) -> AlarmControlPanelEntityFeature: ...
    async def async_alarm_arm_away(self, code: str | None = None) -> None: ...
    async def async_alarm_disarm(self, code: str | None = None) -> None: ...
