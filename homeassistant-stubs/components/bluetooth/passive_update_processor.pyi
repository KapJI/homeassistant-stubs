import logging
from . import BluetoothChange as BluetoothChange, BluetoothScanningMode as BluetoothScanningMode, BluetoothServiceInfoBleak as BluetoothServiceInfoBleak
from .const import DOMAIN as DOMAIN
from .update_coordinator import BasePassiveBluetoothCoordinator as BasePassiveBluetoothCoordinator
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Mapping
from homeassistant.const import ATTR_IDENTIFIERS as ATTR_IDENTIFIERS, ATTR_NAME as ATTR_NAME
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, Entity as Entity, EntityDescription as EntityDescription
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any, TypeVar

class PassiveBluetoothEntityKey:
    key: str
    device_id: Union[str, None]
    def __init__(self, key, device_id) -> None: ...
_T = TypeVar('_T')

class PassiveBluetoothDataUpdate:
    devices: dict[Union[str, None], DeviceInfo]
    entity_descriptions: Mapping[PassiveBluetoothEntityKey, EntityDescription]
    entity_names: Mapping[PassiveBluetoothEntityKey, Union[str, None]]
    entity_data: Mapping[PassiveBluetoothEntityKey, _T]
    def __init__(self, devices, entity_descriptions, entity_names, entity_data) -> None: ...

class PassiveBluetoothProcessorCoordinator(BasePassiveBluetoothCoordinator):
    _processors: Incomplete
    _update_method: Incomplete
    last_update_success: bool
    def __init__(self, hass: HomeAssistant, logger: logging.Logger, address: str, mode: BluetoothScanningMode, update_method: Callable[[BluetoothServiceInfoBleak], _T], connectable: bool = ...) -> None: ...
    @property
    def available(self) -> bool: ...
    def async_register_processor(self, processor: PassiveBluetoothDataProcessor) -> Callable[[], None]: ...
    def _async_handle_unavailable(self, service_info: BluetoothServiceInfoBleak) -> None: ...
    def _async_handle_bluetooth_event(self, service_info: BluetoothServiceInfoBleak, change: BluetoothChange) -> None: ...
_PassiveBluetoothDataProcessorT = TypeVar('_PassiveBluetoothDataProcessorT', bound='PassiveBluetoothDataProcessor[Any]')

class PassiveBluetoothDataProcessor:
    coordinator: PassiveBluetoothProcessorCoordinator
    _listeners: Incomplete
    _entity_key_listeners: Incomplete
    update_method: Incomplete
    entity_names: Incomplete
    entity_data: Incomplete
    entity_descriptions: Incomplete
    devices: Incomplete
    last_update_success: bool
    def __init__(self, update_method: Callable[[_T], PassiveBluetoothDataUpdate[_T]]) -> None: ...
    @property
    def available(self) -> bool: ...
    def async_handle_unavailable(self) -> None: ...
    def async_add_entities_listener(self, entity_class: type[PassiveBluetoothProcessorEntity], async_add_entites: AddEntitiesCallback) -> Callable[[], None]: ...
    def async_add_listener(self, update_callback: Callable[[Union[PassiveBluetoothDataUpdate[_T], None]], None]) -> Callable[[], None]: ...
    def async_add_entity_key_listener(self, update_callback: Callable[[Union[PassiveBluetoothDataUpdate[_T], None]], None], entity_key: PassiveBluetoothEntityKey) -> Callable[[], None]: ...
    def async_update_listeners(self, data: Union[PassiveBluetoothDataUpdate[_T], None]) -> None: ...
    def async_handle_update(self, update: _T) -> None: ...

class PassiveBluetoothProcessorEntity(Entity):
    _attr_has_entity_name: bool
    _attr_should_poll: bool
    entity_description: Incomplete
    entity_key: Incomplete
    processor: Incomplete
    processor_context: Incomplete
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    _attr_name: Incomplete
    def __init__(self, processor: _PassiveBluetoothDataProcessorT, entity_key: PassiveBluetoothEntityKey, description: EntityDescription, context: Any = ...) -> None: ...
    @property
    def available(self) -> bool: ...
    async def async_added_to_hass(self) -> None: ...
    def _handle_processor_update(self, new_data: Union[PassiveBluetoothDataUpdate, None]) -> None: ...
