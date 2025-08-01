from .const import CORE_CLIMATE as CORE_CLIMATE, DOMAIN as DOMAIN, FOOT_WARMER as FOOT_WARMER
from .coordinator import SleepIQData as SleepIQData, SleepIQDataUpdateCoordinator as SleepIQDataUpdateCoordinator
from .entity import SleepIQBedEntity as SleepIQBedEntity, SleepIQSleeperEntity as SleepIQSleeperEntity, sleeper_for_side as sleeper_for_side
from _typeshed import Incomplete
from asyncsleepiq import SleepIQBed as SleepIQBed, SleepIQCoreClimate as SleepIQCoreClimate, SleepIQFootWarmer as SleepIQFootWarmer, SleepIQPreset as SleepIQPreset
from homeassistant.components.select import SelectEntity as SelectEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class SleepIQSelectEntity(SleepIQBedEntity[SleepIQDataUpdateCoordinator], SelectEntity):
    preset: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    _attr_options: Incomplete
    def __init__(self, coordinator: SleepIQDataUpdateCoordinator, bed: SleepIQBed, preset: SleepIQPreset) -> None: ...
    _attr_current_option: Incomplete
    @callback
    def _async_update_attrs(self) -> None: ...
    async def async_select_option(self, option: str) -> None: ...

class SleepIQFootWarmingTempSelectEntity(SleepIQSleeperEntity[SleepIQDataUpdateCoordinator], SelectEntity):
    _attr_icon: str
    _attr_options: Incomplete
    _attr_translation_key: str
    foot_warmer: Incomplete
    def __init__(self, coordinator: SleepIQDataUpdateCoordinator, bed: SleepIQBed, foot_warmer: SleepIQFootWarmer) -> None: ...
    _attr_current_option: Incomplete
    @callback
    def _async_update_attrs(self) -> None: ...
    async def async_select_option(self, option: str) -> None: ...

class SleepIQCoreTempSelectEntity(SleepIQSleeperEntity[SleepIQDataUpdateCoordinator], SelectEntity):
    SLEEPIQ_TO_HA_CORE_TEMP_MAP: Incomplete
    HA_TO_SLEEPIQ_CORE_TEMP_MAP: Incomplete
    _attr_icon: str
    _attr_options: Incomplete
    _attr_translation_key: str
    core_climate: Incomplete
    def __init__(self, coordinator: SleepIQDataUpdateCoordinator, bed: SleepIQBed, core_climate: SleepIQCoreClimate) -> None: ...
    _attr_current_option: Incomplete
    @callback
    def _async_update_attrs(self) -> None: ...
    async def async_select_option(self, option: str) -> None: ...
