from .coordinator import AirOSConfigEntry as AirOSConfigEntry, AirOSDataUpdateCoordinator as AirOSDataUpdateCoordinator, DOMAIN as DOMAIN
from .entity import AirOSEntity as AirOSEntity
from _typeshed import Incomplete
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

PARALLEL_UPDATES: int
REBOOT_BUTTON: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: AirOSConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class AirOSRebootButton(AirOSEntity, ButtonEntity):
    entity_description: ButtonEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: AirOSDataUpdateCoordinator, description: ButtonEntityDescription) -> None: ...
    async def async_press(self) -> None: ...
