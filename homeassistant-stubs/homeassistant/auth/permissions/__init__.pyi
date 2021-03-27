from .const import CAT_ENTITIES as CAT_ENTITIES
from .entities import ENTITY_POLICY_SCHEMA as ENTITY_POLICY_SCHEMA, compile_entities as compile_entities
from .merge import merge_policies as merge_policies
from .models import PermissionLookup as PermissionLookup
from .types import PolicyType as PolicyType
from .util import test_all as test_all
from typing import Any

POLICY_SCHEMA: Any

class AbstractPermissions:
    def access_all_entities(self, key: str) -> bool: ...
    def check_entity(self, entity_id: str, key: str) -> bool: ...

class PolicyPermissions(AbstractPermissions):
    def __init__(self, policy: PolicyType, perm_lookup: PermissionLookup) -> None: ...
    def access_all_entities(self, key: str) -> bool: ...
    def __eq__(self, other: Any) -> bool: ...

class _OwnerPermissions(AbstractPermissions):
    def access_all_entities(self, key: str) -> bool: ...

OwnerPermissions: Any
