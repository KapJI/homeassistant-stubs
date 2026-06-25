from .const import CONF_DEVICE_TYPE as CONF_DEVICE_TYPE, CONF_INFRARED_ENTITY_ID as CONF_INFRARED_ENTITY_ID, CONF_INFRARED_RECEIVER_ENTITY_ID as CONF_INFRARED_RECEIVER_ENTITY_ID, DOMAIN as DOMAIN, LGDeviceType as LGDeviceType
from homeassistant.components.infrared import async_get_emitters as async_get_emitters, async_get_receivers as async_get_receivers
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.helpers.selector import EntitySelector as EntitySelector, EntitySelectorConfig as EntitySelectorConfig, SelectSelector as SelectSelector, SelectSelectorConfig as SelectSelectorConfig, SelectSelectorMode as SelectSelectorMode
from typing import Any, override

DEVICE_TYPE_NAMES: dict[LGDeviceType, str]

class LgIrConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    @override
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
