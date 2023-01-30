from .const import DOMAIN as DOMAIN
from .coordinator import HWEnergyDeviceUpdateCoordinator as HWEnergyDeviceUpdateCoordinator
from .entity import HomeWizardEntity as HomeWizardEntity
from .helpers import homewizard_exception_handler as homewizard_exception_handler
from _typeshed import Incomplete
from homeassistant.components.button import ButtonEntity as ButtonEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class HomeWizardIdentifyButton(HomeWizardEntity, ButtonEntity):
    _attr_entity_category: Incomplete
    _attr_icon: str
    _attr_name: str
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: HWEnergyDeviceUpdateCoordinator, entry: ConfigEntry) -> None: ...
    async def async_press(self) -> None: ...
