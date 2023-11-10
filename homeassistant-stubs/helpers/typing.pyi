import homeassistant
import homeassistant.core
from _typeshed import Incomplete
from enum import Enum
from typing import Any, Generic, TypeVar

_DataT = TypeVar('_DataT')
GPSType = tuple[float, float]
ConfigType = dict[str, Any]
ContextType = homeassistant.core.Context
DiscoveryInfoType = dict[str, Any]
ServiceDataType = dict[str, Any]
StateType: Incomplete
TemplateVarsType: Incomplete
QueryType = Any

class UndefinedType(Enum):
    _singleton: int

UNDEFINED: Incomplete
HomeAssistantType = homeassistant.core.HomeAssistant
ServiceCallType = homeassistant.core.ServiceCall

class EventType(homeassistant.core.Event, Generic[_DataT]):
    data: _DataT
