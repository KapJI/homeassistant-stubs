from .const import CONF_ENERGYID_KEY as CONF_ENERGYID_KEY, CONF_HA_ENTITY_UUID as CONF_HA_ENTITY_UUID, DOMAIN as DOMAIN, NAME as NAME
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigSubentryFlow as ConfigSubentryFlow, SubentryFlowResult as SubentryFlowResult
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import entity_registry as er
from homeassistant.helpers.selector import EntitySelector as EntitySelector, EntitySelectorConfig as EntitySelectorConfig
from typing import Any

_LOGGER: Incomplete

@callback
def _get_suggested_entities(hass: HomeAssistant) -> list[str]: ...
@callback
def _validate_mapping_input(ha_entity_id: str | None, current_mappings: set[str], ent_reg: er.EntityRegistry) -> dict[str, str]: ...

class EnergyIDSensorMappingFlowHandler(ConfigSubentryFlow):
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> SubentryFlowResult: ...
