from .const import CONF_USE_AUX1 as CONF_USE_AUX1, CONF_USE_AUX2 as CONF_USE_AUX2, CONF_USE_AUX3 as CONF_USE_AUX3, CONF_USE_AUX4 as CONF_USE_AUX4, CONF_USE_COVER_SENSOR as CONF_USE_COVER_SENSOR, CONF_USE_LIGHT as CONF_USE_LIGHT
from .coordinator import NeoPoolConfigEntry as NeoPoolConfigEntry, NeoPoolCoordinator as NeoPoolCoordinator
from .entity import NeoPoolEntity as NeoPoolEntity
from _typeshed import Incomplete
from collections.abc import Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any, override

PARALLEL_UPDATES: int
type _SupportedFn = Callable[[dict[str, Any]], bool]

@dataclass(frozen=True, kw_only=True)
class NeoPoolBinarySensorEntityDescription(BinarySensorEntityDescription):
    supported_fn: _SupportedFn | None = ...
    value_fn: Callable[[dict[str, Any], HomeAssistant], bool | None] | None = ...

def _gpio_ok(gpio_key: str) -> _SupportedFn: ...
def _pool_cover_open(data: dict[str, Any], hass: HomeAssistant) -> bool | None: ...

BINARY_SENSOR_DESCRIPTIONS: dict[str, NeoPoolBinarySensorEntityDescription]
_ENTITY_OPTION_KEY: dict[str, str]

async def async_setup_entry(hass: HomeAssistant, entry: NeoPoolConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class NeoPoolBinarySensor(NeoPoolEntity, BinarySensorEntity):
    _winter_mode_active: bool
    entity_description: NeoPoolBinarySensorEntityDescription
    _key: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: NeoPoolCoordinator, key: str, description: NeoPoolBinarySensorEntityDescription) -> None: ...
    @property
    @override
    def is_on(self) -> bool | None: ...
