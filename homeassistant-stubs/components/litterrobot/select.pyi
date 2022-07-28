from .const import DOMAIN as DOMAIN
from .entity import LitterRobotConfigEntity as LitterRobotConfigEntity
from .hub import LitterRobotHub as LitterRobotHub
from homeassistant.components.select import SelectEntity as SelectEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

TYPE_CLEAN_CYCLE_WAIT_TIME_MINUTES: str

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class LitterRobotSelect(LitterRobotConfigEntity, SelectEntity):
    _attr_icon: str
    @property
    def current_option(self) -> Union[str, None]: ...
    @property
    def options(self) -> list[str]: ...
    async def async_select_option(self, option: str) -> None: ...
