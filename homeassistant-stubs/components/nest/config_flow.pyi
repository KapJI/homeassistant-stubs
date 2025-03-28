import logging
from . import api as api
from .const import CONF_CLOUD_PROJECT_ID as CONF_CLOUD_PROJECT_ID, CONF_PROJECT_ID as CONF_PROJECT_ID, CONF_SUBSCRIBER_ID_IMPORTED as CONF_SUBSCRIBER_ID_IMPORTED, CONF_SUBSCRIPTION_NAME as CONF_SUBSCRIPTION_NAME, CONF_TOPIC_NAME as CONF_TOPIC_NAME, DATA_SDM as DATA_SDM, DOMAIN as DOMAIN, OAUTH2_AUTHORIZE as OAUTH2_AUTHORIZE, SDM_SCOPES as SDM_SCOPES
from _typeshed import Incomplete
from collections.abc import Iterable, Mapping
from google_nest_sdm.admin_client import AdminClient as AdminClient, EligibleSubscriptions as EligibleSubscriptions, EligibleTopics as EligibleTopics
from google_nest_sdm.structure import Structure as Structure
from homeassistant.config_entries import ConfigFlowResult as ConfigFlowResult, SOURCE_REAUTH as SOURCE_REAUTH
from homeassistant.helpers import config_entry_oauth2_flow as config_entry_oauth2_flow
from homeassistant.helpers.selector import SelectSelector as SelectSelector, SelectSelectorConfig as SelectSelectorConfig, SelectSelectorMode as SelectSelectorMode
from homeassistant.util import get_random_string as get_random_string
from typing import Any

DATA_FLOW_IMPL: str
TOPIC_FORMAT: str
SUBSCRIPTION_FORMAT: str
RAND_LENGTH: int
MORE_INFO_URL: str
CLOUD_CONSOLE_URL: str
SDM_API_URL: str
PUBSUB_API_URL: str
DEVICE_ACCESS_CONSOLE_URL: str
DEVICE_ACCESS_CONSOLE_EDIT_URL: str
CREATE_NEW_TOPIC_KEY: str
CREATE_NEW_SUBSCRIPTION_KEY: str
_LOGGER: Incomplete

def _generate_subscription_id(cloud_project_id: str) -> str: ...
def _generate_topic_id(cloud_project_id: str) -> str: ...
def generate_config_title(structures: Iterable[Structure]) -> str | None: ...

class NestFlowHandler(config_entry_oauth2_flow.AbstractOAuth2FlowHandler, domain=DOMAIN):
    DOMAIN = DOMAIN
    VERSION: int
    _data: dict[str, Any]
    _structure_config_title: str | None
    _admin_client: AdminClient | None
    _eligible_topics: EligibleTopics | None
    _eligible_subscriptions: EligibleSubscriptions | None
    def __init__(self) -> None: ...
    @property
    def logger(self) -> logging.Logger: ...
    @property
    def extra_authorize_data(self) -> dict[str, str]: ...
    async def async_generate_authorize_url(self) -> str: ...
    async def async_oauth_create_entry(self, data: dict[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_create_cloud_project(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_cloud_project(self, user_input: dict | None = None) -> ConfigFlowResult: ...
    async def async_step_device_project(self, user_input: dict | None = None) -> ConfigFlowResult: ...
    async def async_step_pubsub_topic(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_pubsub_topic_confirm(self, user_input: dict | None = None) -> ConfigFlowResult: ...
    async def async_step_pubsub_subscription(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def _async_finish(self) -> ConfigFlowResult: ...
