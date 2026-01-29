from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from pooldose.client import PooldoseClient as PooldoseClient
from pooldose.type_definitions import DeviceInfoDict as DeviceInfoDict, StructuredValuesDict

_LOGGER: Incomplete
type PooldoseConfigEntry = ConfigEntry[PooldoseCoordinator]

class PooldoseCoordinator(DataUpdateCoordinator[StructuredValuesDict]):
    device_info: DeviceInfoDict
    config_entry: PooldoseConfigEntry
    client: Incomplete
    def __init__(self, hass: HomeAssistant, client: PooldoseClient, config_entry: PooldoseConfigEntry) -> None: ...
    async def _async_setup(self) -> None: ...
    async def _async_update_data(self) -> StructuredValuesDict: ...
