from .coordinator import FireflyConfigEntry as FireflyConfigEntry, FireflyDataUpdateCoordinator as FireflyDataUpdateCoordinator
from .entity import FireflyAccountBaseEntity as FireflyAccountBaseEntity, FireflyBudgetBaseEntity as FireflyBudgetBaseEntity, FireflyCategoryBaseEntity as FireflyCategoryBaseEntity
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorStateClass as SensorStateClass, StateType as StateType
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pyfirefly.models import Account as Account, Budget as Budget, Category as Category

ACCOUNT_ROLE_MAPPING: Incomplete
ACCOUNT_TYPE_ICONS: Incomplete
ACCOUNT_BALANCE: str
ACCOUNT_ROLE: str
ACCOUNT_TYPE: str
CATEGORY: str
BUDGET: str

async def async_setup_entry(hass: HomeAssistant, entry: FireflyConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class FireflyAccountBalanceSensor(FireflyAccountBaseEntity, SensorEntity):
    _attr_translation_key: str
    _attr_device_class: Incomplete
    _attr_state_class: Incomplete
    _account: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    def __init__(self, coordinator: FireflyDataUpdateCoordinator, account: Account, key: str) -> None: ...
    @property
    def native_value(self) -> StateType: ...

class FireflyAccountRoleSensor(FireflyAccountBaseEntity, SensorEntity):
    _attr_translation_key: str
    _attr_entity_category: Incomplete
    _attr_entity_registry_enabled_default: bool
    _account: Incomplete
    def __init__(self, coordinator: FireflyDataUpdateCoordinator, account: Account, key: str) -> None: ...
    @property
    def native_value(self) -> StateType: ...

class FireflyAccountTypeSensor(FireflyAccountBaseEntity, SensorEntity):
    _attr_translation_key: str
    _attr_entity_category: Incomplete
    _attr_entity_registry_enabled_default: bool
    _attr_icon: Incomplete
    def __init__(self, coordinator: FireflyDataUpdateCoordinator, account: Account, key: str) -> None: ...
    @property
    def native_value(self) -> StateType: ...

class FireflyCategorySensor(FireflyCategoryBaseEntity, SensorEntity):
    _attr_translation_key: str
    _attr_device_class: Incomplete
    _attr_state_class: Incomplete
    _category: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    def __init__(self, coordinator: FireflyDataUpdateCoordinator, category: Category, key: str) -> None: ...
    @property
    def native_value(self) -> StateType: ...

class FireflyBudgetSensor(FireflyBudgetBaseEntity, SensorEntity):
    _attr_translation_key: str
    _attr_device_class: Incomplete
    _attr_state_class: Incomplete
    _budget: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    def __init__(self, coordinator: FireflyDataUpdateCoordinator, budget: Budget, key: str) -> None: ...
    @property
    def native_value(self) -> StateType: ...
