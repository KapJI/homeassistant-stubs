from . import EsphomeEntity as EsphomeEntity, platform_async_setup_entry as platform_async_setup_entry
from aioesphomeapi import BinarySensorInfo, BinarySensorState
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class EsphomeBinarySensor(EsphomeEntity[BinarySensorInfo, BinarySensorState], BinarySensorEntity):
    @property
    def is_on(self) -> Union[bool, None]: ...
    @property
    def device_class(self) -> str: ...
    @property
    def available(self) -> bool: ...
