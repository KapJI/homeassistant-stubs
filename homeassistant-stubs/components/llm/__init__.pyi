from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.frame import ReportBehavior as ReportBehavior, report_usage as report_usage
from homeassistant.helpers.integration_platform import LazyIntegrationPlatforms as LazyIntegrationPlatforms
from homeassistant.helpers.llm import API as API, APIInstance as APIInstance, LLMContext as LLMContext, LLM_API_ASSIST as LLM_API_ASSIST, Tool as Tool, async_register_api as async_register_api, selector_serializer as selector_serializer
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.loader import async_get_issue_integration as async_get_issue_integration
from homeassistant.util.hass_dict import HassKey as HassKey
from typing import Protocol, override

_LOGGER: Incomplete
CONFIG_SCHEMA: Incomplete
TOOL_PREFIX_BREAKS_IN_HA_VERSION: str
DATA_PLATFORMS: HassKey[LazyIntegrationPlatforms[LLMToolsPlatformProtocol]]

@dataclass(slots=True)
class LLMTools:
    tools: list[Tool]
    prompt: str | None = ...

class LLMToolsPlatformProtocol(Protocol):
    @callback
    def async_get_tools(self, hass: HomeAssistant, llm_context: LLMContext, api_id: str) -> LLMTools | None: ...

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
@callback
def _process_llm_tools_platform(hass: HomeAssistant, domain: str, platform: LLMToolsPlatformProtocol) -> LLMToolsPlatformProtocol: ...
async def async_get_tools(hass: HomeAssistant, llm_context: LLMContext, api_id: str) -> LLMTools: ...
@callback
def _async_report_unprefixed_tools(hass: HomeAssistant, domain: str, tools: list[Tool]) -> None: ...

class AssistAPI(API):
    def __init__(self, hass: HomeAssistant) -> None: ...
    @override
    async def async_get_api_instance(self, llm_context: LLMContext) -> APIInstance: ...
