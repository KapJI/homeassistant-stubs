from .const import LOGGER as LOGGER
from .storage import RememberTheMilkConfiguration as RememberTheMilkConfiguration
from _typeshed import Incomplete
from aiortm import AioRTMClient as AioRTMClient
from homeassistant.const import CONF_ID as CONF_ID, CONF_NAME as CONF_NAME, STATE_OK as STATE_OK
from homeassistant.core import ServiceCall as ServiceCall, callback as callback
from homeassistant.helpers.entity import Entity as Entity
from typing import override

class RememberTheMilkEntity(Entity):
    _name: Incomplete
    _rtm_config: Incomplete
    _client: Incomplete
    _config_entry_id: Incomplete
    _token_valid: Incomplete
    def __init__(self, *, name: str, client: AioRTMClient, config_entry_id: str, storage: RememberTheMilkConfiguration, token_valid: bool) -> None: ...
    async def create_task(self, call: ServiceCall) -> None: ...
    async def complete_task(self, call: ServiceCall) -> None: ...
    @property
    @override
    def name(self) -> str: ...
    @property
    @override
    def state(self) -> str: ...
    @callback
    def _handle_token(self, token_valid: bool) -> None: ...
