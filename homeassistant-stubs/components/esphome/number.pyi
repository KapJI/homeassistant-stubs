from .entity import EsphomeEntity as EsphomeEntity, esphome_state_property as esphome_state_property, platform_async_setup_entry as platform_async_setup_entry
from .enum_mapper import EsphomeEnumMapper as EsphomeEnumMapper
from _typeshed import Incomplete
from aioesphomeapi import EntityInfo as EntityInfo, NumberInfo, NumberMode as EsphomeNumberMode, NumberState
from homeassistant.components.number import NumberDeviceClass as NumberDeviceClass, NumberEntity as NumberEntity, NumberMode as NumberMode
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.util.enum import try_parse_enum as try_parse_enum

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

NUMBER_MODES: EsphomeEnumMapper[EsphomeNumberMode, NumberMode]

class EsphomeNumber(EsphomeEntity[NumberInfo, NumberState], NumberEntity):
    _attr_device_class: Incomplete
    _attr_native_min_value: Incomplete
    _attr_native_max_value: Incomplete
    _attr_native_step: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    _attr_mode: Incomplete
    def _on_static_info_update(self, static_info: EntityInfo) -> None: ...
    @property
    def native_value(self) -> float | None: ...
    async def async_set_native_value(self, value: float) -> None: ...
