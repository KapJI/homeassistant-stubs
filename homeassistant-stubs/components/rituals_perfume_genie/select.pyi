from . import RitualsDataUpdateCoordinator as RitualsDataUpdateCoordinator
from .const import COORDINATORS as COORDINATORS, DEVICES as DEVICES, DOMAIN as DOMAIN
from .entity import DiffuserEntity as DiffuserEntity
from _typeshed import Incomplete
from homeassistant.components.select import SelectEntity as SelectEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import AREA_SQUARE_METERS as AREA_SQUARE_METERS
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pyrituals import Diffuser as Diffuser

ROOM_SIZE_SUFFIX: str

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DiffuserRoomSize(DiffuserEntity, SelectEntity):
    _attr_icon: str
    _attr_unit_of_measurement: Incomplete
    _attr_options: Incomplete
    _attr_entity_category: Incomplete
    _attr_entity_registry_enabled_default: Incomplete
    def __init__(self, diffuser: Diffuser, coordinator: RitualsDataUpdateCoordinator) -> None: ...
    @property
    def current_option(self) -> str: ...
    async def async_select_option(self, option: str) -> None: ...
