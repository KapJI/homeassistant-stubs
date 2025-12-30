import voluptuous as vol
from _typeshed import Incomplete
from collections.abc import Mapping
from enum import Enum
from typing import Any, Never

type GPSType = tuple[float, float]
type ConfigType = dict[str, Any]
type DiscoveryInfoType = dict[str, Any]
type ServiceDataType = dict[str, Any]
type StateType = str | int | float | None
type TemplateVarsType = Mapping[str, Any] | None
type NoEventData = Mapping[str, Never]
type VolSchemaType = vol.Schema | vol.All | vol.Any
type VolDictType = dict[str | vol.Marker, Any]
type QueryType = Any
class UndefinedType(Enum):
    _singleton = 0

UNDEFINED: Incomplete
