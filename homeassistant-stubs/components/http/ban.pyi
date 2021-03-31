from datetime import datetime
from homeassistant.config import load_yaml_config_file as load_yaml_config_file
from homeassistant.const import HTTP_BAD_REQUEST as HTTP_BAD_REQUEST
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.util import yaml as yaml
from typing import Any

KEY_BANNED_IPS: str
KEY_FAILED_LOGIN_ATTEMPTS: str
KEY_LOGIN_THRESHOLD: str
NOTIFICATION_ID_BAN: str
NOTIFICATION_ID_LOGIN: str
IP_BANS_FILE: str
ATTR_BANNED_AT: str
SCHEMA_IP_BAN_ENTRY: Any

def setup_bans(hass: Any, app: Any, login_threshold: Any) -> None: ...
async def ban_middleware(request: Any, handler: Any): ...
def log_invalid_auth(func: Any): ...
async def process_wrong_login(request: Any) -> None: ...
async def process_success_login(request: Any) -> None: ...

class IpBan:
    ip_address: Any = ...
    banned_at: Any = ...
    def __init__(self, ip_ban: str, banned_at: Union[datetime, None]=...) -> None: ...

async def async_load_ip_bans_config(hass: HomeAssistant, path: str) -> list[IpBan]: ...
def update_ip_bans_config(path: str, ip_ban: IpBan) -> None: ...
