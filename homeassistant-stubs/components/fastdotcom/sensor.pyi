from . import DATA_UPDATED as DATA_UPDATED
from homeassistant.components.sensor import SensorEntity as SensorEntity
from homeassistant.const import DATA_RATE_MEGABITS_PER_SECOND as DATA_RATE_MEGABITS_PER_SECOND
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

ICON: str

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: Union[DiscoveryInfoType, None] = ...) -> None: ...

class SpeedtestSensor(RestoreEntity, SensorEntity):
    _attr_name: str
    _attr_unit_of_measurement: Any
    _attr_icon: Any
    _attr_should_poll: bool
    _attr_state: Any
    _speedtest_data: Any
    def __init__(self, speedtest_data: dict[str, Any]) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    def update(self) -> None: ...
    def _schedule_immediate_update(self) -> None: ...
