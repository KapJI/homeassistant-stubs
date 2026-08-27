from .const import DOMAIN as DOMAIN
from .coordinator import FlowItConfigEntry as FlowItConfigEntry, FlowItCoordinator as FlowItCoordinator
from .entity import FlowItVmcEntity as FlowItVmcEntity
from _typeshed import Incomplete
from flow_it_api.client import FlowItVMCMachine as FlowItVMCMachine
from flow_it_api.const import Speed
from homeassistant.components.fan import FanEntity as FanEntity, FanEntityDescription as FanEntityDescription, FanEntityFeature as FanEntityFeature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.util.percentage import ordered_list_item_to_percentage as ordered_list_item_to_percentage, percentage_to_ordered_list_item as percentage_to_ordered_list_item
from typing import Any, override

ORDERED_NAMED_FAN_SPEEDS: Incomplete
PRESET_MODES: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: FlowItConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class FlowItVmcFan(FlowItVmcEntity, FanEntity):
    _attr_supported_features: Incomplete
    _attr_preset_modes: Incomplete
    _attr_speed_count: Incomplete
    def __init__(self, coordinator: FlowItCoordinator, vmc: FlowItVMCMachine) -> None: ...
    @override
    @property
    def is_on(self) -> bool | None: ...
    @override
    @property
    def percentage(self) -> int | None: ...
    @override
    @property
    def preset_mode(self) -> str | None: ...
    async def _async_send_command(self, speed: Speed, flow_in: bool, flow_out: bool) -> None: ...
    @override
    async def async_set_percentage(self, percentage: int) -> None: ...
    @override
    async def async_set_preset_mode(self, preset_mode: str) -> None: ...
    @override
    async def async_turn_on(self, percentage: int | None = None, preset_mode: str | None = None, **kwargs: Any) -> None: ...
    @override
    async def async_turn_off(self, **kwargs: Any) -> None: ...
