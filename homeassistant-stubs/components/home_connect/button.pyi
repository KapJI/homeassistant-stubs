from .common import setup_home_connect_entry as setup_home_connect_entry
from .const import APPLIANCES_WITH_PROGRAMS as APPLIANCES_WITH_PROGRAMS, DOMAIN as DOMAIN
from .coordinator import HomeConnectApplianceData as HomeConnectApplianceData, HomeConnectConfigEntry as HomeConnectConfigEntry, HomeConnectCoordinator as HomeConnectCoordinator
from .entity import HomeConnectEntity as HomeConnectEntity
from .utils import get_dict_from_home_connect_error as get_dict_from_home_connect_error
from _typeshed import Incomplete
from aiohomeconnect.model import CommandKey
from homeassistant.components.button import ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

PARALLEL_UPDATES: int

class HomeConnectCommandButtonEntityDescription(ButtonEntityDescription):
    key: CommandKey

COMMAND_BUTTONS: Incomplete

def _get_entities_for_appliance(entry: HomeConnectConfigEntry, appliance: HomeConnectApplianceData) -> list[HomeConnectEntity]: ...
async def async_setup_entry(hass: HomeAssistant, entry: HomeConnectConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class HomeConnectButtonEntity(HomeConnectEntity, ButtonEntity):
    entity_description: ButtonEntityDescription
    def __init__(self, coordinator: HomeConnectCoordinator, appliance: HomeConnectApplianceData, desc: ButtonEntityDescription) -> None: ...
    def update_native_value(self) -> None: ...

class HomeConnectCommandButtonEntity(HomeConnectButtonEntity):
    entity_description: HomeConnectCommandButtonEntityDescription
    async def async_press(self) -> None: ...

class HomeConnectStopProgramButtonEntity(HomeConnectButtonEntity):
    def __init__(self, coordinator: HomeConnectCoordinator, appliance: HomeConnectApplianceData) -> None: ...
    async def async_press(self) -> None: ...
