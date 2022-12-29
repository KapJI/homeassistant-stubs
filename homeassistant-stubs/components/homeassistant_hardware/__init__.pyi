from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.typing import ConfigType as ConfigType

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
