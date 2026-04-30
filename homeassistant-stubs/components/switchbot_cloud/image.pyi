from . import SwitchBotCoordinator as SwitchBotCoordinator, SwitchbotCloudConfigEntry as SwitchbotCloudConfigEntry
from .entity import SwitchBotCloudEntity as SwitchBotCloudEntity
from _typeshed import Incomplete
from homeassistant.components.image import ImageEntity as ImageEntity
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from switchbot_api import Device as Device, Remote as Remote, SwitchBotAPI as SwitchBotAPI

async def async_setup_entry(hass: HomeAssistant, config: SwitchbotCloudConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class SwitchBotCloudImage(SwitchBotCloudEntity, ImageEntity):
    _attr_translation_key: str
    _image_content: bytes
    def __init__(self, api: SwitchBotAPI, device: Device | Remote, coordinator: SwitchBotCoordinator) -> None: ...
    async def async_image(self) -> bytes | None: ...
    _attr_image_last_updated: Incomplete
    _attr_image_url: Incomplete
    def _set_attributes(self) -> None: ...

@callback
def _async_make_entity(api: SwitchBotAPI, device: Device | Remote, coordinator: SwitchBotCoordinator) -> SwitchBotCloudImage: ...
