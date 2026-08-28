from _typeshed import Incomplete
from hass_nabucasa import LoginFailedReason

AUTO_LOGIN_FAILED_TRANSLATION_KEYS: Incomplete

def auto_login_failure_key(reason: LoginFailedReason | None) -> str | None: ...
