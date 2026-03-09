from .const import UPDATE_URL as UPDATE_URL
from _typeshed import Incomplete
from aiohttp import ClientSession as ClientSession
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError

_LOGGER: Incomplete

async def update_namecheapdns(session: ClientSession, host: str, domain: str, password: str) -> bool: ...

class AuthFailed(HomeAssistantError): ...
