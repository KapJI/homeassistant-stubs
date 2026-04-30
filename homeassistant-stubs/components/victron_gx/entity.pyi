import abc
from _typeshed import Incomplete
from abc import abstractmethod
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import Entity as Entity
from typing import Any
from victron_mqtt import Device as VictronVenusDevice, Metric as VictronVenusMetric

ENTITIES_CATEGORY_DIAGNOSTIC: Incomplete
ENTITIES_DISABLE_BY_DEFAULT: Incomplete

class VictronBaseEntity(Entity, metaclass=abc.ABCMeta):
    _attr_should_poll: bool
    _attr_has_entity_name: bool
    _device: Incomplete
    _metric: Incomplete
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    _attr_suggested_display_precision: Incomplete
    _attr_name: Incomplete
    _attr_translation_key: Incomplete
    _attr_translation_placeholders: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    _attr_entity_category: Incomplete
    _attr_entity_registry_enabled_default: Incomplete
    def __init__(self, device: VictronVenusDevice, metric: VictronVenusMetric, device_info: DeviceInfo, installation_id: str) -> None: ...
    @callback
    @abstractmethod
    def _on_update_cb(self, value: Any) -> None: ...
    @callback
    def _on_update(self, _: VictronVenusMetric, value: Any) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
