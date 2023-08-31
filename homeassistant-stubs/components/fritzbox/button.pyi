from . import FritzBoxEntity as FritzBoxEntity, FritzboxDataUpdateCoordinator as FritzboxDataUpdateCoordinator
from .const import CONF_COORDINATOR as CONF_COORDINATOR
from homeassistant.components.button import ButtonEntity as ButtonEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pyfritzhome.devicetypes import FritzhomeTemplate as FritzhomeTemplate

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class FritzBoxTemplate(FritzBoxEntity, ButtonEntity):
    @property
    def data(self) -> FritzhomeTemplate: ...
    @property
    def device_info(self) -> DeviceInfo: ...
    async def async_press(self) -> None: ...
    def apply_template(self) -> None: ...
