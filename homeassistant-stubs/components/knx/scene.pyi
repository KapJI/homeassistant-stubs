from .const import DOMAIN as DOMAIN
from .knx_entity import KnxEntity as KnxEntity
from homeassistant.components.scene import Scene as Scene
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any, Callable, Iterable
from xknx.devices import Scene as XknxScene

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: Callable[[Iterable[Entity]], None], discovery_info: Union[DiscoveryInfoType, None]=...) -> None: ...

class KNXScene(KnxEntity, Scene):
    _device: Any
    def __init__(self, device: XknxScene) -> None: ...
    async def async_activate(self, **kwargs: Any) -> None: ...
