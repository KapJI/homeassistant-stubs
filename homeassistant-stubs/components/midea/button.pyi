from .const import DOMAIN as DOMAIN
from .entity import MideaConfigEntry as MideaConfigEntry, MideaEntity as MideaEntity, midea_api_call as midea_api_call
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.button import ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ServiceValidationError as ServiceValidationError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from midealocal.const import DeviceType
from midealocal.device import MideaDevice as MideaDevice
from typing import override

PARALLEL_UPDATES: int

@dataclass(kw_only=True, frozen=True)
class MideaButtonEntityDescription(ButtonEntityDescription):
    models: list[DeviceType]
    supported_models: list[str]
    press_fn: Callable[[MideaDevice], None]

def _e1_button_press(device: MideaDevice) -> None: ...

BUTTONS: list[MideaButtonEntityDescription]

async def async_setup_entry(hass: HomeAssistant, config_entry: MideaConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class MideaButton(MideaEntity, ButtonEntity):
    entity_description: MideaButtonEntityDescription
    @override
    async def async_press(self) -> None: ...
