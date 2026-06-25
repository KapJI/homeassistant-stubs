import asyncio
from .const import ATTR_HOST_NAME as ATTR_HOST_NAME, ATTR_IN_ZONES as ATTR_IN_ZONES, ATTR_IP as ATTR_IP, ATTR_MAC as ATTR_MAC, ATTR_SOURCE_TYPE as ATTR_SOURCE_TYPE, ATTR_TRACKING_TYPE as ATTR_TRACKING_TYPE, CONF_ASSOCIATED_ZONE as CONF_ASSOCIATED_ZONE, CONNECTED_DEVICE_REGISTERED as CONNECTED_DEVICE_REGISTERED, DOMAIN as DOMAIN, DeviceTrackerEntityCapabilityAttribute as DeviceTrackerEntityCapabilityAttribute, DeviceTrackerEntityStateAttribute as DeviceTrackerEntityStateAttribute, LOGGER as LOGGER, ScannerEntityStateAttribute as ScannerEntityStateAttribute, SourceType as SourceType, TrackerEntityStateAttribute as TrackerEntityStateAttribute, TrackingType as TrackingType
from _typeshed import Incomplete
from homeassistant.components import zone as zone
from homeassistant.components.zone import ATTR_PASSIVE as ATTR_PASSIVE, ATTR_RADIUS as ATTR_RADIUS
from homeassistant.const import ATTR_BATTERY_LEVEL as ATTR_BATTERY_LEVEL, ATTR_GPS_ACCURACY as ATTR_GPS_ACCURACY, ATTR_LATITUDE as ATTR_LATITUDE, ATTR_LONGITUDE as ATTR_LONGITUDE, EntityCategory as EntityCategory, STATE_HOME as STATE_HOME, STATE_NOT_HOME as STATE_NOT_HOME
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, Event as Event, EventStateChangedData as EventStateChangedData, HomeAssistant as HomeAssistant, State as State, async_get_hass_or_none as async_get_hass_or_none, callback as callback
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo, EventDeviceRegistryUpdatedData as EventDeviceRegistryUpdatedData
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.entity import Entity as Entity, EntityDescription as EntityDescription
from homeassistant.helpers.entity_platform import EntityPlatform as EntityPlatform
from homeassistant.helpers.event import async_track_state_change_event as async_track_state_change_event
from homeassistant.loader import async_suggest_report_issue as async_suggest_report_issue
from homeassistant.util.hass_dict import HassKey as HassKey
from propcache.api import cached_property
from typing import Any, final, override

_LOGGER: Incomplete
DATA_KEY: HassKey[dict[str, tuple[str, str]]]

@callback
def _async_connected_device_registered(hass: HomeAssistant, mac: str, ip_address: str | None, hostname: str | None) -> None: ...
@callback
def _async_register_mac(hass: HomeAssistant, domain: str, mac: str, unique_id: str) -> None: ...

class BaseTrackerEntity(Entity):
    _attr_device_info: None
    _attr_entity_category: Incomplete
    _attr_source_type: SourceType
    @override
    def __init_subclass__(cls, **kwargs: Any) -> None: ...
    @cached_property
    def battery_level(self) -> int | None: ...
    @property
    def source_type(self) -> SourceType: ...
    @property
    @override
    def state_attributes(self) -> dict[str, Any]: ...

class TrackerEntityDescription(EntityDescription, frozen_or_thawed=True): ...

CACHED_TRACKER_PROPERTIES_WITH_ATTR_: Incomplete

class TrackerEntity(BaseTrackerEntity, cached_properties=CACHED_TRACKER_PROPERTIES_WITH_ATTR_):
    entity_description: TrackerEntityDescription
    _attr_capability_attributes: dict[str, Any]
    _attr_in_zones: list[str] | None
    _attr_latitude: float | None
    _attr_location_accuracy: float
    _attr_location_name: str | None
    _attr_longitude: float | None
    _attr_source_type: SourceType
    __active_zone: State | None
    __deprecated_attr_location_name_reported: bool
    __in_zones: list[str] | None
    @override
    def __init_subclass__(cls, **kwargs: Any) -> None: ...
    @cached_property
    @override
    def should_poll(self) -> bool: ...
    @property
    @override
    def force_update(self) -> bool: ...
    @cached_property
    def in_zones(self) -> list[str] | None: ...
    @cached_property
    def location_accuracy(self) -> float: ...
    @cached_property
    def location_name(self) -> str | None: ...
    @cached_property
    def latitude(self) -> float | None: ...
    @cached_property
    def longitude(self) -> float | None: ...
    @callback
    @override
    def _async_write_ha_state(self) -> None: ...
    @property
    @override
    def state(self) -> str | None: ...
    @final
    @property
    @override
    def state_attributes(self) -> dict[str, Any]: ...

class BaseScannerEntity(BaseTrackerEntity):
    _attr_capability_attributes: dict[str, Any]
    _scanner_option_associated_zone: str
    _scanner_option_associated_zone_unsub: CALLBACK_TYPE | None
    @override
    async def async_internal_added_to_hass(self) -> None: ...
    @override
    async def async_internal_will_remove_from_hass(self) -> None: ...
    @callback
    @override
    def async_registry_entry_updated(self) -> None: ...
    @callback
    def _async_read_entity_options(self) -> None: ...
    @callback
    def _async_associated_zone_state_changed(self, event: Event[EventStateChangedData]) -> None: ...
    @callback
    def _async_create_associated_zone_issue(self) -> None: ...
    @callback
    def _async_clear_associated_zone_issue(self) -> None: ...
    @property
    def _associated_zone_issue_id(self) -> str: ...
    @property
    @override
    def state(self) -> str | None: ...
    @property
    def is_connected(self) -> bool | None: ...
    @final
    @property
    @override
    def state_attributes(self) -> dict[str, Any]: ...

class ScannerEntityDescription(EntityDescription, frozen_or_thawed=True): ...

CACHED_SCANNER_PROPERTIES_WITH_ATTR_: Incomplete

class ScannerEntity(BaseScannerEntity, cached_properties=CACHED_SCANNER_PROPERTIES_WITH_ATTR_):
    entity_description: ScannerEntityDescription
    _attr_hostname: str | None
    _attr_ip_address: str | None
    _attr_mac_address: str | None
    _attr_source_type: SourceType
    @cached_property
    def ip_address(self) -> str | None: ...
    @cached_property
    def mac_address(self) -> str | None: ...
    @cached_property
    def hostname(self) -> str | None: ...
    @property
    @override
    def unique_id(self) -> str | None: ...
    @final
    @property
    @override
    def device_info(self) -> DeviceInfo | None: ...
    @property
    @override
    def entity_registry_enabled_default(self) -> bool: ...
    @callback
    @override
    def add_to_platform_start(self, hass: HomeAssistant, platform: EntityPlatform, parallel_updates: asyncio.Semaphore | None) -> None: ...
    @callback
    def find_device_entry(self) -> dr.DeviceEntry | None: ...
    registry_entry: Incomplete
    @override
    async def async_internal_added_to_hass(self) -> None: ...
    @final
    @property
    @override
    def state_attributes(self) -> dict[str, Any]: ...
