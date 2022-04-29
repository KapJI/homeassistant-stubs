from .deconz_device import DeconzDevice as DeconzDevice
from .gateway import DeconzGateway as DeconzGateway, get_gateway_from_config_entry as get_gateway_from_config_entry
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components.number import DOMAIN as DOMAIN, NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pydeconz.models.sensor.presence import Presence

class DeconzNumberDescriptionMixin:
    suffix: str
    update_key: str
    value_fn: Callable[[Presence], Union[float, None]]
    def __init__(self, suffix, update_key, value_fn) -> None: ...

class DeconzNumberDescription(NumberEntityDescription, DeconzNumberDescriptionMixin):
    def __init__(self, suffix, update_key, value_fn, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, name, unit_of_measurement, max_value, min_value, step) -> None: ...

ENTITY_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DeconzNumber(DeconzDevice, NumberEntity):
    TYPE: Incomplete
    _device: Presence
    entity_description: Incomplete
    _attr_name: Incomplete
    _update_keys: Incomplete
    def __init__(self, device: Presence, gateway: DeconzGateway, description: DeconzNumberDescription) -> None: ...
    def async_update_callback(self) -> None: ...
    @property
    def value(self) -> Union[float, None]: ...
    async def async_set_value(self, value: float) -> None: ...
    @property
    def unique_id(self) -> str: ...
