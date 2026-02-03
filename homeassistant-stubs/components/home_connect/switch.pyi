from .common import setup_home_connect_entry as setup_home_connect_entry, should_add_option_entity as should_add_option_entity
from .const import BSH_POWER_OFF as BSH_POWER_OFF, BSH_POWER_ON as BSH_POWER_ON, BSH_POWER_STANDBY as BSH_POWER_STANDBY, DOMAIN as DOMAIN
from .coordinator import HomeConnectApplianceData as HomeConnectApplianceData, HomeConnectConfigEntry as HomeConnectConfigEntry
from .entity import HomeConnectEntity as HomeConnectEntity, HomeConnectOptionEntity as HomeConnectOptionEntity
from .utils import get_dict_from_home_connect_error as get_dict_from_home_connect_error
from _typeshed import Incomplete
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import entity_registry as er
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import UNDEFINED as UNDEFINED, UndefinedType as UndefinedType
from typing import Any

_LOGGER: Incomplete
PARALLEL_UPDATES: int
SWITCHES: Incomplete
POWER_SWITCH_DESCRIPTION: Incomplete
SWITCH_OPTIONS: Incomplete

def _get_entities_for_appliance(entry: HomeConnectConfigEntry, appliance: HomeConnectApplianceData) -> list[HomeConnectEntity]: ...
def _get_option_entities_for_appliance(entry: HomeConnectConfigEntry, appliance: HomeConnectApplianceData, entity_registry: er.EntityRegistry) -> list[HomeConnectOptionEntity]: ...
async def async_setup_entry(hass: HomeAssistant, entry: HomeConnectConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class HomeConnectSwitch(HomeConnectEntity, SwitchEntity):
    _attr_available: bool
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    _attr_is_on: Incomplete
    def update_native_value(self) -> None: ...

class HomeConnectPowerSwitch(HomeConnectEntity, SwitchEntity):
    power_off_state: str | None | UndefinedType
    _attr_is_on: bool
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    def update_native_value(self) -> None: ...
    async def async_fetch_power_off_state(self) -> None: ...

class HomeConnectSwitchOptionEntity(HomeConnectOptionEntity, SwitchEntity):
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    _attr_is_on: Incomplete
    def update_native_value(self) -> None: ...
