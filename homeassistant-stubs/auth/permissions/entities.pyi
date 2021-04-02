from .const import POLICY_CONTROL as POLICY_CONTROL, POLICY_EDIT as POLICY_EDIT, POLICY_READ as POLICY_READ, SUBCAT_ALL as SUBCAT_ALL
from .models import PermissionLookup as PermissionLookup
from .types import CategoryType as CategoryType, SubCategoryDict as SubCategoryDict, ValueType as ValueType
from .util import SubCatLookupType as SubCatLookupType, compile_policy as compile_policy, lookup_all as lookup_all
from typing import Any, Callable

SINGLE_ENTITY_SCHEMA: Any
ENTITY_DOMAINS: str
ENTITY_AREAS: str
ENTITY_DEVICE_IDS: str
ENTITY_ENTITY_IDS: str
ENTITY_VALUES_SCHEMA: Any
ENTITY_POLICY_SCHEMA: Any

def _lookup_domain(perm_lookup: PermissionLookup, domains_dict: SubCategoryDict, entity_id: str) -> Union[ValueType, None]: ...
def _lookup_area(perm_lookup: PermissionLookup, area_dict: SubCategoryDict, entity_id: str) -> Union[ValueType, None]: ...
def _lookup_device(perm_lookup: PermissionLookup, devices_dict: SubCategoryDict, entity_id: str) -> Union[ValueType, None]: ...
def _lookup_entity_id(perm_lookup: PermissionLookup, entities_dict: SubCategoryDict, entity_id: str) -> Union[ValueType, None]: ...
def compile_entities(policy: CategoryType, perm_lookup: PermissionLookup) -> Callable[[str, str], bool]: ...
