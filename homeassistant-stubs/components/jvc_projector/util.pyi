from .const import DOMAIN as DOMAIN
from homeassistant.components.automation import automations_with_entity as automations_with_entity
from homeassistant.components.script import scripts_with_entity as scripts_with_entity
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import entity_registry as er
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue, async_delete_issue as async_delete_issue

def deprecate_entity(hass: HomeAssistant, entity_registry: er.EntityRegistry, platform_domain: str, entity_unique_id: str, issue_id: str, issue_string: str, replacement_entity_unique_id: str, replacement_entity_id: str, version: str = '2026.9.0') -> bool: ...
def get_automations_and_scripts_using_entity(hass: HomeAssistant, entity_id: str) -> list[str]: ...
