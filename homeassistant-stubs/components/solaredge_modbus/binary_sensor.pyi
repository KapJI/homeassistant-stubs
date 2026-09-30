from .coordinator import SolarEdgeModbusConfigEntry as SolarEdgeModbusConfigEntry
from .entity import SolarEdgeModbusBatteryEntity as SolarEdgeModbusBatteryEntity, SolarEdgeModbusInverterEntity as SolarEdgeModbusInverterEntity
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from solaredged import Battery as Battery, Inverter as Inverter
from typing import override

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class SolarEdgeModbusBinarySensorEntityDescription[ComponentT](BinarySensorEntityDescription):
    exists_fn: Callable[[ComponentT], bool] = ...
    is_on_fn: Callable[[ComponentT], bool | None]

def _faulted(inverter: Inverter) -> bool | None: ...
def _charging(battery: Battery) -> bool | None: ...

INVERTER_BINARY_SENSORS: tuple[SolarEdgeModbusBinarySensorEntityDescription[Inverter], ...]
BATTERY_BINARY_SENSORS: tuple[SolarEdgeModbusBinarySensorEntityDescription[Battery], ...]

async def async_setup_entry(hass: HomeAssistant, entry: SolarEdgeModbusConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class SolarEdgeModbusInverterBinarySensorEntity(SolarEdgeModbusInverterEntity, BinarySensorEntity):
    entity_description: SolarEdgeModbusBinarySensorEntityDescription[Inverter]
    @property
    @override
    def is_on(self) -> bool | None: ...

class SolarEdgeModbusBatteryBinarySensorEntity(SolarEdgeModbusBatteryEntity, BinarySensorEntity):
    entity_description: SolarEdgeModbusBinarySensorEntityDescription[Battery]
    @property
    @override
    def is_on(self) -> bool | None: ...
