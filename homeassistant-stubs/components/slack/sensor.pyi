from .const import ATTR_SNOOZE as ATTR_SNOOZE, DOMAIN as DOMAIN, SLACK_DATA as SLACK_DATA
from .entity import SlackEntity as SlackEntity
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from slack_sdk.web.async_client import AsyncWebClient as AsyncWebClient

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class SlackSensorEntity(SlackEntity, SensorEntity):
    _client: AsyncWebClient
    _attr_native_value: Incomplete
    async def async_update(self) -> None: ...
