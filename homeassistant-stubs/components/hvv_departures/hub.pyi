from _typeshed import Incomplete
from aiohttp import ClientSession as ClientSession
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from pygti.models import InitResponse as InitResponse

type HVVConfigEntry = ConfigEntry[GTIHub]
class GTIHub:
    host: Incomplete
    username: Incomplete
    password: Incomplete
    gti: Incomplete
    def __init__(self, host: str, username: str, password: str, session: ClientSession) -> None: ...
    async def authenticate(self) -> InitResponse: ...
