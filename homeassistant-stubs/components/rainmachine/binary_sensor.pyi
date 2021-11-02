from . import RainMachineEntity as RainMachineEntity
from .const import DATA_CONTROLLER as DATA_CONTROLLER, DATA_COORDINATOR as DATA_COORDINATOR, DATA_PROVISION_SETTINGS as DATA_PROVISION_SETTINGS, DATA_RESTRICTIONS_CURRENT as DATA_RESTRICTIONS_CURRENT, DATA_RESTRICTIONS_UNIVERSAL as DATA_RESTRICTIONS_UNIVERSAL, DOMAIN as DOMAIN
from .model import RainMachineSensorDescriptionMixin as RainMachineSensorDescriptionMixin
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ENTITY_CATEGORY_DIAGNOSTIC as ENTITY_CATEGORY_DIAGNOSTIC
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

TYPE_FLOW_SENSOR: str
TYPE_FREEZE: str
TYPE_FREEZE_PROTECTION: str
TYPE_HOT_DAYS: str
TYPE_HOURLY: str
TYPE_MONTH: str
TYPE_RAINDELAY: str
TYPE_RAINSENSOR: str
TYPE_WEEKDAY: str

class RainMachineBinarySensorDescription(BinarySensorEntityDescription, RainMachineSensorDescriptionMixin): ...

BINARY_SENSOR_DESCRIPTIONS: Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class CurrentRestrictionsBinarySensor(RainMachineEntity, BinarySensorEntity):
    _attr_is_on: Any
    def update_from_latest_data(self) -> None: ...

class ProvisionSettingsBinarySensor(RainMachineEntity, BinarySensorEntity):
    _attr_is_on: Any
    def update_from_latest_data(self) -> None: ...

class UniversalRestrictionsBinarySensor(RainMachineEntity, BinarySensorEntity):
    _attr_is_on: Any
    def update_from_latest_data(self) -> None: ...
