from .const import ATTRIBUTION as ATTRIBUTION, DOMAIN as DOMAIN
from .coordinator import AmberUpdateCoordinator as AmberUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

PRICE_SPIKE_ICONS: Incomplete

class AmberPriceGridSensor(CoordinatorEntity[AmberUpdateCoordinator], BinarySensorEntity):
    _attr_attribution = ATTRIBUTION
    site_id: Incomplete
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: AmberUpdateCoordinator, description: BinarySensorEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool | None: ...

class AmberPriceSpikeBinarySensor(AmberPriceGridSensor):
    @property
    def icon(self) -> str: ...
    @property
    def is_on(self) -> bool | None: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
