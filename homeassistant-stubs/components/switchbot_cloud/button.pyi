from . import SwitchBotCoordinator as SwitchBotCoordinator, SwitchbotCloudConfigEntry as SwitchbotCloudConfigEntry
from .entity import SwitchBotCloudEntity as SwitchBotCloudEntity
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.button import ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from switchbot_api import Commands as SwitchBotCloudBaseCommands, Device as Device, Remote as Remote, SwitchBotAPI as SwitchBotAPI
from typing import Any

@dataclass(frozen=True, kw_only=True)
class SwitchbotCloudButtonEntityDescription(ButtonEntityDescription):
    command: SwitchBotCloudBaseCommands = ...
    command_type: str = ...
    parameters: dict | str = ...

BOT_BUTTON_DESCRIPTION: Incomplete
ART_FRAME_NEXT_BUTTON_DESCRIPTION: Incomplete
ART_FRAME_PREVIOUS_BUTTON_DESCRIPTION: Incomplete
BUTTON_DESCRIPTIONS_BY_DEVICE_TYPES: Incomplete

async def async_setup_entry(hass: HomeAssistant, config: SwitchbotCloudConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class SwitchBotCloudBot(SwitchBotCloudEntity, ButtonEntity):
    entity_description: SwitchbotCloudButtonEntityDescription
    _attr_unique_id: Incomplete
    _device_id: Incomplete
    def __init__(self, api: SwitchBotAPI, device: Device, coordinator: SwitchBotCoordinator, description: SwitchbotCloudButtonEntityDescription) -> None: ...
    async def async_press(self, **kwargs: Any) -> None: ...

@callback
def _async_make_entity(api: SwitchBotAPI, device: Device | Remote, coordinator: SwitchBotCoordinator, description: SwitchbotCloudButtonEntityDescription) -> SwitchBotCloudBot: ...
