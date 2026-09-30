from .const import DOMAIN as DOMAIN
from .coordinator import FlowItConfigEntry as FlowItConfigEntry, FlowItCoordinator as FlowItCoordinator
from .entity import FlowItVmcEntity as FlowItVmcEntity
from flow_it_api.client import FlowItVMCMachine as FlowItVMCMachine
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any, override

SWITCHES: tuple[SwitchEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: FlowItConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class FlowItVmcFlowSwitch(FlowItVmcEntity, SwitchEntity):
    entity_description: SwitchEntityDescription
    def __init__(self, coordinator: FlowItCoordinator, vmc: FlowItVMCMachine, description: SwitchEntityDescription) -> None: ...
    @override
    @property
    def is_on(self) -> bool | None: ...
    @override
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @override
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def _async_set_flow(self, state: bool) -> None: ...
