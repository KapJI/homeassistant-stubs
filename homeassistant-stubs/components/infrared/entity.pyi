import abc
from _typeshed import Incomplete
from abc import abstractmethod
from collections.abc import Callable as Callable
from dataclasses import dataclass
from enum import StrEnum
from homeassistant.const import STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, callback as callback
from homeassistant.helpers.deprecation import deprecated_class as deprecated_class
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from infrared_protocols.commands import Command as InfraredCommand
from propcache.api import cached_property
from typing import final, override

_LOGGER: Incomplete

class InfraredDeviceClass(StrEnum):
    EMITTER = 'emitter'
    RECEIVER = 'receiver'

@dataclass(frozen=True, slots=True)
class InfraredReceivedSignal:
    timings: list[int]
    modulation: int | None = ...

class InfraredEmitterEntityDescription(EntityDescription, frozen_or_thawed=True): ...

class InfraredEmitterEntity(RestoreEntity, metaclass=abc.ABCMeta):
    entity_description: InfraredEmitterEntityDescription
    _attr_device_class: InfraredDeviceClass
    _attr_should_poll: bool
    _attr_state: None
    __last_command_sent: str | None
    @property
    @final
    @override
    def state(self) -> str | None: ...
    @final
    async def async_send_command_internal(self, command: InfraredCommand) -> None: ...
    @final
    @override
    async def async_internal_added_to_hass(self) -> None: ...
    @abstractmethod
    async def async_send_command(self, command: InfraredCommand) -> None: ...

class InfraredReceiverEntityDescription(EntityDescription, frozen_or_thawed=True): ...

class InfraredReceiverEntity(RestoreEntity):
    entity_description: InfraredReceiverEntityDescription
    _attr_device_class: InfraredDeviceClass
    _attr_should_poll: bool
    _attr_state: None
    __last_signal_received: str | None
    @cached_property
    def __signal_callbacks(self) -> set[Callable[[InfraredReceivedSignal], None]]: ...
    @property
    @final
    @override
    def state(self) -> str | None: ...
    @final
    @override
    async def async_internal_added_to_hass(self) -> None: ...
    @final
    def _handle_received_signal(self, signal: InfraredReceivedSignal) -> None: ...
    @callback
    def async_subscribe_received_signal(self, signal_callback: Callable[[InfraredReceivedSignal], None]) -> CALLBACK_TYPE: ...

class InfraredEntityDescription(InfraredEmitterEntityDescription): ...
class InfraredEntity(InfraredEmitterEntity, metaclass=abc.ABCMeta): ...
