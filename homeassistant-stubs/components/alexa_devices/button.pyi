from .coordinator import AmazonConfigEntry as AmazonConfigEntry, AmazonDevicesCoordinator as AmazonDevicesCoordinator, alexa_api_call as alexa_api_call
from .entity import AmazonEntity as AmazonEntity, AmazonServiceEntity as AmazonServiceEntity
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.util import slugify as slugify
from typing import Final, override

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class AmazonButtonEntityDescription(ButtonEntityDescription):
    capability: str

DEVICE_BUTTONS: Final[Incomplete]

async def async_setup_entry(hass: HomeAssistant, entry: AmazonConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class AmazonRoutineButton(AmazonServiceEntity, ButtonEntity):
    _routine: Incomplete
    def __init__(self, coordinator: AmazonDevicesCoordinator, routine: str) -> None: ...
    @override
    async def async_press(self) -> None: ...

class AmazonDeviceButton(AmazonEntity, ButtonEntity):
    @override
    async def async_press(self) -> None: ...
