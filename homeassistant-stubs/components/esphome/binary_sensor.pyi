from .domain_data import DomainData as DomainData
from .entity import EsphomeAssistEntity as EsphomeAssistEntity, EsphomeEntity as EsphomeEntity, platform_async_setup_entry as platform_async_setup_entry
from _typeshed import Incomplete
from aioesphomeapi import BinarySensorInfo, BinarySensorState, EntityInfo as EntityInfo
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.util.enum import try_parse_enum as try_parse_enum

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class EsphomeBinarySensor(EsphomeEntity[BinarySensorInfo, BinarySensorState], BinarySensorEntity):
    @property
    def is_on(self) -> bool | None: ...
    _attr_device_class: Incomplete
    def _on_static_info_update(self, static_info: EntityInfo) -> None: ...
    @property
    def available(self) -> bool: ...

class EsphomeAssistInProgressBinarySensor(EsphomeAssistEntity, BinarySensorEntity):
    entity_description: Incomplete
    @property
    def is_on(self) -> bool | None: ...
