from .const import DOMAIN as DOMAIN
from .entity import BondEntity as BondEntity
from .models import BondData as BondData
from .utils import BondDevice as BondDevice, BondHub as BondHub
from _typeshed import Incomplete
from bond_async import Action, BPUPSubscriptions as BPUPSubscriptions
from homeassistant.components.button import ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

STEP_SIZE: int

class BondButtonEntityDescriptionMixin:
    mutually_exclusive: Action | None
    argument: int | None
    def __init__(self, mutually_exclusive, argument) -> None: ...

class BondButtonEntityDescription(ButtonEntityDescription, BondButtonEntityDescriptionMixin):
    name: str | None
    def __init__(self, mutually_exclusive, argument, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement) -> None: ...

STOP_BUTTON: Incomplete
BUTTONS: tuple[BondButtonEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class BondButtonEntity(BondEntity, ButtonEntity):
    entity_description: BondButtonEntityDescription
    def __init__(self, hub: BondHub, device: BondDevice, bpup_subs: BPUPSubscriptions, description: BondButtonEntityDescription) -> None: ...
    async def async_press(self) -> None: ...
    def _apply_state(self) -> None: ...
