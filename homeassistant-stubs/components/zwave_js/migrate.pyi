from .const import DOMAIN as DOMAIN
from .discovery import ZwaveDiscoveryInfo as ZwaveDiscoveryInfo
from .helpers import get_unique_id as get_unique_id
from homeassistant.core import callback as callback
from homeassistant.helpers.entity_registry import EntityRegistry as EntityRegistry
from typing import Any
from zwave_js_server.client import Client as ZwaveClient
from zwave_js_server.model.value import Value as ZwaveValue

_LOGGER: Any

def async_migrate_entity(ent_reg: EntityRegistry, platform: str, old_unique_id: str, new_unique_id: str) -> None: ...
def async_migrate_discovered_value(ent_reg: EntityRegistry, client: ZwaveClient, disc_info: ZwaveDiscoveryInfo) -> None: ...
def get_old_value_ids(value: ZwaveValue) -> list[str]: ...
