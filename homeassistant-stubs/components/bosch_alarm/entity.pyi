from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from bosch_alarm_mode2 import Panel as Panel
from homeassistant.components.sensor import Entity as Entity
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo

PARALLEL_UPDATES: int

class BoschAlarmEntity(Entity):
    _attr_has_entity_name: bool
    panel: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, panel: Panel, unique_id: str) -> None: ...
    @property
    def available(self) -> bool: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...

class BoschAlarmAreaEntity(BoschAlarmEntity):
    _area_id: Incomplete
    _area_unique_id: Incomplete
    _observe_alarms: Incomplete
    _observe_ready: Incomplete
    _observe_status: Incomplete
    _area: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, panel: Panel, area_id: int, unique_id: str, observe_alarms: bool, observe_ready: bool, observe_status: bool) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
