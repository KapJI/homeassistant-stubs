import logging
from .const import DOMAIN as DOMAIN
from homeassistant.helpers import config_entry_oauth2_flow as config_entry_oauth2_flow
from typing import Any

class OAuth2FlowHandler(config_entry_oauth2_flow.AbstractOAuth2FlowHandler):
    DOMAIN: Any
    @property
    def logger(self) -> logging.Logger: ...
    @property
    def extra_authorize_data(self) -> dict: ...
