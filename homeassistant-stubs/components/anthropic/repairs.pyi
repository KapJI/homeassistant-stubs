from . import AnthropicConfigEntry as AnthropicConfigEntry
from .config_flow import get_model_list as get_model_list
from .const import CONF_CHAT_MODEL as CONF_CHAT_MODEL, DEPRECATED_MODELS as DEPRECATED_MODELS, DOMAIN as DOMAIN
from collections.abc import Iterator
from homeassistant import data_entry_flow as data_entry_flow
from homeassistant.components.repairs import RepairsFlow as RepairsFlow
from homeassistant.config_entries import ConfigEntryState as ConfigEntryState, ConfigSubentry as ConfigSubentry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.selector import SelectOptionDict as SelectOptionDict, SelectSelector as SelectSelector, SelectSelectorConfig as SelectSelectorConfig

class ModelDeprecatedRepairFlow(RepairsFlow):
    _subentry_iter: Iterator[tuple[str, str]] | None
    _current_entry_id: str | None
    _current_subentry_id: str | None
    _model_list_cache: dict[str, list[SelectOptionDict]] | None
    def __init__(self) -> None: ...
    async def async_step_init(self, user_input: dict[str, str]) -> data_entry_flow.FlowResult: ...
    def _iter_deprecated_subentries(self) -> Iterator[tuple[str, str]]: ...
    async def _async_next_target(self) -> tuple[AnthropicConfigEntry, ConfigSubentry, str] | None: ...
    def _async_update_current_subentry(self, user_input: dict[str, str]) -> None: ...
    def _format_subentry_type(self, subentry_type: str) -> str: ...

async def async_create_fix_flow(hass: HomeAssistant, issue_id: str, data: dict[str, str | int | float | None] | None) -> RepairsFlow: ...
