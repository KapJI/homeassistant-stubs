from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from anova_wifi import AnovaPrecisionCooker as AnovaPrecisionCooker
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

_LOGGER: Incomplete

class AnovaCoordinator(DataUpdateCoordinator):
    data: dict[str, dict[str, str | int | float]]
    _device_unique_id: Incomplete
    anova_device: Incomplete
    device_info: Incomplete
    def __init__(self, hass: HomeAssistant, anova_device: AnovaPrecisionCooker) -> None: ...
    def async_setup(self, firmware_version: str) -> None: ...
    async def _async_update_data(self) -> dict[str, dict[str, str | int | float]]: ...
