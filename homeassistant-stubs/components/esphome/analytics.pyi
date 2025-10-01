from homeassistant.components.analytics import AnalyticsInput as AnalyticsInput, AnalyticsModifications as AnalyticsModifications
from homeassistant.core import HomeAssistant as HomeAssistant

async def async_modify_analytics(hass: HomeAssistant, analytics_input: AnalyticsInput) -> AnalyticsModifications: ...
