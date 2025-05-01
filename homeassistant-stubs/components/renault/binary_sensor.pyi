from . import RenaultConfigEntry as RenaultConfigEntry
from .entity import RenaultDataEntity as RenaultDataEntity, RenaultDataEntityDescription as RenaultDataEntityDescription
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from renault_api.kamereon.enums import ChargeState
from renault_api.kamereon.models import KamereonVehicleBatteryStatusData

PARALLEL_UPDATES: int
_PLUG_FROM_CHARGE_STATUS: set[ChargeState]

@dataclass(frozen=True, kw_only=True)
class RenaultBinarySensorEntityDescription(BinarySensorEntityDescription, RenaultDataEntityDescription):
    on_key: str | None = ...
    on_value: StateType | None = ...
    value_lambda: Callable[[RenaultBinarySensor], bool | None] | None = ...

async def async_setup_entry(hass: HomeAssistant, config_entry: RenaultConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class RenaultBinarySensor(RenaultDataEntity[KamereonVehicleBatteryStatusData], BinarySensorEntity):
    entity_description: RenaultBinarySensorEntityDescription
    @property
    def is_on(self) -> bool | None: ...

def _plugged_in_value_lambda(self) -> bool | None: ...

BINARY_SENSOR_TYPES: tuple[RenaultBinarySensorEntityDescription, ...]
