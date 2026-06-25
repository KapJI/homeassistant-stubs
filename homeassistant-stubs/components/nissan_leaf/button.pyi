from . import DATA_CHARGING as DATA_CHARGING, DATA_LEAF as DATA_LEAF
from .entity import LeafEntity as LeafEntity
from _typeshed import Incomplete
from homeassistant.components.button import ButtonEntity as ButtonEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import override

_LOGGER: Incomplete

def setup_platform(hass: HomeAssistant, config: ConfigType, add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...

class LeafChargingButton(LeafEntity, ButtonEntity):
    _attr_icon: str
    @property
    @override
    def name(self) -> str: ...
    @property
    @override
    def available(self) -> bool: ...
    @override
    async def async_press(self) -> None: ...
