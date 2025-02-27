from .const import ASSETS_URL as ASSETS_URL, DOMAIN as DOMAIN
from .coordinator import HabiticaConfigEntry as HabiticaConfigEntry, HabiticaData as HabiticaData, HabiticaDataUpdateCoordinator as HabiticaDataUpdateCoordinator
from .entity import HabiticaBase as HabiticaBase
from collections.abc import Callable as Callable
from dataclasses import dataclass
from enum import StrEnum
from habiticalib import HabiticaClass
from homeassistant.components.button import ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, ServiceValidationError as ServiceValidationError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any

PARALLEL_UPDATES: int

@dataclass(kw_only=True, frozen=True)
class HabiticaButtonEntityDescription(ButtonEntityDescription):
    press_fn: Callable[[HabiticaDataUpdateCoordinator], Any]
    available_fn: Callable[[HabiticaData], bool]
    class_needed: HabiticaClass | None = ...
    entity_picture: str | None = ...

class HabiticaButtonEntity(StrEnum):
    RUN_CRON = 'run_cron'
    BUY_HEALTH_POTION = 'buy_health_potion'
    ALLOCATE_ALL_STAT_POINTS = 'allocate_all_stat_points'
    REVIVE = 'revive'
    MPHEAL = 'mpheal'
    EARTH = 'earth'
    FROST = 'frost'
    DEFENSIVE_STANCE = 'defensive_stance'
    VALOROUS_PRESENCE = 'valorous_presence'
    INTIMIDATE = 'intimidate'
    TOOLS_OF_TRADE = 'tools_of_trade'
    STEALTH = 'stealth'
    HEAL = 'heal'
    PROTECT_AURA = 'protect_aura'
    BRIGHTNESS = 'brightness'
    HEAL_ALL = 'heal_all'

BUTTON_DESCRIPTIONS: tuple[HabiticaButtonEntityDescription, ...]
CLASS_SKILLS: tuple[HabiticaButtonEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: HabiticaConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class HabiticaButton(HabiticaBase, ButtonEntity):
    entity_description: HabiticaButtonEntityDescription
    async def async_press(self) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def entity_picture(self) -> str | None: ...
