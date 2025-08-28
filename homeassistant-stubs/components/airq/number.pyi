from . import AirQConfigEntry as AirQConfigEntry, AirQCoordinator as AirQCoordinator
from _typeshed import Incomplete
from aioairq.core import AirQ as AirQ
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.number import NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription
from homeassistant.const import PERCENTAGE as PERCENTAGE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

_LOGGER: Incomplete

@dataclass(frozen=True, kw_only=True)
class AirQBrightnessDescription(NumberEntityDescription):
    value: Callable[[dict], float]
    set_value: Callable[[AirQ, float], Awaitable[None]]

AIRQ_LED_BRIGHTNESS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: AirQConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class AirQLEDBrightness(CoordinatorEntity[AirQCoordinator], NumberEntity):
    _attr_has_entity_name: bool
    entity_description: AirQBrightnessDescription
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: AirQCoordinator, description: AirQBrightnessDescription) -> None: ...
    @property
    def native_value(self) -> float: ...
    async def async_set_native_value(self, value: float) -> None: ...
