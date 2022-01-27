from .const import BPUP_SUBS as BPUP_SUBS, DOMAIN as DOMAIN, HUB as HUB
from .entity import BondEntity as BondEntity
from .utils import BondDevice as BondDevice, BondHub as BondHub
from bond_api import Action, BPUPSubscriptions as BPUPSubscriptions
from homeassistant.components.button import ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

_LOGGER: Any
STEP_SIZE: int

class BondButtonEntityDescriptionMixin:
    mutually_exclusive: Union[Action, None]
    argument: Union[int, None]
    def __init__(self, mutually_exclusive, argument) -> None: ...

class BondButtonEntityDescription(ButtonEntityDescription, BondButtonEntityDescriptionMixin):
    def __init__(self, mutually_exclusive, argument, key, device_class, entity_category, entity_registry_enabled_default, force_update, icon, name, unit_of_measurement) -> None: ...

STOP_BUTTON: Any
BUTTONS: tuple[BondButtonEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class BondButtonEntity(BondEntity, ButtonEntity):
    entity_description: BondButtonEntityDescription
    def __init__(self, hub: BondHub, device: BondDevice, bpup_subs: BPUPSubscriptions, description: BondButtonEntityDescription) -> None: ...
    async def async_press(self, **kwargs: Any) -> None: ...
    def _apply_state(self, state: dict) -> None: ...
