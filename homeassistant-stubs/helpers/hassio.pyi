from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback

@callback
def is_hassio(hass: HomeAssistant) -> bool: ...
@callback
def get_supervisor_ip() -> str | None: ...
