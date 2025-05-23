from . import IronOSConfigEntry as IronOSConfigEntry
from .coordinator import IronOSCoordinators as IronOSCoordinators
from .entity import IronOSBaseEntity as IronOSBaseEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from enum import Enum, StrEnum
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pynecil import CharSetting, SettingsDataResponse as SettingsDataResponse

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class IronOSSelectEntityDescription(SelectEntityDescription):
    value_fn: Callable[[SettingsDataResponse], str | None]
    characteristic: CharSetting
    raw_value_fn: Callable[[str], Enum]

class PinecilSelect(StrEnum):
    MIN_DC_VOLTAGE_CELLS = 'min_dc_voltage_cells'
    ORIENTATION_MODE = 'orientation_mode'
    ANIMATION_SPEED = 'animation_speed'
    AUTOSTART_MODE = 'autostart_mode'
    TEMP_UNIT = 'temp_unit'
    DESC_SCROLL_SPEED = 'desc_scroll_speed'
    LOCKING_MODE = 'locking_mode'
    LOGO_DURATION = 'logo_duration'
    USB_PD_MODE = 'usb_pd_mode'
    TIP_TYPE = 'tip_type'

def enum_to_str(enum: Enum | None) -> str | None: ...

PINECIL_SELECT_DESCRIPTIONS: tuple[IronOSSelectEntityDescription, ...]
PINECIL_SELECT_DESCRIPTIONS_V222: tuple[IronOSSelectEntityDescription, ...]
PINECIL_SELECT_DESCRIPTIONS_V223: tuple[IronOSSelectEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: IronOSConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class IronOSSelectEntity(IronOSBaseEntity, SelectEntity):
    entity_description: IronOSSelectEntityDescription
    settings: Incomplete
    def __init__(self, coordinators: IronOSCoordinators, entity_description: IronOSSelectEntityDescription) -> None: ...
    @property
    def current_option(self) -> str | None: ...
    async def async_select_option(self, option: str) -> None: ...
    async def async_added_to_hass(self) -> None: ...
