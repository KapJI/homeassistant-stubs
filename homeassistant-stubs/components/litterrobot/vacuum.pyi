from .const import DOMAIN as DOMAIN
from .entity import LitterRobotControlEntity as LitterRobotControlEntity
from .hub import LitterRobotHub as LitterRobotHub
from _typeshed import Incomplete
from homeassistant.components.vacuum import STATE_CLEANING as STATE_CLEANING, STATE_DOCKED as STATE_DOCKED, STATE_ERROR as STATE_ERROR, STATE_PAUSED as STATE_PAUSED, StateVacuumEntity as StateVacuumEntity, VacuumEntityFeature as VacuumEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import STATE_OFF as STATE_OFF
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import entity_platform as entity_platform
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

_LOGGER: Incomplete
TYPE_LITTER_BOX: str
SERVICE_RESET_WASTE_DRAWER: str
SERVICE_SET_SLEEP_MODE: str
SERVICE_SET_WAIT_TIME: str
LITTER_BOX_STATUS_STATE_MAP: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class LitterRobotCleaner(LitterRobotControlEntity, StateVacuumEntity):
    _attr_supported_features: Incomplete
    @property
    def state(self) -> str: ...
    @property
    def status(self) -> str: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_start(self) -> None: ...
    async def async_reset_waste_drawer(self) -> None: ...
    async def async_set_sleep_mode(self, enabled: bool, start_time: Union[str, None] = ...) -> None: ...
    async def async_set_wait_time(self, minutes: int) -> None: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
