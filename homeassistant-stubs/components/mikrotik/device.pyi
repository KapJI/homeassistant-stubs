from .const import ATTR_DEVICE_TRACKER as ATTR_DEVICE_TRACKER
from _typeshed import Incomplete
from datetime import datetime
from homeassistant.util import slugify as slugify
from typing import Any

class Device:
    _mac: Incomplete
    _params: Incomplete
    _last_seen: Incomplete
    _attrs: Incomplete
    _wireless_params: Incomplete
    def __init__(self, mac: str, params: dict[str, Any]) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def ip_address(self) -> Union[str, None]: ...
    @property
    def mac(self) -> str: ...
    @property
    def last_seen(self) -> Union[datetime, None]: ...
    @property
    def attrs(self) -> dict[str, Any]: ...
    def update(self, wireless_params: Union[dict[str, Any], None] = ..., params: Union[dict[str, Any], None] = ..., active: bool = ...) -> None: ...
