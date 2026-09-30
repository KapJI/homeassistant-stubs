import anthropic
from . import AnthropicConfigEntry as AnthropicConfigEntry
from .const import CONF_CHAT_MODEL as CONF_CHAT_MODEL, CONF_THINKING_EFFORT as CONF_THINKING_EFFORT, DOMAIN as DOMAIN, THINKING_EFFORT_NONE_SUPPORTED_MODELS as THINKING_EFFORT_NONE_SUPPORTED_MODELS
from .coordinator import model_alias as model_alias
from collections.abc import Iterator
from homeassistant.components.repairs import RepairsFlow as RepairsFlow, RepairsFlowResult as RepairsFlowResult
from homeassistant.config_entries import ConfigEntryState as ConfigEntryState, ConfigSubentry as ConfigSubentry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.selector import SelectOptionDict as SelectOptionDict, SelectSelector as SelectSelector, SelectSelectorConfig as SelectSelectorConfig

class ModelDeprecatedRepairFlow(RepairsFlow):
    _subentry_iter: Iterator[tuple[str, str]] | None
    _current_entry_id: str | None
    _current_subentry_id: str | None
    _model_list_cache: dict[str, list[anthropic.types.ModelInfo]] | None
    def __init__(self) -> None: ...
    async def async_step_init(self, user_input: dict[str, str] | None) -> RepairsFlowResult: ...
    def _iter_deprecated_subentries(self) -> Iterator[tuple[str, str]]: ...
    async def _async_next_target(self) -> tuple[AnthropicConfigEntry, ConfigSubentry, str] | None: ...
    async def _async_update_current_subentry(self, user_input: dict[str, str]) -> None: ...
    def _format_subentry_type(self, subentry_type: str) -> str: ...

async def async_create_fix_flow(hass: HomeAssistant, issue_id: str, data: dict[str, str | int | float | None] | None) -> RepairsFlow: ...
