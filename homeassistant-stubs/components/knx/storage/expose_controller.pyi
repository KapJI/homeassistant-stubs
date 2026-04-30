from ..expose import KnxExposeEntity as KnxExposeEntity, KnxExposeOptions as KnxExposeOptions
from .entity_store_validation import validate_config_store_data as validate_config_store_data
from .knx_selector import GASelector as GASelector
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import selector as selector
from typing import Any, NotRequired, TypedDict
from xknx import XKNX as XKNX

class KNXExposeStoreOptionModel(TypedDict):
    ga: dict[str, Any]
    attribute: NotRequired[str]
    cooldown: NotRequired[float]
    default: NotRequired[Any]
    periodic_send: NotRequired[float]
    respond_to_read: NotRequired[bool]
    value_template: NotRequired[str]

class KNXExposeStoreConfigModel(TypedDict):
    options: list[KNXExposeStoreOptionModel]
    notes: NotRequired[str]
type KNXExposeStoreModel = dict[str, KNXExposeStoreConfigModel]

class KNXExposeDataModel(TypedDict):
    entity_id: str
    data: KNXExposeStoreConfigModel

def validate_expose_template_no_coerce(value: str) -> str: ...

EXPOSE_OPTION_SCHEMA: Incomplete
EXPOSE_CONFIG_SCHEMA: Incomplete

def validate_expose_data(data: dict) -> KNXExposeDataModel: ...
def _store_to_expose_option(hass: HomeAssistant, config: KNXExposeStoreOptionModel) -> KnxExposeOptions: ...

class ExposeController:
    _entity_exposes: dict[str, KnxExposeEntity]
    def __init__(self) -> None: ...
    @callback
    def stop(self) -> None: ...
    @callback
    def start(self, hass: HomeAssistant, xknx: XKNX, config: KNXExposeStoreModel) -> None: ...
    @callback
    def update_entity_expose(self, hass: HomeAssistant, xknx: XKNX, entity_id: str, expose_config: KNXExposeStoreConfigModel) -> None: ...
    @callback
    def remove_entity_expose(self, entity_id: str) -> None: ...
