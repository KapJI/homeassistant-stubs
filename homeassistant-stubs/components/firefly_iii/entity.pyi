from .const import DOMAIN as DOMAIN, MANUFACTURER as MANUFACTURER, NAME as NAME
from .coordinator import FireflyDataUpdateCoordinator as FireflyDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.const import CONF_URL as CONF_URL
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from pyfirefly.models import Account as Account, Budget as Budget, Category as Category

class FireflyBaseEntity(CoordinatorEntity[FireflyDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    _attr_device_info: Incomplete
    def __init__(self, coordinator: FireflyDataUpdateCoordinator) -> None: ...

class FireflyAccountBaseEntity(FireflyBaseEntity):
    _account: Incomplete
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: FireflyDataUpdateCoordinator, account: Account, key: str) -> None: ...

class FireflyCategoryBaseEntity(FireflyBaseEntity):
    _category: Incomplete
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: FireflyDataUpdateCoordinator, category: Category, key: str) -> None: ...

class FireflyBudgetBaseEntity(FireflyBaseEntity):
    _budget: Incomplete
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: FireflyDataUpdateCoordinator, budget: Budget, key: str) -> None: ...
