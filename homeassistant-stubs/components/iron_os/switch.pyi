from . import IronOSConfigEntry as IronOSConfigEntry
from .coordinator import IronOSCoordinators as IronOSCoordinators
from .entity import IronOSBaseEntity as IronOSBaseEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from enum import StrEnum
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pynecil import CharSetting, SettingsDataResponse as SettingsDataResponse
from typing import Any

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class IronOSSwitchEntityDescription(SwitchEntityDescription):
    is_on_fn: Callable[[SettingsDataResponse], bool | None]
    characteristic: CharSetting

class IronOSSwitch(StrEnum):
    ANIMATION_LOOP = 'animation_loop'
    COOLING_TEMP_BLINK = 'cooling_temp_blink'
    IDLE_SCREEN_DETAILS = 'idle_screen_details'
    SOLDER_SCREEN_DETAILS = 'solder_screen_details'
    INVERT_BUTTONS = 'invert_buttons'
    DISPLAY_INVERT = 'display_invert'
    CALIBRATE_CJC = 'calibrate_cjc'

SWITCH_DESCRIPTIONS: tuple[IronOSSwitchEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: IronOSConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class IronOSSwitchEntity(IronOSBaseEntity, SwitchEntity):
    entity_description: IronOSSwitchEntityDescription
    settings: Incomplete
    def __init__(self, coordinators: IronOSCoordinators, entity_description: IronOSSwitchEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool | None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_added_to_hass(self) -> None: ...
