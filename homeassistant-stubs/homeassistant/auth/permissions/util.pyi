from .const import SUBCAT_ALL as SUBCAT_ALL
from .models import PermissionLookup as PermissionLookup
from .types import CategoryType as CategoryType, SubCategoryDict as SubCategoryDict, ValueType as ValueType
from typing import Callable, Dict, Optional

LookupFunc = Callable[[PermissionLookup, SubCategoryDict, str], Optional[ValueType]]
SubCatLookupType = Dict[str, LookupFunc]

def lookup_all(perm_lookup: PermissionLookup, lookup_dict: SubCategoryDict, object_id: str) -> ValueType: ...
def compile_policy(policy: CategoryType, subcategories: SubCatLookupType, perm_lookup: PermissionLookup) -> Callable[[str, str], bool]: ...
def test_all(policy: CategoryType, key: str) -> bool: ...
