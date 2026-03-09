from .const import AITaskEntityFeature as AITaskEntityFeature, DOMAIN as DOMAIN
from .entity import AITaskEntity as AITaskEntity
from .task import GenDataTask as GenDataTask, GenDataTaskResult as GenDataTaskResult, GenImageTask as GenImageTask, GenImageTaskResult as GenImageTaskResult, async_generate_data as async_generate_data, async_generate_image as async_generate_image
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers import storage
from homeassistant.helpers.typing import UndefinedType

__all__ = ['DOMAIN', 'AITaskEntity', 'AITaskEntityFeature', 'GenDataTask', 'GenDataTaskResult', 'GenImageTask', 'GenImageTaskResult', 'async_generate_data', 'async_generate_image']

class AITaskPreferences:
    KEYS: Incomplete
    gen_data_entity_id: str | None
    gen_image_entity_id: str | None
    _store: storage.Store[dict[str, str | None]]
    def __init__(self, hass: HomeAssistant) -> None: ...
    async def async_load(self) -> None: ...
    @callback
    def async_set_preferences(self, *, gen_data_entity_id: str | None | UndefinedType = ..., gen_image_entity_id: str | None | UndefinedType = ...) -> None: ...
    @callback
    def as_dict(self) -> dict[str, str | None]: ...
