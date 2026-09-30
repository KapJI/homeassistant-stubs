from aiothreema import ThreemaAuthError as ThreemaAuthError, ThreemaConnectionError as ThreemaConnectionError, ThreemaGatewayClient, ThreemaSendError as ThreemaSendError, derive_public_key as derive_public_key, generate_key_pair as generate_key_pair
from homeassistant.core import HomeAssistant

__all__ = ['ThreemaAPIClient', 'ThreemaAuthError', 'ThreemaConnectionError', 'ThreemaSendError', 'derive_public_key', 'generate_key_pair']

class ThreemaAPIClient(ThreemaGatewayClient):
    def __init__(self, hass: HomeAssistant, gateway_id: str, api_secret: str, private_key: str | None = None) -> None: ...
