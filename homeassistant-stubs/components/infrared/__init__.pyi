from .const import DOMAIN as DOMAIN
from .entity import InfraredCommand as InfraredCommand, InfraredEmitterEntity as InfraredEmitterEntity, InfraredEmitterEntityDescription as InfraredEmitterEntityDescription, InfraredEntity as InfraredEntity, InfraredEntityDescription as InfraredEntityDescription, InfraredReceivedSignal as InfraredReceivedSignal, InfraredReceiverEntity as InfraredReceiverEntity, InfraredReceiverEntityDescription as InfraredReceiverEntityDescription
from .helpers import InfraredEmitterConsumerEntity as InfraredEmitterConsumerEntity, InfraredReceiverConsumerEntity as InfraredReceiverConsumerEntity, async_send_command as async_send_command, async_subscribe_receiver as async_subscribe_receiver
from homeassistant.core import HomeAssistant, callback

__all__ = ['DOMAIN', 'InfraredCommand', 'InfraredEmitterConsumerEntity', 'InfraredEmitterEntity', 'InfraredEmitterEntityDescription', 'InfraredEntity', 'InfraredEntityDescription', 'InfraredReceivedSignal', 'InfraredReceiverConsumerEntity', 'InfraredReceiverEntity', 'InfraredReceiverEntityDescription', 'async_get_emitters', 'async_get_receivers', 'async_send_command', 'async_subscribe_receiver']

@callback
def async_get_emitters(hass: HomeAssistant) -> list[str]: ...
@callback
def async_get_receivers(hass: HomeAssistant) -> list[str]: ...
