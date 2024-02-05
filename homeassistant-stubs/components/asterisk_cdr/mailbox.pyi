from _typeshed import Incomplete
from homeassistant.components.asterisk_mbox import SIGNAL_CDR_UPDATE as SIGNAL_CDR_UPDATE
from homeassistant.components.mailbox import Mailbox as Mailbox
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

MAILBOX_NAME: str

async def async_get_handler(hass: HomeAssistant, config: ConfigType, discovery_info: DiscoveryInfoType | None = None) -> Mailbox: ...

class AsteriskCDR(Mailbox):
    cdr: Incomplete
    def __init__(self, hass: HomeAssistant, name: str) -> None: ...
    def _update_callback(self, msg: list[dict[str, Any]]) -> Any: ...
    def _build_message(self) -> None: ...
    async def async_get_messages(self) -> list[dict[str, Any]]: ...
