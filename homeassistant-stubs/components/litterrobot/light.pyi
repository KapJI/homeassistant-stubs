from .coordinator import LitterRobotConfigEntry as LitterRobotConfigEntry
from .entity import LitterRobotEntity as LitterRobotEntity, whisker_command as whisker_command
from _typeshed import Incomplete
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ATTR_RGB_COLOR as ATTR_RGB_COLOR, ColorMode as ColorMode, LightEntity as LightEntity, LightEntityDescription as LightEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pylitterbot import LitterRobot5
from typing import Any, override

PARALLEL_UPDATES: int
NIGHT_LIGHT_DESCRIPTION: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: LitterRobotConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LitterRobotNightLight(LitterRobotEntity[LitterRobot5], LightEntity):
    _attr_color_mode: Incomplete
    _attr_supported_color_modes: Incomplete
    @property
    @override
    def is_on(self) -> bool: ...
    @property
    @override
    def brightness(self) -> int: ...
    @property
    @override
    def rgb_color(self) -> tuple[int, int, int] | None: ...
    @whisker_command
    @override
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @whisker_command
    @override
    async def async_turn_off(self, **kwargs: Any) -> None: ...
