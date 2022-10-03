from .const import DOMAIN as DOMAIN
from .entity import LitterRobotEntity as LitterRobotEntity, async_update_unique_id as async_update_unique_id
from .hub import LitterRobotHub as LitterRobotHub
from _typeshed import Incomplete
from datetime import time
from homeassistant.components.vacuum import STATE_CLEANING as STATE_CLEANING, STATE_DOCKED as STATE_DOCKED, STATE_ERROR as STATE_ERROR, STATE_PAUSED as STATE_PAUSED, StateVacuumEntity as StateVacuumEntity, StateVacuumEntityDescription as StateVacuumEntityDescription, VacuumEntityFeature as VacuumEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import STATE_OFF as STATE_OFF
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import entity_platform as entity_platform
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pylitterbot import LitterRobot
from typing import Any

SERVICE_SET_SLEEP_MODE: str
LITTER_BOX_STATUS_STATE_MAP: Incomplete
LITTER_BOX_ENTITY: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class LitterRobotCleaner(LitterRobotEntity[LitterRobot], StateVacuumEntity):
    _attr_supported_features: Incomplete
    @property
    def state(self) -> str: ...
    @property
    def status(self) -> str: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_start(self) -> None: ...
    async def async_set_sleep_mode(self, enabled: bool, start_time: Union[str, None] = ...) -> None: ...
    @staticmethod
    def parse_time_at_default_timezone(time_str: Union[str, None]) -> Union[time, None]: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
