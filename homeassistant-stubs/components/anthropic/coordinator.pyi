import anthropic
from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_API_KEY as CONF_API_KEY
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.httpx_client import get_async_client as get_async_client
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

UPDATE_INTERVAL_CONNECTED: Incomplete
UPDATE_INTERVAL_DISCONNECTED: Incomplete
type AnthropicConfigEntry = ConfigEntry[AnthropicCoordinator]
_model_short_form: Incomplete

@callback
def model_alias(model_id: str) -> str: ...

class AnthropicCoordinator(DataUpdateCoordinator[list[anthropic.types.ModelInfo]]):
    client: anthropic.AsyncAnthropic
    def __init__(self, hass: HomeAssistant, config_entry: AnthropicConfigEntry) -> None: ...
    update_interval: Incomplete
    @callback
    def async_set_updated_data(self, data: list[anthropic.types.ModelInfo]) -> None: ...
    async def async_update_data(self) -> list[anthropic.types.ModelInfo]: ...
    last_update_success: bool
    def mark_connection_error(self) -> None: ...
    @callback
    def get_model_info(self, model_id: str) -> tuple[anthropic.types.ModelInfo, bool]: ...
