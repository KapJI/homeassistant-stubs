import evohomeasync2 as evo
from .const import EVOHOME_DATA as EVOHOME_DATA
from .coordinator import EvoDataUpdateCoordinator as EvoDataUpdateCoordinator
from .entity import is_valid_zone as is_valid_zone, unique_zone_id as unique_zone_id
from _typeshed import Incomplete
from homeassistant.components.button import ButtonEntity as ButtonEntity
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

async def async_setup_platform(hass: HomeAssistant, _: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...

class EvoResetButtonBase(CoordinatorEntity[EvoDataUpdateCoordinator], ButtonEntity):
    _attr_entity_category: Incomplete
    _evo_device: evo.ControlSystem | evo.HotWater | evo.Zone
    def __init__(self, coordinator: EvoDataUpdateCoordinator, evo_device: evo.ControlSystem | evo.HotWater | evo.Zone) -> None: ...
    async def async_press(self) -> None: ...

class EvoResetSystemButton(EvoResetButtonBase):
    _evo_device: evo.ControlSystem
    _attr_unique_id: Incomplete
    _attr_name: Incomplete
    def __init__(self, coordinator: EvoDataUpdateCoordinator, evo_device: evo.ControlSystem) -> None: ...

class EvoResetDhwButton(EvoResetButtonBase):
    _evo_device: evo.HotWater
    _attr_unique_id: Incomplete
    _attr_name: Incomplete
    def __init__(self, coordinator: EvoDataUpdateCoordinator, evo_device: evo.HotWater) -> None: ...

class EvoResetZoneButton(EvoResetButtonBase):
    _evo_device: evo.Zone
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: EvoDataUpdateCoordinator, evo_device: evo.Zone) -> None: ...
    @property
    def name(self) -> str: ...
