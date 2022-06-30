from . import RainMachineEntity as RainMachineEntity, async_update_programs_and_zones as async_update_programs_and_zones
from .const import CONF_ZONE_RUN_TIME as CONF_ZONE_RUN_TIME, DATA_CONTROLLER as DATA_CONTROLLER, DATA_COORDINATOR as DATA_COORDINATOR, DATA_PROGRAMS as DATA_PROGRAMS, DATA_ZONES as DATA_ZONES, DEFAULT_ZONE_RUN as DEFAULT_ZONE_RUN, DOMAIN as DOMAIN, RUN_STATE_MAP as RUN_STATE_MAP
from .model import RainMachineDescriptionMixinUid as RainMachineDescriptionMixinUid
from _typeshed import Incomplete
from collections.abc import Coroutine
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_ID as ATTR_ID
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import entity_platform as entity_platform
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from regenmaschine.controller import Controller as Controller
from typing import Any

ATTR_AREA: str
ATTR_CS_ON: str
ATTR_CURRENT_CYCLE: str
ATTR_CYCLES: str
ATTR_DELAY: str
ATTR_DELAY_ON: str
ATTR_FIELD_CAPACITY: str
ATTR_NEXT_RUN: str
ATTR_NO_CYCLES: str
ATTR_PRECIP_RATE: str
ATTR_RESTRICTIONS: str
ATTR_SLOPE: str
ATTR_SOAK: str
ATTR_SOIL_TYPE: str
ATTR_SPRINKLER_TYPE: str
ATTR_STATUS: str
ATTR_SUN_EXPOSURE: str
ATTR_VEGETATION_TYPE: str
ATTR_ZONES: str
DAYS: Incomplete
SOIL_TYPE_MAP: Incomplete
SLOPE_TYPE_MAP: Incomplete
SPRINKLER_TYPE_MAP: Incomplete
SUN_EXPOSURE_MAP: Incomplete
VEGETATION_MAP: Incomplete

class RainMachineSwitchDescription(SwitchEntityDescription, RainMachineDescriptionMixinUid):
    def __init__(self, uid, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, unit_of_measurement) -> None: ...

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RainMachineBaseSwitch(RainMachineEntity, SwitchEntity):
    entity_description: RainMachineSwitchDescription
    _attr_is_on: bool
    _entry: Incomplete
    def __init__(self, entry: ConfigEntry, coordinator: DataUpdateCoordinator, controller: Controller, description: RainMachineSwitchDescription) -> None: ...
    async def _async_run_api_coroutine(self, api_coro: Coroutine) -> None: ...
    async def async_start_program(self) -> None: ...
    async def async_start_zone(self, *, zone_run_time: int) -> None: ...
    async def async_stop_program(self) -> None: ...
    async def async_stop_zone(self) -> None: ...

class RainMachineActivitySwitch(RainMachineBaseSwitch):
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_turn_off_when_active(self, **kwargs: Any) -> None: ...
    _attr_is_on: bool
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_on_when_active(self, **kwargs: Any) -> None: ...

class RainMachineEnabledSwitch(RainMachineBaseSwitch):
    _attr_is_on: Incomplete
    def update_from_latest_data(self) -> None: ...

class RainMachineProgram(RainMachineActivitySwitch):
    async def async_start_program(self) -> None: ...
    async def async_stop_program(self) -> None: ...
    async def async_turn_off_when_active(self, **kwargs: Any) -> None: ...
    async def async_turn_on_when_active(self, **kwargs: Any) -> None: ...
    _attr_is_on: Incomplete
    def update_from_latest_data(self) -> None: ...

class RainMachineProgramEnabled(RainMachineEnabledSwitch):
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...

class RainMachineZone(RainMachineActivitySwitch):
    async def async_start_zone(self, *, zone_run_time: int) -> None: ...
    async def async_stop_zone(self) -> None: ...
    async def async_turn_off_when_active(self, **kwargs: Any) -> None: ...
    async def async_turn_on_when_active(self, **kwargs: Any) -> None: ...
    _attr_is_on: Incomplete
    def update_from_latest_data(self) -> None: ...

class RainMachineZoneEnabled(RainMachineEnabledSwitch):
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
