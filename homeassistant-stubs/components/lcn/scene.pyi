from .const import CONF_DOMAIN_DATA as CONF_DOMAIN_DATA, CONF_OUTPUTS as CONF_OUTPUTS, CONF_REGISTER as CONF_REGISTER, CONF_TRANSITION as CONF_TRANSITION, OUTPUT_PORTS as OUTPUT_PORTS
from .entity import LcnEntity as LcnEntity
from .helpers import LcnConfigEntry as LcnConfigEntry
from _typeshed import Incomplete
from collections.abc import Iterable
from homeassistant.components.scene import Scene as Scene
from homeassistant.const import CONF_DOMAIN as CONF_DOMAIN, CONF_ENTITIES as CONF_ENTITIES, CONF_SCENE as CONF_SCENE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

PARALLEL_UPDATES: int

def add_lcn_entities(config_entry: LcnConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback, entity_configs: Iterable[ConfigType]) -> None: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: LcnConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LcnScene(LcnEntity, Scene):
    register_id: Incomplete
    scene_id: Incomplete
    output_ports: Incomplete
    relay_ports: Incomplete
    transition: Incomplete
    def __init__(self, config: ConfigType, config_entry: LcnConfigEntry) -> None: ...
    async def async_activate(self, **kwargs: Any) -> None: ...
