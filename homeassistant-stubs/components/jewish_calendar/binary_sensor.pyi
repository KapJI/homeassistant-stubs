from . import DOMAIN as DOMAIN
from _typeshed import Incomplete
from datetime import datetime
from hdate.zmanim import Zmanim as Zmanim
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import event as event
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType

BINARY_SENSORS: Incomplete

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: Union[DiscoveryInfoType, None] = ...) -> None: ...

class JewishCalendarBinarySensor(BinarySensorEntity):
    _attr_should_poll: bool
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    _location: Incomplete
    _hebrew: Incomplete
    _candle_lighting_offset: Incomplete
    _havdalah_offset: Incomplete
    _update_unsub: Incomplete
    def __init__(self, data: dict[str, Union[str, bool, int, float]], description: BinarySensorEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool: ...
    def _get_zmanim(self) -> Zmanim: ...
    async def async_added_to_hass(self) -> None: ...
    def _update(self, now: Union[datetime, None] = ...) -> None: ...
    def _schedule_update(self) -> None: ...
