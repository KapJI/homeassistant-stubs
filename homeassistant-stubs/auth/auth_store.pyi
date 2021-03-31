from . import models as models
from .const import GROUP_ID_ADMIN as GROUP_ID_ADMIN, GROUP_ID_READ_ONLY as GROUP_ID_READ_ONLY, GROUP_ID_USER as GROUP_ID_USER
from .permissions import PermissionLookup as PermissionLookup, system_policies as system_policies
from .permissions.types import PolicyType as PolicyType
from datetime import timedelta
from homeassistant.auth.const import ACCESS_TOKEN_EXPIRATION as ACCESS_TOKEN_EXPIRATION
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from typing import Any

STORAGE_VERSION: int
STORAGE_KEY: str
GROUP_NAME_ADMIN: str
GROUP_NAME_USER: str
GROUP_NAME_READ_ONLY: str

class AuthStore:
    hass: Any = ...
    def __init__(self, hass: HomeAssistant) -> None: ...
    async def async_get_groups(self) -> list[models.Group]: ...
    async def async_get_group(self, group_id: str) -> Union[models.Group, None]: ...
    async def async_get_users(self) -> list[models.User]: ...
    async def async_get_user(self, user_id: str) -> Union[models.User, None]: ...
    async def async_create_user(self, name: Union[str, None], is_owner: Union[bool, None]=..., is_active: Union[bool, None]=..., system_generated: Union[bool, None]=..., credentials: Union[models.Credentials, None]=..., group_ids: Union[list[str], None]=...) -> models.User: ...
    async def async_link_user(self, user: models.User, credentials: models.Credentials) -> None: ...
    async def async_remove_user(self, user: models.User) -> None: ...
    async def async_update_user(self, user: models.User, name: Union[str, None]=..., is_active: Union[bool, None]=..., group_ids: Union[list[str], None]=...) -> None: ...
    async def async_activate_user(self, user: models.User) -> None: ...
    async def async_deactivate_user(self, user: models.User) -> None: ...
    async def async_remove_credentials(self, credentials: models.Credentials) -> None: ...
    async def async_create_refresh_token(self, user: models.User, client_id: Union[str, None]=..., client_name: Union[str, None]=..., client_icon: Union[str, None]=..., token_type: str=..., access_token_expiration: timedelta=..., credential: Union[models.Credentials, None]=...) -> models.RefreshToken: ...
    async def async_remove_refresh_token(self, refresh_token: models.RefreshToken) -> None: ...
    async def async_get_refresh_token(self, token_id: str) -> Union[models.RefreshToken, None]: ...
    async def async_get_refresh_token_by_token(self, token: str) -> Union[models.RefreshToken, None]: ...
    def async_log_refresh_token_usage(self, refresh_token: models.RefreshToken, remote_ip: Union[str, None]=...) -> None: ...
