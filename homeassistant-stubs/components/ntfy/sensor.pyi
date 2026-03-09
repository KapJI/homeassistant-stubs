from .coordinator import NtfyConfigEntry as NtfyConfigEntry, NtfyDataUpdateCoordinator as NtfyDataUpdateCoordinator
from .entity import NtfyCommonBaseEntity as NtfyCommonBaseEntity
from aiontfy import Account as NtfyAccount
from collections.abc import Callable as Callable
from dataclasses import dataclass
from enum import StrEnum
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory, UnitOfInformation as UnitOfInformation, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType

PARALLEL_UPDATES: int

@dataclass(kw_only=True, frozen=True)
class NtfySensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[NtfyAccount], StateType]

class NtfySensor(StrEnum):
    MESSAGES = 'messages'
    MESSAGES_REMAINING = 'messages_remaining'
    MESSAGES_LIMIT = 'messages_limit'
    MESSAGES_EXPIRY_DURATION = 'messages_expiry_duration'
    EMAILS = 'emails'
    EMAILS_REMAINING = 'emails_remaining'
    EMAILS_LIMIT = 'emails_limit'
    CALLS = 'calls'
    CALLS_REMAINING = 'calls_remaining'
    CALLS_LIMIT = 'calls_limit'
    RESERVATIONS = 'reservations'
    RESERVATIONS_REMAINING = 'reservations_remaining'
    RESERVATIONS_LIMIT = 'reservations_limit'
    ATTACHMENT_TOTAL_SIZE = 'attachment_total_size'
    ATTACHMENT_TOTAL_SIZE_REMAINING = 'attachment_total_size_remaining'
    ATTACHMENT_TOTAL_SIZE_LIMIT = 'attachment_total_size_limit'
    ATTACHMENT_EXPIRY_DURATION = 'attachment_expiry_duration'
    ATTACHMENT_BANDWIDTH = 'attachment_bandwidth'
    ATTACHMENT_FILE_SIZE = 'attachment_file_size'
    TIER = 'tier'

SENSOR_DESCRIPTIONS: tuple[NtfySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: NtfyConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class NtfySensorEntity(NtfyCommonBaseEntity, SensorEntity):
    entity_description: NtfySensorEntityDescription
    coordinator: NtfyDataUpdateCoordinator
    @property
    def native_value(self) -> StateType: ...
