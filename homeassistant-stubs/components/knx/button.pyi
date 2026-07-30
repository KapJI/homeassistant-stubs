from .const import CONF_PAYLOAD_LENGTH as CONF_PAYLOAD_LENGTH, CONF_VALUE as CONF_VALUE, DOMAIN as DOMAIN, KNX_ADDRESS as KNX_ADDRESS, KNX_MODULE_KEY as KNX_MODULE_KEY
from .entity import KnxUiEntity as KnxUiEntity, KnxUiEntityPlatformController as KnxUiEntityPlatformController, KnxYamlEntity as KnxYamlEntity, build_yaml_unique_id as build_yaml_unique_id
from .knx_module import KNXModule as KNXModule
from .storage.const import CONF_DATA as CONF_DATA, CONF_ENTITY as CONF_ENTITY, CONF_GA_SEND as CONF_GA_SEND
from .storage.util import ConfigExtractor as ConfigExtractor
from _typeshed import Incomplete
from homeassistant import config_entries as config_entries
from homeassistant.components.button import ButtonEntity as ButtonEntity
from homeassistant.const import CONF_NAME as CONF_NAME, CONF_PAYLOAD as CONF_PAYLOAD, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback, async_get_current_platform as async_get_current_platform
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any, override
from xknx.devices import ExposeSensor as XknxExposeSensor, RawValue as XknxRawValue

async def async_setup_entry(hass: HomeAssistant, config_entry: config_entries.ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class _KnxButton(ButtonEntity):
    _device: XknxRawValue | XknxExposeSensor
    _payload: Any
    @override
    async def async_press(self) -> None: ...

class KnxYamlButton(_KnxButton, KnxYamlEntity):
    _device: XknxRawValue
    _payload: Incomplete
    def __init__(self, knx_module: KNXModule, config: ConfigType) -> None: ...

class KnxUiButton(_KnxButton, KnxUiEntity):
    _device: XknxRawValue | XknxExposeSensor
    _payload: Incomplete
    def __init__(self, knx_module: KNXModule, unique_id: str, config: dict[str, Any]) -> None: ...
