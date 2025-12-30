from aiohttp import ClientSession as ClientSession
from homeassistant.helpers.typing import UNDEFINED as UNDEFINED, UndefinedType as UndefinedType

UPDATE_URL: str

async def update_duckdns(session: ClientSession, domain: str, token: str, *, txt: str | None | UndefinedType = ..., clear: bool = False) -> bool: ...
