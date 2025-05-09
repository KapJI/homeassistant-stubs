from .const import SUBCAT_ALL as SUBCAT_ALL
from .models import PermissionLookup as PermissionLookup
from .types import CategoryType as CategoryType, SubCategoryDict as SubCategoryDict, ValueType as ValueType
from collections.abc import Callable

type LookupFunc = Callable[[PermissionLookup, SubCategoryDict, str], ValueType | None]
type SubCatLookupType = dict[str, LookupFunc]
def lookup_all(perm_lookup: PermissionLookup, lookup_dict: SubCategoryDict, object_id: str) -> ValueType: ...
def compile_policy(policy: CategoryType, subcategories: SubCatLookupType, perm_lookup: PermissionLookup) -> Callable[[str, str], bool]: ...
def _gen_dict_test_func(perm_lookup: PermissionLookup, lookup_func: LookupFunc, lookup_dict: SubCategoryDict) -> Callable[[str, str], bool | None]: ...
def test_all(policy: CategoryType, key: str) -> bool: ...
