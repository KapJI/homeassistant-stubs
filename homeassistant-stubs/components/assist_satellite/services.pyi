from .const import AssistSatelliteEntityFeature as AssistSatelliteEntityFeature, DATA_COMPONENT as DATA_COMPONENT, DOMAIN as DOMAIN
from .entity import AssistSatelliteEntity as AssistSatelliteEntity
from _typeshed import Incomplete
from homeassistant.auth.permissions.const import CAT_ENTITIES as CAT_ENTITIES, POLICY_CONTROL as POLICY_CONTROL
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, SupportsResponse as SupportsResponse, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, Unauthorized as Unauthorized, UnknownUser as UnknownUser

def has_no_punctuation(value: list[str]) -> list[str]: ...
def _remove_list_references(sentence: str) -> str: ...
def is_valid_sentence(value: list[str]) -> list[str]: ...
def has_one_non_empty_item(value: list[str]) -> list[str]: ...

_media_id_validator: Incomplete

@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
