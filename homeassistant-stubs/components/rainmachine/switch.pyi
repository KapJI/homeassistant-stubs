from . import RainMachineData as RainMachineData, RainMachineEntity as RainMachineEntity, async_update_programs_and_zones as async_update_programs_and_zones
from .const import CONF_DEFAULT_ZONE_RUN_TIME as CONF_DEFAULT_ZONE_RUN_TIME, CONF_DURATION as CONF_DURATION, CONF_USE_APP_RUN_TIMES as CONF_USE_APP_RUN_TIMES, DATA_PROGRAMS as DATA_PROGRAMS, DATA_PROVISION_SETTINGS as DATA_PROVISION_SETTINGS, DATA_RESTRICTIONS_UNIVERSAL as DATA_RESTRICTIONS_UNIVERSAL, DATA_ZONES as DATA_ZONES, DEFAULT_ZONE_RUN as DEFAULT_ZONE_RUN, DOMAIN as DOMAIN
from .model import RainMachineEntityDescription as RainMachineEntityDescription, RainMachineEntityDescriptionMixinDataKey as RainMachineEntityDescriptionMixinDataKey, RainMachineEntityDescriptionMixinUid as RainMachineEntityDescriptionMixinUid
from .util import RUN_STATE_MAP as RUN_STATE_MAP, key_exists as key_exists
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable, Coroutine
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_ID as ATTR_ID, EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import entity_platform as entity_platform
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any, Concatenate, TypeVar

ATTR_AREA: str
ATTR_CS_ON: str
ATTR_CURRENT_CYCLE: str
ATTR_CYCLES: str
ATTR_ZONE_RUN_TIME: str
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
_T = TypeVar('_T', bound='RainMachineBaseSwitch')
_P: Incomplete

def raise_on_request_error(func: Callable[Concatenate[_T, _P], Awaitable[None]]) -> Callable[Concatenate[_T, _P], Coroutine[Any, Any, None]]: ...

class RainMachineSwitchDescription(SwitchEntityDescription, RainMachineEntityDescription):
    def __init__(self, api_category, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement) -> None: ...

class RainMachineActivitySwitchDescription(RainMachineSwitchDescription, RainMachineEntityDescriptionMixinUid):
    def __init__(self, uid, api_category, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement) -> None: ...

class RainMachineRestrictionSwitchDescription(RainMachineSwitchDescription, RainMachineEntityDescriptionMixinDataKey):
    def __init__(self, data_key, api_category, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement) -> None: ...

TYPE_RESTRICTIONS_FREEZE_PROTECT_ENABLED: str
TYPE_RESTRICTIONS_HOT_DAYS_EXTRA_WATERING: str
RESTRICTIONS_SWITCH_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RainMachineBaseSwitch(RainMachineEntity, SwitchEntity):
    entity_description: RainMachineSwitchDescription
    _attr_is_on: bool
    _entry: Incomplete
    def __init__(self, entry: ConfigEntry, data: RainMachineData, description: RainMachineSwitchDescription) -> None: ...
    def _update_activities(self) -> None: ...
    async def async_start_program(self) -> None: ...
    async def async_start_zone(self, *, zone_run_time: int) -> None: ...
    async def async_stop_program(self) -> None: ...
    async def async_stop_zone(self) -> None: ...

class RainMachineActivitySwitch(RainMachineBaseSwitch):
    _attr_icon: str
    entity_description: RainMachineActivitySwitchDescription
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_turn_off_when_active(self, **kwargs: Any) -> None: ...
    _attr_is_on: bool
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_on_when_active(self, **kwargs: Any) -> None: ...

class RainMachineEnabledSwitch(RainMachineBaseSwitch):
    _attr_entity_category: Incomplete
    _attr_icon: str
    entity_description: RainMachineActivitySwitchDescription
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

class RainMachineRestrictionSwitch(RainMachineBaseSwitch):
    _attr_entity_category: Incomplete
    entity_description: RainMachineRestrictionSwitchDescription
    _attr_is_on: bool
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    def update_from_latest_data(self) -> None: ...

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
