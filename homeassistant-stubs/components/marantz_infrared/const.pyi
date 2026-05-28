from homeassistant.util import slugify as slugify
from infrared_protocols.codes.marantz import models as marantz_models

DOMAIN: str
CONF_INFRARED_EMITTER_ENTITY_ID: str
MODELS: dict[str, marantz_models.MarantzModel]
