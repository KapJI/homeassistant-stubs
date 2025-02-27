from .common import setup_home_connect_entry as setup_home_connect_entry
from .const import DOMAIN as DOMAIN, SVE_TRANSLATION_KEY_SET_SETTING as SVE_TRANSLATION_KEY_SET_SETTING, SVE_TRANSLATION_PLACEHOLDER_ENTITY_ID as SVE_TRANSLATION_PLACEHOLDER_ENTITY_ID, SVE_TRANSLATION_PLACEHOLDER_KEY as SVE_TRANSLATION_PLACEHOLDER_KEY, SVE_TRANSLATION_PLACEHOLDER_VALUE as SVE_TRANSLATION_PLACEHOLDER_VALUE
from .coordinator import HomeConnectApplianceData as HomeConnectApplianceData, HomeConnectConfigEntry as HomeConnectConfigEntry
from .entity import HomeConnectEntity as HomeConnectEntity
from .utils import get_dict_from_home_connect_error as get_dict_from_home_connect_error
from _typeshed import Incomplete
from datetime import time
from homeassistant.components.time import TimeEntity as TimeEntity, TimeEntityDescription as TimeEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

PARALLEL_UPDATES: int
TIME_ENTITIES: Incomplete

def _get_entities_for_appliance(entry: HomeConnectConfigEntry, appliance: HomeConnectApplianceData) -> list[HomeConnectEntity]: ...
async def async_setup_entry(hass: HomeAssistant, entry: HomeConnectConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...
def seconds_to_time(seconds: int) -> time: ...
def time_to_seconds(t: time) -> int: ...

class HomeConnectTimeEntity(HomeConnectEntity, TimeEntity):
    async def async_set_value(self, value: time) -> None: ...
    _attr_native_value: Incomplete
    def update_native_value(self) -> None: ...
