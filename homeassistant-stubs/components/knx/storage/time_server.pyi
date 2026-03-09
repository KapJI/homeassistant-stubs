from ..expose import KnxExposeTime as KnxExposeTime, create_time_server_exposures as create_time_server_exposures
from .entity_store_validation import validate_config_store_data as validate_config_store_data
from .knx_selector import GASelector as GASelector
from _typeshed import Incomplete
from typing import Any, TypedDict
from xknx import XKNX as XKNX

class KNXTimeServerStoreModel(TypedDict, total=False):
    time: dict[str, Any] | None
    date: dict[str, Any] | None
    datetime: dict[str, Any] | None

TIME_SERVER_CONFIG_SCHEMA: Incomplete

def validate_time_server_data(time_server_data: dict) -> KNXTimeServerStoreModel: ...

class TimeServerController:
    time_exposes: list[KnxExposeTime]
    def __init__(self) -> None: ...
    def stop(self) -> None: ...
    def start(self, xknx: XKNX, config: KNXTimeServerStoreModel) -> None: ...
