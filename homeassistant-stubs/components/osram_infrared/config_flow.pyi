from .const import CONF_IR_EMITTER_ENTITY_ID as CONF_IR_EMITTER_ENTITY_ID, CONF_IR_RECEIVER_ENTITY_ID as CONF_IR_RECEIVER_ENTITY_ID, DOMAIN as DOMAIN
from collections.abc import Collection
from homeassistant.components.infrared import async_get_emitters as async_get_emitters, async_get_receivers as async_get_receivers
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.helpers.selector import EntitySelector as EntitySelector, EntitySelectorConfig as EntitySelectorConfig
from typing import Any, override

class OsramIrConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    def _async_get_entry_title(self, emitter_entity_id: str) -> str: ...
    def _async_validate_input(self, user_input: dict[str, Any], emitter_entity_ids: Collection[str], receiver_entity_ids: Collection[str]) -> dict[str, str]: ...
    @override
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
