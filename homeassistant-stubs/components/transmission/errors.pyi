from homeassistant.exceptions import HomeAssistantError as HomeAssistantError

class AuthenticationError(HomeAssistantError): ...
class CannotConnect(HomeAssistantError): ...
class UnknownError(HomeAssistantError): ...
