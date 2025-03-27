from .common import setup_home_connect_entry as setup_home_connect_entry
from .const import DOMAIN as DOMAIN, UNIT_MAP as UNIT_MAP
from .coordinator import HomeConnectApplianceData as HomeConnectApplianceData, HomeConnectConfigEntry as HomeConnectConfigEntry
from .entity import HomeConnectEntity as HomeConnectEntity, HomeConnectOptionEntity as HomeConnectOptionEntity, constraint_fetcher as constraint_fetcher
from .utils import get_dict_from_home_connect_error as get_dict_from_home_connect_error
from _typeshed import Incomplete
from aiohomeconnect.model import GetSetting as GetSetting
from homeassistant.components.number import NumberDeviceClass as NumberDeviceClass, NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

_LOGGER: Incomplete
PARALLEL_UPDATES: int
NUMBERS: Incomplete
NUMBER_OPTIONS: Incomplete

def _get_entities_for_appliance(entry: HomeConnectConfigEntry, appliance: HomeConnectApplianceData) -> list[HomeConnectEntity]: ...
def _get_option_entities_for_appliance(entry: HomeConnectConfigEntry, appliance: HomeConnectApplianceData) -> list[HomeConnectOptionEntity]: ...
async def async_setup_entry(hass: HomeAssistant, entry: HomeConnectConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class HomeConnectNumberEntity(HomeConnectEntity, NumberEntity):
    async def async_set_native_value(self, value: float) -> None: ...
    _attr_native_unit_of_measurement: Incomplete
    @constraint_fetcher
    async def async_fetch_constraints(self) -> None: ...
    _attr_native_max_value: Incomplete
    _attr_native_min_value: Incomplete
    _attr_native_step: Incomplete
    def set_constraints(self, setting: GetSetting) -> None: ...
    _attr_native_value: Incomplete
    def update_native_value(self) -> None: ...
    async def async_added_to_hass(self) -> None: ...

class HomeConnectOptionNumberEntity(HomeConnectOptionEntity, NumberEntity):
    async def async_set_native_value(self, value: float) -> None: ...
    _attr_native_value: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    _attr_native_min_value: Incomplete
    _attr_native_max_value: Incomplete
    _attr_native_step: Incomplete
    def update_native_value(self) -> None: ...
