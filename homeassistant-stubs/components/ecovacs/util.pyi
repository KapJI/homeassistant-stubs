from .controller import EcovacsController as EcovacsController
from .entity import EcovacsCapabilityEntityDescription as EcovacsCapabilityEntityDescription, EcovacsDescriptionEntity as EcovacsDescriptionEntity, EcovacsEntity as EcovacsEntity
from collections.abc import Mapping
from enum import Enum
from homeassistant.const import CONF_DEVICE_ID as CONF_DEVICE_ID
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.util import slugify as slugify
from typing import Any

def get_client_device_id(hass: HomeAssistant, self_hosted: bool, config: Mapping[str, Any]) -> str: ...
def get_supported_entities(controller: EcovacsController, entity_class: type[EcovacsDescriptionEntity], descriptions: tuple[EcovacsCapabilityEntityDescription, ...]) -> list[EcovacsEntity]: ...
@callback
def get_name_key(enum: Enum) -> str: ...
@callback
def get_options(enum: type[Enum]) -> list[str]: ...
