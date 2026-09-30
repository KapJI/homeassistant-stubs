from .const import PRINTER_TYPE_INK as PRINTER_TYPE_INK, PRINTER_TYPE_LASER as PRINTER_TYPE_LASER
from .coordinator import BrotherConfigEntry as BrotherConfigEntry
from .entity import BrotherPrinterEntity as BrotherPrinterEntity
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import CONF_TYPE as CONF_TYPE, EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import override

PARALLEL_UPDATES: int
BINARY_SENSOR_TYPES: tuple[BinarySensorEntityDescription, ...]
SUPPLY_BINARY_SENSOR_TYPES: dict[str, tuple[BinarySensorEntityDescription, ...]]

async def async_setup_entry(hass: HomeAssistant, entry: BrotherConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class BrotherPrinterBinarySensor(BrotherPrinterEntity, BinarySensorEntity):
    @property
    @override
    def is_on(self) -> bool: ...
