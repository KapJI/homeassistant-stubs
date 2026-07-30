import voluptuous as vol
from .const import CONF_DEVICE_TYPE as CONF_DEVICE_TYPE, CONF_HVAC_MODES as CONF_HVAC_MODES, CONF_INFRARED_ENTITY_ID as CONF_INFRARED_ENTITY_ID, CONF_INFRARED_RECEIVER_ENTITY_ID as CONF_INFRARED_RECEIVER_ENTITY_ID, DOMAIN as DOMAIN, LGDeviceType as LGDeviceType
from _typeshed import Incomplete
from homeassistant.components.climate import HVACMode as HVACMode
from homeassistant.components.infrared import async_get_emitters as async_get_emitters, async_get_receivers as async_get_receivers
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.selector import EntitySelector as EntitySelector, EntitySelectorConfig as EntitySelectorConfig, SelectSelector as SelectSelector, SelectSelectorConfig as SelectSelectorConfig, SelectSelectorMode as SelectSelectorMode
from typing import Any, override

DEVICE_TYPE_NAMES: dict[LGDeviceType, str]
_HVAC_MODE_OPTIONS: Incomplete
_DEFAULT_HVAC_MODES: Incomplete

@callback
def _infrared_entity_schema(hass: HomeAssistant, *, emitter_required: bool) -> vol.Schema: ...

class LgIrConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    def _entity_name(self, entity_id: str) -> str: ...
    async def _async_create_device_entry(self, device_type: LGDeviceType, user_input: dict[str, Any]) -> ConfigFlowResult: ...
    @override
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_tv(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_ac(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
