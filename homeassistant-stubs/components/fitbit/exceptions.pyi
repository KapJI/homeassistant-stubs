from homeassistant.exceptions import HomeAssistantError as HomeAssistantError

class FitbitApiException(HomeAssistantError): ...
class FitbitAuthException(FitbitApiException): ...
