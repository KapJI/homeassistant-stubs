from .common import setup_home_connect_entry as setup_home_connect_entry
from .const import APPLIANCES_WITH_PROGRAMS as APPLIANCES_WITH_PROGRAMS, AVAILABLE_MAPS_ENUM as AVAILABLE_MAPS_ENUM, BEAN_AMOUNT_OPTIONS as BEAN_AMOUNT_OPTIONS, BEAN_CONTAINER_OPTIONS as BEAN_CONTAINER_OPTIONS, CLEANING_MODE_OPTIONS as CLEANING_MODE_OPTIONS, COFFEE_MILK_RATIO_OPTIONS as COFFEE_MILK_RATIO_OPTIONS, COFFEE_TEMPERATURE_OPTIONS as COFFEE_TEMPERATURE_OPTIONS, DOMAIN as DOMAIN, DRYING_TARGET_OPTIONS as DRYING_TARGET_OPTIONS, FLOW_RATE_OPTIONS as FLOW_RATE_OPTIONS, HOT_WATER_TEMPERATURE_OPTIONS as HOT_WATER_TEMPERATURE_OPTIONS, INTENSIVE_LEVEL_OPTIONS as INTENSIVE_LEVEL_OPTIONS, PROGRAMS_TRANSLATION_KEYS_MAP as PROGRAMS_TRANSLATION_KEYS_MAP, SPIN_SPEED_OPTIONS as SPIN_SPEED_OPTIONS, SVE_TRANSLATION_KEY_SET_SETTING as SVE_TRANSLATION_KEY_SET_SETTING, SVE_TRANSLATION_PLACEHOLDER_ENTITY_ID as SVE_TRANSLATION_PLACEHOLDER_ENTITY_ID, SVE_TRANSLATION_PLACEHOLDER_KEY as SVE_TRANSLATION_PLACEHOLDER_KEY, SVE_TRANSLATION_PLACEHOLDER_PROGRAM as SVE_TRANSLATION_PLACEHOLDER_PROGRAM, SVE_TRANSLATION_PLACEHOLDER_VALUE as SVE_TRANSLATION_PLACEHOLDER_VALUE, TEMPERATURE_OPTIONS as TEMPERATURE_OPTIONS, TRANSLATION_KEYS_PROGRAMS_MAP as TRANSLATION_KEYS_PROGRAMS_MAP, VARIO_PERFECT_OPTIONS as VARIO_PERFECT_OPTIONS, VENTING_LEVEL_OPTIONS as VENTING_LEVEL_OPTIONS, WARMING_LEVEL_OPTIONS as WARMING_LEVEL_OPTIONS
from .coordinator import HomeConnectApplianceData as HomeConnectApplianceData, HomeConnectConfigEntry as HomeConnectConfigEntry, HomeConnectCoordinator as HomeConnectCoordinator
from .entity import HomeConnectEntity as HomeConnectEntity, HomeConnectOptionEntity as HomeConnectOptionEntity
from .utils import bsh_key_to_translation_key as bsh_key_to_translation_key, get_dict_from_home_connect_error as get_dict_from_home_connect_error
from _typeshed import Incomplete
from aiohomeconnect.client import Client as HomeConnectClient
from aiohomeconnect.model import ProgramKey
from aiohomeconnect.model.program import Execution
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any

PARALLEL_UPDATES: int
FUNCTIONAL_LIGHT_COLOR_TEMPERATURE_ENUM: Incomplete
AMBIENT_LIGHT_COLOR_TEMPERATURE_ENUM: Incomplete

@dataclass(frozen=True, kw_only=True)
class HomeConnectProgramSelectEntityDescription(SelectEntityDescription):
    allowed_executions: tuple[Execution, ...]
    set_program_fn: Callable[[HomeConnectClient, str, ProgramKey], Coroutine[Any, Any, None]]
    error_translation_key: str

@dataclass(frozen=True, kw_only=True)
class HomeConnectSelectEntityDescription(SelectEntityDescription):
    translation_key_values: dict[str, str]
    values_translation_key: dict[str, str]

PROGRAM_SELECT_ENTITY_DESCRIPTIONS: Incomplete
SELECT_ENTITY_DESCRIPTIONS: Incomplete
PROGRAM_SELECT_OPTION_ENTITY_DESCRIPTIONS: Incomplete

def _get_entities_for_appliance(entry: HomeConnectConfigEntry, appliance: HomeConnectApplianceData) -> list[HomeConnectEntity]: ...
def _get_option_entities_for_appliance(entry: HomeConnectConfigEntry, appliance: HomeConnectApplianceData) -> list[HomeConnectOptionEntity]: ...
async def async_setup_entry(hass: HomeAssistant, entry: HomeConnectConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class HomeConnectProgramSelectEntity(HomeConnectEntity, SelectEntity):
    entity_description: HomeConnectProgramSelectEntityDescription
    _attr_options: Incomplete
    def __init__(self, coordinator: HomeConnectCoordinator, appliance: HomeConnectApplianceData, desc: HomeConnectProgramSelectEntityDescription) -> None: ...
    _attr_current_option: Incomplete
    def update_native_value(self) -> None: ...
    async def async_select_option(self, option: str) -> None: ...

class HomeConnectSelectEntity(HomeConnectEntity, SelectEntity):
    entity_description: HomeConnectSelectEntityDescription
    def __init__(self, coordinator: HomeConnectCoordinator, appliance: HomeConnectApplianceData, desc: HomeConnectSelectEntityDescription) -> None: ...
    async def async_select_option(self, option: str) -> None: ...
    _attr_current_option: Incomplete
    def update_native_value(self) -> None: ...
    _attr_options: Incomplete
    async def async_added_to_hass(self) -> None: ...

class HomeConnectSelectOptionEntity(HomeConnectOptionEntity, SelectEntity):
    entity_description: HomeConnectSelectEntityDescription
    _original_option_keys: set[str | None]
    def __init__(self, coordinator: HomeConnectCoordinator, appliance: HomeConnectApplianceData, desc: HomeConnectSelectEntityDescription) -> None: ...
    async def async_select_option(self, option: str) -> None: ...
    _attr_current_option: Incomplete
    _attr_options: Incomplete
    def update_native_value(self) -> None: ...
