import probatio
from ..const import CONF_PAYLOAD_LENGTH as CONF_PAYLOAD_LENGTH, CONF_VALUE as CONF_VALUE, SelectConf as SelectConf
from ..dpt import HaDptClass as HaDptClass, get_supported_dpts as get_supported_dpts
from ..validation import ga_validator as ga_validator, maybe_ga_validator as maybe_ga_validator, sync_state_validator as sync_state_validator
from .const import CONF_DPT as CONF_DPT, CONF_GA_PASSIVE as CONF_GA_PASSIVE, CONF_GA_STATE as CONF_GA_STATE, CONF_GA_WRITE as CONF_GA_WRITE
from .util import dpt_string_to_dict as dpt_string_to_dict
from _typeshed import Incomplete
from collections.abc import Iterable
from enum import Enum
from homeassistant.const import CONF_PAYLOAD as CONF_PAYLOAD
from typing import Any, override

class AllSerializeFirst(probatio.All): ...

class KNXSelectorBase:
    schema: probatio.Schema | probatio.Any | probatio.All | GroupSelectSchema
    selector_type: str
    serialize_subschema: bool
    def __call__(self, data: Any) -> Any: ...
    def serialize(self) -> dict[str, Any]: ...

class KNXSectionFlat(KNXSelectorBase):
    selector_type: str
    schema: Incomplete
    collapsible: Incomplete
    def __init__(self, collapsible: bool = False) -> None: ...
    @override
    def serialize(self) -> dict[str, Any]: ...

class KNXSection(KNXSelectorBase):
    selector_type: str
    serialize_subschema: bool
    collapsible: Incomplete
    schema: Incomplete
    def __init__(self, schema: dict[str | probatio.Marker, probatio.Schemable], collapsible: bool = True) -> None: ...
    @override
    def serialize(self) -> dict[str, Any]: ...

class GroupSelectOption(KNXSelectorBase):
    selector_type: str
    serialize_subschema: bool
    translation_key: Incomplete
    schema: Incomplete
    def __init__(self, schema: probatio.Schemable, translation_key: str) -> None: ...
    @override
    def serialize(self) -> dict[str, Any]: ...

def _has_extra_keys_error(exc: probatio.Invalid) -> bool: ...

class GroupSelectSchema:
    validators: Incomplete
    msg: Incomplete
    _compiled: Incomplete
    def __init__(self, *options: probatio.Schemable, msg: str | None = None) -> None: ...
    def __call__(self, data: Any) -> Any: ...

class GroupSelect(KNXSelectorBase):
    selector_type: str
    serialize_subschema: bool
    collapsible: Incomplete
    schema: Incomplete
    def __init__(self, *options: GroupSelectOption, collapsible: bool = True) -> None: ...
    @override
    def serialize(self) -> dict[str, Any]: ...

class GASelector(KNXSelectorBase):
    selector_type: str
    write: Incomplete
    state: Incomplete
    passive: Incomplete
    write_required: Incomplete
    state_required: Incomplete
    dpt: Incomplete
    dpt_required: Incomplete
    valid_dpt: Incomplete
    schema: Incomplete
    def __init__(self, write: bool = True, state: bool = True, passive: bool = True, write_required: bool = False, state_required: bool = False, dpt: type[Enum] | list[HaDptClass] | None = None, dpt_required: bool = True, valid_dpt: str | Iterable[str] | None = None) -> None: ...
    @override
    def serialize(self) -> dict[str, Any]: ...
    def build_schema(self) -> probatio.Schema: ...
    def _add_group_addresses(self, schema: dict[probatio.Marker, Any]) -> None: ...
    def _add_passive(self, schema: dict[probatio.Marker, Any]) -> None: ...
    def _add_dpt(self, schema: dict[probatio.Marker, Any]) -> None: ...

class SyncStateSelector(KNXSelectorBase):
    schema: Incomplete
    selector_type: str
    allow_false: Incomplete
    def __init__(self, allow_false: bool = False) -> None: ...
    @override
    def serialize(self) -> dict[str, Any]: ...
    @override
    def __call__(self, data: Any) -> Any: ...

class KnxPayloadSelector(KNXSelectorBase):
    schema: Incomplete
    selector_type: str
    ga_path: Incomplete
    def __init__(self, ga_path: str) -> None: ...
    @override
    def serialize(self) -> dict[str, Any]: ...
    @override
    def __call__(self, data: Any) -> Any: ...

class KnxSelectOptionsSelector(KNXSelectorBase):
    selector_type: str
    ga_path: Incomplete
    _payload_selector: Incomplete
    schema: Incomplete
    def __init__(self, ga_path: str) -> None: ...
    @override
    def serialize(self) -> dict[str, Any]: ...
    def _validate_option(self, data: Any) -> dict[str, Any]: ...
