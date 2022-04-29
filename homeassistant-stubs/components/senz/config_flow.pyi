import logging
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.helpers import config_entry_oauth2_flow as config_entry_oauth2_flow

class OAuth2FlowHandler(config_entry_oauth2_flow.AbstractOAuth2FlowHandler):
    DOMAIN: Incomplete
    @property
    def logger(self) -> logging.Logger: ...
    @property
    def extra_authorize_data(self) -> dict: ...
