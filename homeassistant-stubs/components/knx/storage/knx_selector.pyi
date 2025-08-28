import voluptuous as vol
from ..validation import ga_validator as ga_validator, maybe_ga_validator as maybe_ga_validator, sync_state_validator as sync_state_validator
from .const import CONF_DPT as CONF_DPT, CONF_GA_PASSIVE as CONF_GA_PASSIVE, CONF_GA_STATE as CONF_GA_STATE, CONF_GA_WRITE as CONF_GA_WRITE
from .util import dpt_string_to_dict as dpt_string_to_dict
from _typeshed import Incomplete
from collections.abc import Hashable, Iterable
from enum import Enum
from typing import Any

class AllSerializeFirst(vol.All): ...

class KNXSelectorBase:
    schema: vol.Schema | vol.Any | vol.All
    selector_type: str
    serialize_subschema: bool
    def __call__(self, data: Any) -> Any: ...
    def serialize(self) -> dict[str, Any]: ...

class KNXSectionFlat(KNXSelectorBase):
    selector_type: str
    schema: Incomplete
    collapsible: Incomplete
    def __init__(self, collapsible: bool = False) -> None: ...
    def serialize(self) -> dict[str, Any]: ...

class KNXSection(KNXSelectorBase):
    selector_type: str
    serialize_subschema: bool
    collapsible: Incomplete
    schema: Incomplete
    def __init__(self, schema: dict[str | vol.Marker, vol.Schemable], collapsible: bool = True) -> None: ...
    def serialize(self) -> dict[str, Any]: ...

class GroupSelectOption(KNXSelectorBase):
    selector_type: str
    serialize_subschema: bool
    translation_key: Incomplete
    schema: Incomplete
    def __init__(self, schema: vol.Schemable, translation_key: str) -> None: ...
    def serialize(self) -> dict[str, Any]: ...

class GroupSelectSchema(vol.Any):
    def _exec(self, funcs: Iterable, v: Any, path: list[Hashable] | None = None) -> Any: ...

class GroupSelect(KNXSelectorBase):
    selector_type: str
    serialize_subschema: bool
    collapsible: Incomplete
    schema: Incomplete
    def __init__(self, *options: GroupSelectOption, collapsible: bool = True) -> None: ...
    def serialize(self) -> dict[str, Any]: ...

class GASelector(KNXSelectorBase):
    selector_type: str
    write: Incomplete
    state: Incomplete
    passive: Incomplete
    write_required: Incomplete
    state_required: Incomplete
    dpt: Incomplete
    valid_dpt: Incomplete
    schema: Incomplete
    def __init__(self, write: bool = True, state: bool = True, passive: bool = True, write_required: bool = False, state_required: bool = False, dpt: type[Enum] | None = None, valid_dpt: str | Iterable[str] | None = None) -> None: ...
    def serialize(self) -> dict[str, Any]: ...
    def build_schema(self) -> vol.Schema: ...
    def _add_group_addresses(self, schema: dict[vol.Marker, Any]) -> None: ...
    def _add_passive(self, schema: dict[vol.Marker, Any]) -> None: ...
    def _add_dpt(self, schema: dict[vol.Marker, Any]) -> None: ...

class SyncStateSelector(KNXSelectorBase):
    schema: Incomplete
    selector_type: str
    allow_false: Incomplete
    def __init__(self, allow_false: bool = False) -> None: ...
    def serialize(self) -> dict[str, Any]: ...
    def __call__(self, data: Any) -> Any: ...
