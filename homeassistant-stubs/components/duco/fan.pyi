from .const import DOMAIN as DOMAIN
from .coordinator import DucoConfigEntry as DucoConfigEntry, DucoCoordinator as DucoCoordinator
from .entity import DucoEntity as DucoEntity
from _typeshed import Incomplete
from duco.models import Node as Node, VentilationState
from homeassistant.components.fan import FanEntity as FanEntity, FanEntityFeature as FanEntityFeature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.util.percentage import percentage_to_ordered_list_item as percentage_to_ordered_list_item

_LOGGER: Incomplete
PARALLEL_UPDATES: int
ORDERED_NAMED_FAN_SPEEDS: list[VentilationState]
PRESET_AUTO: str
_SPEED_LEVEL_PERCENTAGES: list[int]
_STATE_TO_PERCENTAGE: dict[VentilationState, int]

async def async_setup_entry(hass: HomeAssistant, entry: DucoConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class DucoVentilationFanEntity(DucoEntity, FanEntity):
    _attr_translation_key: str
    _attr_name: Incomplete
    _attr_supported_features: Incomplete
    _attr_preset_modes: Incomplete
    _attr_speed_count: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: DucoCoordinator, node: Node) -> None: ...
    @property
    def percentage(self) -> int | None: ...
    @property
    def preset_mode(self) -> str | None: ...
    async def async_set_preset_mode(self, preset_mode: str) -> None: ...
    async def async_set_percentage(self, percentage: int) -> None: ...
    async def _async_set_state(self, state: VentilationState) -> None: ...
