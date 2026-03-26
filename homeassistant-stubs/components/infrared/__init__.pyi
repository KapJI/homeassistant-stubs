import abc
from .const import DOMAIN as DOMAIN
from abc import abstractmethod
from homeassistant.core import Context, HomeAssistant, callback
from homeassistant.helpers.entity import EntityDescription
from homeassistant.helpers.restore_state import RestoreEntity
from infrared_protocols import Command as InfraredCommand
from typing import final

__all__ = ['DOMAIN', 'InfraredEntity', 'InfraredEntityDescription', 'async_get_emitters', 'async_send_command']

@callback
def async_get_emitters(hass: HomeAssistant) -> list[str]: ...
async def async_send_command(hass: HomeAssistant, entity_id_or_uuid: str, command: InfraredCommand, context: Context | None = None) -> None: ...

class InfraredEntityDescription(EntityDescription, frozen_or_thawed=True): ...

class InfraredEntity(RestoreEntity, metaclass=abc.ABCMeta):
    entity_description: InfraredEntityDescription
    _attr_should_poll: bool
    _attr_state: None
    __last_command_sent: str | None
    @property
    @final
    def state(self) -> str | None: ...
    @final
    async def async_send_command_internal(self, command: InfraredCommand) -> None: ...
    @final
    async def async_internal_added_to_hass(self) -> None: ...
    @abstractmethod
    async def async_send_command(self, command: InfraredCommand) -> None: ...
