from .const import CONF_CONNECTIONS as CONF_CONNECTIONS, DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from pyfritzhome import Fritzhome as Fritzhome, FritzhomeDevice as FritzhomeDevice
from pyfritzhome.devicetypes import FritzhomeTemplate as FritzhomeTemplate

@dataclass
class FritzboxCoordinatorData:
    devices: dict[str, FritzhomeDevice]
    templates: dict[str, FritzhomeTemplate]
    def __init__(self, devices, templates) -> None: ...

class FritzboxDataUpdateCoordinator(DataUpdateCoordinator[FritzboxCoordinatorData]):
    configuration_url: str
    entry: Incomplete
    fritz: Incomplete
    has_templates: Incomplete
    def __init__(self, hass: HomeAssistant, entry: ConfigEntry, has_templates: bool) -> None: ...
    def _update_fritz_devices(self) -> FritzboxCoordinatorData: ...
    async def _async_update_data(self) -> FritzboxCoordinatorData: ...
