from .const import DOMAIN as DOMAIN, KNX_ADDRESS as KNX_ADDRESS, KNX_MODULE_KEY as KNX_MODULE_KEY, SceneConf as SceneConf
from .entity import KnxUiEntity as KnxUiEntity, KnxUiEntityPlatformController as KnxUiEntityPlatformController, KnxYamlEntity as KnxYamlEntity, _KnxEntityBase as _KnxEntityBase
from .knx_module import KNXModule as KNXModule
from .schema import SceneSchema as SceneSchema
from .storage.const import CONF_ENTITY as CONF_ENTITY, CONF_GA_SCENE as CONF_GA_SCENE
from .storage.util import ConfigExtractor as ConfigExtractor
from _typeshed import Incomplete
from homeassistant import config_entries as config_entries
from homeassistant.components.scene import BaseScene as BaseScene
from homeassistant.const import CONF_ENTITY_CATEGORY as CONF_ENTITY_CATEGORY, CONF_NAME as CONF_NAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback, async_get_current_platform as async_get_current_platform
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any
from xknx.devices import Device as XknxDevice, Scene as XknxScene

async def async_setup_entry(hass: HomeAssistant, config_entry: config_entries.ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class _KnxScene(BaseScene, _KnxEntityBase):
    _device: XknxScene
    async def _async_activate(self, **kwargs: Any) -> None: ...
    def after_update_callback(self, device: XknxDevice) -> None: ...

class KnxYamlScene(_KnxScene, KnxYamlEntity):
    _device: XknxScene
    _attr_entity_category: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, knx_module: KNXModule, config: ConfigType) -> None: ...

class KnxUiScene(_KnxScene, KnxUiEntity):
    _device: XknxScene
    def __init__(self, knx_module: KNXModule, unique_id: str, config: ConfigType) -> None: ...
