from .entity_store_schema import KNX_SCHEMA_FOR_PLATFORM as KNX_SCHEMA_FOR_PLATFORM
from .knx_selector import AllSerializeFirst as AllSerializeFirst, GroupSelectSchema as GroupSelectSchema, KNXSelectorBase as KNXSelectorBase
from homeassistant.const import Platform as Platform
from homeassistant.helpers import selector as selector
from typing import Any

def knx_serializer(schema: Any) -> Any: ...
def get_serialized_schema(platform: Platform) -> dict[str, Any] | list[dict[str, Any]] | None: ...
