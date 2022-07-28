from .const import COORDINATOR as COORDINATOR, DOMAIN as DOMAIN
from .coordinator import YaleDataUpdateCoordinator as YaleDataUpdateCoordinator
from .entity import YaleAlarmEntity as YaleAlarmEntity
from _typeshed import Incomplete
from homeassistant.components.button import ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

BUTTON_TYPES: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class YalePanicButton(YaleAlarmEntity, ButtonEntity):
    entity_description: ButtonEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: YaleDataUpdateCoordinator, description: ButtonEntityDescription) -> None: ...
    async def async_press(self) -> None: ...
