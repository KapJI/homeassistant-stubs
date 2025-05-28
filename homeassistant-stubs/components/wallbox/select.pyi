from .const import CHARGER_DATA_KEY as CHARGER_DATA_KEY, CHARGER_ECO_SMART_KEY as CHARGER_ECO_SMART_KEY, CHARGER_FEATURES_KEY as CHARGER_FEATURES_KEY, CHARGER_PLAN_KEY as CHARGER_PLAN_KEY, CHARGER_POWER_BOOST_KEY as CHARGER_POWER_BOOST_KEY, CHARGER_SERIAL_NUMBER_KEY as CHARGER_SERIAL_NUMBER_KEY, DOMAIN as DOMAIN, EcoSmartMode as EcoSmartMode
from .coordinator import WallboxCoordinator as WallboxCoordinator
from .entity import WallboxEntity as WallboxEntity
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

@dataclass(frozen=True, kw_only=True)
class WallboxSelectEntityDescription(SelectEntityDescription):
    current_option_fn: Callable[[WallboxCoordinator], str | None]
    select_option_fn: Callable[[WallboxCoordinator, str], Awaitable[None]]
    supported_fn: Callable[[WallboxCoordinator], bool]

SELECT_TYPES: dict[str, WallboxSelectEntityDescription]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class WallboxSelect(WallboxEntity, SelectEntity):
    entity_description: WallboxSelectEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: WallboxCoordinator, description: WallboxSelectEntityDescription) -> None: ...
    @property
    def current_option(self) -> str | None: ...
    async def async_select_option(self, option: str) -> None: ...
