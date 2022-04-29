from . import LcnEntity as LcnEntity
from .const import CONF_DOMAIN_DATA as CONF_DOMAIN_DATA, CONF_OUTPUTS as CONF_OUTPUTS, CONF_REGISTER as CONF_REGISTER, CONF_TRANSITION as CONF_TRANSITION, OUTPUT_PORTS as OUTPUT_PORTS
from .helpers import DeviceConnectionType as DeviceConnectionType, get_device_connection as get_device_connection
from _typeshed import Incomplete
from homeassistant.components.scene import Scene as Scene
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_ADDRESS as CONF_ADDRESS, CONF_DOMAIN as CONF_DOMAIN, CONF_ENTITIES as CONF_ENTITIES, CONF_SCENE as CONF_SCENE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

PARALLEL_UPDATES: int

def create_lcn_scene_entity(hass: HomeAssistant, entity_config: ConfigType, config_entry: ConfigEntry) -> LcnEntity: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class LcnScene(LcnEntity, Scene):
    register_id: Incomplete
    scene_id: Incomplete
    output_ports: Incomplete
    relay_ports: Incomplete
    transition: Incomplete
    def __init__(self, config: ConfigType, entry_id: str, device_connection: DeviceConnectionType) -> None: ...
    async def async_activate(self, **kwargs: Any) -> None: ...
