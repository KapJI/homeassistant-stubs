import aiounifi
from . import UnifiConfigEntry as UnifiConfigEntry
from .const import ATTR_MANUFACTURER as ATTR_MANUFACTURER
from .entity import HandlerT as HandlerT, SubscriptionT as SubscriptionT, UnifiEntity as UnifiEntity, UnifiEntityDescription as UnifiEntityDescription, async_client_device_info_fn as async_client_device_info_fn, async_device_available_fn as async_device_available_fn, async_device_device_info_fn as async_device_device_info_fn, async_wlan_device_info_fn as async_wlan_device_info_fn
from .hub import UnifiHub as UnifiHub
from _typeshed import Incomplete
from aiounifi.interfaces.api_handlers import ItemEvent
from aiounifi.models.api import ApiItemT
from aiounifi.models.dpi_restriction_group import DPIRestrictionGroup
from aiounifi.models.event import Event as Event
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.components.switch import SwitchDeviceClass as SwitchDeviceClass, SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

CLIENT_BLOCKED: Incomplete
CLIENT_UNBLOCKED: Incomplete

def async_block_client_allowed_fn(hub: UnifiHub, obj_id: str) -> bool: ...
def async_dpi_group_is_on_fn(hub: UnifiHub, dpi_group: DPIRestrictionGroup) -> bool: ...
def async_dpi_group_device_info_fn(hub: UnifiHub, obj_id: str) -> DeviceInfo: ...
def async_unifi_network_device_info_fn(hub: UnifiHub, obj_id: str) -> DeviceInfo: ...
async def async_block_client_control_fn(hub: UnifiHub, obj_id: str, target: bool) -> None: ...
async def async_dpi_group_control_fn(hub: UnifiHub, obj_id: str, target: bool) -> None: ...
def async_outlet_switching_supported_fn(hub: UnifiHub, obj_id: str) -> bool: ...
async def async_outlet_control_fn(hub: UnifiHub, obj_id: str, target: bool) -> None: ...
async def async_poe_port_control_fn(hub: UnifiHub, obj_id: str, target: bool) -> None: ...
async def async_port_forward_control_fn(hub: UnifiHub, obj_id: str, target: bool) -> None: ...
async def async_traffic_rule_control_fn(hub: UnifiHub, obj_id: str, target: bool) -> None: ...
async def async_wlan_control_fn(hub: UnifiHub, obj_id: str, target: bool) -> None: ...

@dataclass(frozen=True, kw_only=True)
class UnifiSwitchEntityDescription(SwitchEntityDescription, UnifiEntityDescription[HandlerT, ApiItemT]):
    control_fn: Callable[[UnifiHub, str, bool], Coroutine[Any, Any, None]]
    is_on_fn: Callable[[UnifiHub, ApiItemT], bool]
    custom_subscribe: Callable[[aiounifi.Controller], SubscriptionT] | None = ...
    only_event_for_state_change: bool = ...

ENTITY_DESCRIPTIONS: tuple[UnifiSwitchEntityDescription, ...]

def async_update_unique_id(hass: HomeAssistant, config_entry: UnifiConfigEntry) -> None: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: UnifiConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class UnifiSwitchEntity(UnifiEntity[HandlerT, ApiItemT], SwitchEntity):
    entity_description: UnifiSwitchEntityDescription[HandlerT, ApiItemT]
    def async_initiate_state(self) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    _attr_is_on: Incomplete
    def async_update_state(self, event: ItemEvent, obj_id: str, first_update: bool = False) -> None: ...
    _attr_available: Incomplete
    def async_event_callback(self, event: Event) -> None: ...
    async def async_added_to_hass(self) -> None: ...
