from .coordinator import AmazonConfigEntry as AmazonConfigEntry, AmazonDevicesCoordinator as AmazonDevicesCoordinator, alexa_api_call as alexa_api_call
from .entity import AmazonServiceEntity as AmazonServiceEntity
from _typeshed import Incomplete
from homeassistant.components.button import ButtonEntity as ButtonEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.util import slugify as slugify
from typing import override

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: AmazonConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class AmazonRoutineButton(AmazonServiceEntity, ButtonEntity):
    _routine: Incomplete
    def __init__(self, coordinator: AmazonDevicesCoordinator, routine: str) -> None: ...
    @override
    async def async_press(self) -> None: ...
