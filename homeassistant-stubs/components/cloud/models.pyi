import dataclasses
from _typeshed import Incomplete
from hass_nabucasa import AutoLoginController as AutoLoginController, LoginFailedReason

AUTO_LOGIN_FAILED_TRANSLATION_KEYS: Incomplete

def auto_login_failure_key(reason: LoginFailedReason | None) -> str | None: ...

@dataclasses.dataclass
class PendingAutoLogin:
    email: str
    controller: AutoLoginController | None
    failed_reason: LoginFailedReason | None = ...
    def mark_failed(self, reason: LoginFailedReason) -> None: ...
