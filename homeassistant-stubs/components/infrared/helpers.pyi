import abc
from .const import DATA_COMPONENT as DATA_COMPONENT, DOMAIN as DOMAIN
from .entity import InfraredEmitterEntity as InfraredEmitterEntity, InfraredReceivedSignal as InfraredReceivedSignal, InfraredReceiverEntity as InfraredReceiverEntity
from _typeshed import Incomplete
from abc import abstractmethod
from collections.abc import Callable as Callable
from homeassistant.const import STATE_UNAVAILABLE as STATE_UNAVAILABLE
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, Context as Context, Event as Event, EventStateChangedData as EventStateChangedData, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.event import async_track_state_change_event as async_track_state_change_event
from infrared_protocols.commands import Command as InfraredCommand
from typing import override

_LOGGER: Incomplete

async def async_send_command(hass: HomeAssistant, entity_id_or_uuid: str, command: InfraredCommand, context: Context | None = None) -> None: ...
@callback
def async_subscribe_receiver(hass: HomeAssistant, entity_id_or_uuid: str, signal_callback: Callable[[InfraredReceivedSignal], None]) -> CALLBACK_TYPE: ...

class InfraredConsumerEntity(Entity):
    _attr_available: Incomplete
    @callback
    def _async_track_availability(self, infrared_entity_id: str) -> CALLBACK_TYPE: ...
    @callback
    def _async_infrared_availability_changed(self, available: bool) -> None: ...

class InfraredEmitterConsumerEntity(InfraredConsumerEntity):
    _attr_should_poll: bool
    _infrared_emitter_entity_id: str
    @override
    async def async_added_to_hass(self) -> None: ...
    async def _send_command(self, command: InfraredCommand) -> None: ...

class InfraredReceiverConsumerEntity(InfraredConsumerEntity, metaclass=abc.ABCMeta):
    _attr_should_poll: bool
    _infrared_receiver_entity_id: str
    _remove_signal_subscription: CALLBACK_TYPE | None
    @override
    async def async_added_to_hass(self) -> None: ...
    @override
    @callback
    def _async_infrared_availability_changed(self, available: bool) -> None: ...
    @callback
    @abstractmethod
    def _handle_signal(self, signal: InfraredReceivedSignal) -> None: ...
    @callback
    def _async_unsubscribe_receiver(self) -> None: ...
    @callback
    def _async_update_receiver_subscription(self) -> None: ...
