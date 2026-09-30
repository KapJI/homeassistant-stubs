import probatio
from .const import CONF_HVAC_MODES as CONF_HVAC_MODES, CONF_INFRARED_EMITTER_ENTITY_ID as CONF_INFRARED_EMITTER_ENTITY_ID, CONF_INFRARED_RECEIVER_ENTITY_ID as CONF_INFRARED_RECEIVER_ENTITY_ID, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.climate import HVACMode as HVACMode
from homeassistant.components.infrared import async_get_emitters as async_get_emitters, async_get_receivers as async_get_receivers
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.selector import EntitySelector as EntitySelector, EntitySelectorConfig as EntitySelectorConfig, SelectSelector as SelectSelector, SelectSelectorConfig as SelectSelectorConfig, SelectSelectorMode as SelectSelectorMode
from typing import Any, override

_HVAC_MODE_OPTIONS: Incomplete
_DEFAULT_HVAC_MODES: Incomplete

@callback
def _user_schema(hass: HomeAssistant) -> probatio.Schema: ...

class GreeIrConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    def _entity_name(self, entity_id: str) -> str: ...
    @override
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
