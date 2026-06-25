from . import OverkizDataConfigEntry as OverkizDataConfigEntry
from _typeshed import Incomplete
from homeassistant.components.scene import Scene as Scene
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pyoverkiz.client import OverkizClient as OverkizClient
from pyoverkiz.models import PersistedActionGroup as PersistedActionGroup
from typing import Any, override

async def async_setup_entry(hass: HomeAssistant, entry: OverkizDataConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class OverkizScene(Scene):
    scenario: Incomplete
    client: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, scenario: PersistedActionGroup, client: OverkizClient) -> None: ...
    @override
    async def async_activate(self, **kwargs: Any) -> None: ...
