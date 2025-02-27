from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from anova_wifi import APCUpdate, APCWifiDevice as APCWifiDevice, AnovaApi as AnovaApi
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator

_LOGGER: Incomplete

@dataclass
class AnovaData:
    api_jwt: str
    coordinators: list[AnovaCoordinator]
    api: AnovaApi
type AnovaConfigEntry = ConfigEntry[AnovaData]

class AnovaCoordinator(DataUpdateCoordinator[APCUpdate]):
    config_entry: AnovaConfigEntry
    device_unique_id: Incomplete
    anova_device: Incomplete
    device_info: DeviceInfo | None
    sensor_data_set: bool
    def __init__(self, hass: HomeAssistant, config_entry: AnovaConfigEntry, anova_device: APCWifiDevice) -> None: ...
