import asyncio
from .models import EntityUsageDataCache as EntityUsageDataCache, EntityUsagePredictions as EntityUsagePredictions
from homeassistant.util.hass_dict import HassKey as HassKey

DOMAIN: str
DATA_CACHE: HassKey[dict[str, asyncio.Task[EntityUsagePredictions] | EntityUsageDataCache]]
