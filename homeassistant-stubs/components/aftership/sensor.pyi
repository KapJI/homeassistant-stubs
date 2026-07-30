from . import AfterShipConfigEntry as AfterShipConfigEntry
from .const import ATTRIBUTION as ATTRIBUTION, ATTR_TRACKINGS as ATTR_TRACKINGS, BASE as BASE, DOMAIN as DOMAIN, MIN_TIME_BETWEEN_UPDATES as MIN_TIME_BETWEEN_UPDATES, UPDATE_TOPIC as UPDATE_TOPIC
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorEntity as SensorEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.util import Throttle as Throttle
from pyaftership import AfterShip as AfterShip
from typing import Any, Final, override

_LOGGER: Final[Incomplete]
PLATFORM_SCHEMA: Final[Incomplete]

async def async_setup_entry(hass: HomeAssistant, config_entry: AfterShipConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class AfterShipSensor(SensorEntity):
    _attr_attribution = ATTRIBUTION
    _attr_native_unit_of_measurement: str
    _attr_translation_key: str
    _attributes: dict[str, Any]
    _state: int | None
    aftership: Incomplete
    _attr_name: Incomplete
    def __init__(self, aftership: AfterShip, name: str) -> None: ...
    @property
    @override
    def native_value(self) -> int | None: ...
    @property
    @override
    def extra_state_attributes(self) -> dict[str, str]: ...
    @override
    async def async_added_to_hass(self) -> None: ...
    async def _force_update(self) -> None: ...
    async def async_update(self, **kwargs: Any) -> None: ...
