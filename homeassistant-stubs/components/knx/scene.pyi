from .const import DATA_KNX_CONFIG as DATA_KNX_CONFIG, DOMAIN as DOMAIN, KNX_ADDRESS as KNX_ADDRESS
from .knx_entity import KnxEntity as KnxEntity
from .schema import SceneSchema as SceneSchema
from _typeshed import Incomplete
from homeassistant import config_entries as config_entries
from homeassistant.components.scene import Scene as Scene
from homeassistant.const import CONF_ENTITY_CATEGORY as CONF_ENTITY_CATEGORY, CONF_NAME as CONF_NAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any
from xknx import XKNX as XKNX
from xknx.devices import Scene as XknxScene

async def async_setup_entry(hass: HomeAssistant, config_entry: config_entries.ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class KNXScene(KnxEntity, Scene):
    _device: XknxScene
    _attr_entity_category: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, xknx: XKNX, config: ConfigType) -> None: ...
    async def async_activate(self, **kwargs: Any) -> None: ...
