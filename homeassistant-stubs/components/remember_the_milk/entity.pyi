from .const import LOGGER as LOGGER
from .storage import RememberTheMilkConfiguration as RememberTheMilkConfiguration
from _typeshed import Incomplete
from homeassistant.const import CONF_ID as CONF_ID, CONF_NAME as CONF_NAME, STATE_OK as STATE_OK
from homeassistant.core import ServiceCall as ServiceCall
from homeassistant.helpers.entity import Entity as Entity

class RememberTheMilkEntity(Entity):
    _name: Incomplete
    _api_key: Incomplete
    _shared_secret: Incomplete
    _token: Incomplete
    _rtm_config: Incomplete
    _rtm_api: Incomplete
    _token_valid: bool
    def __init__(self, name: str, api_key: str, shared_secret: str, token: str, rtm_config: RememberTheMilkConfiguration) -> None: ...
    def _check_token(self) -> bool: ...
    def create_task(self, call: ServiceCall) -> None: ...
    def complete_task(self, call: ServiceCall) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def state(self) -> str: ...
