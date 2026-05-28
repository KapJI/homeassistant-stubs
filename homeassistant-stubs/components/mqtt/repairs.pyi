from .config_flow import try_connection as try_connection
from .const import DEFAULT_PORT as DEFAULT_PORT, DOMAIN as DOMAIN, PROTOCOL_5 as PROTOCOL_5
from _typeshed import Incomplete
from homeassistant.components.repairs import RepairsFlow as RepairsFlow, RepairsFlowResult as RepairsFlowResult
from homeassistant.const import CONF_PORT as CONF_PORT, CONF_PROTOCOL as CONF_PROTOCOL
from homeassistant.core import HomeAssistant as HomeAssistant

URL_MQTT_BROKER_CONFIGURATION: str

class MQTTDeviceEntryMigration(RepairsFlow):
    entry_id: Incomplete
    subentry_id: Incomplete
    name: Incomplete
    def __init__(self, entry_id: str, subentry_id: str, name: str) -> None: ...
    async def async_step_init(self, user_input: dict[str, str] | None = None) -> RepairsFlowResult: ...
    async def async_step_confirm(self, user_input: dict[str, str] | None = None) -> RepairsFlowResult: ...

class MQTTProtocolV5Migration(RepairsFlow):
    entry_id: Incomplete
    broker: Incomplete
    protocol: Incomplete
    def __init__(self, entry_id: str, broker: str, protocol: str) -> None: ...
    async def async_step_init(self, user_input: dict[str, str] | None = None) -> RepairsFlowResult: ...
    async def async_step_confirm(self, user_input: dict[str, str] | None = None) -> RepairsFlowResult: ...

async def async_create_fix_flow(hass: HomeAssistant, issue_id: str, data: dict[str, str | int | float | None] | None) -> RepairsFlow: ...
