from .const import CREDENTIAL_RULE_DUAL as CREDENTIAL_RULE_DUAL, CREDENTIAL_RULE_SINGLE as CREDENTIAL_RULE_SINGLE, CREDENTIAL_RULE_TRIPLE as CREDENTIAL_RULE_TRIPLE, CREDENTIAL_TYPE_BLE as CREDENTIAL_TYPE_BLE, CREDENTIAL_TYPE_DESFIRE as CREDENTIAL_TYPE_DESFIRE, CREDENTIAL_TYPE_EYE_BIOMETRIC as CREDENTIAL_TYPE_EYE_BIOMETRIC, CREDENTIAL_TYPE_FACE_BIOMETRIC as CREDENTIAL_TYPE_FACE_BIOMETRIC, CREDENTIAL_TYPE_FINGER_BIOMETRIC as CREDENTIAL_TYPE_FINGER_BIOMETRIC, CREDENTIAL_TYPE_HAND_BIOMETRIC as CREDENTIAL_TYPE_HAND_BIOMETRIC, CREDENTIAL_TYPE_NFC as CREDENTIAL_TYPE_NFC, CREDENTIAL_TYPE_PASSWORD as CREDENTIAL_TYPE_PASSWORD, CREDENTIAL_TYPE_PIN_CODE as CREDENTIAL_TYPE_PIN_CODE, CREDENTIAL_TYPE_RFID_CODE as CREDENTIAL_TYPE_RFID_CODE, CREDENTIAL_TYPE_UNSPECIFIED_BIOMETRIC as CREDENTIAL_TYPE_UNSPECIFIED_BIOMETRIC, CREDENTIAL_TYPE_UWB as CREDENTIAL_TYPE_UWB, DOMAIN as DOMAIN, USER_TYPE_DISPOSABLE as USER_TYPE_DISPOSABLE, USER_TYPE_DURESS as USER_TYPE_DURESS, USER_TYPE_EXPIRING as USER_TYPE_EXPIRING, USER_TYPE_GENERAL as USER_TYPE_GENERAL, USER_TYPE_NON_ACCESS as USER_TYPE_NON_ACCESS, USER_TYPE_PROGRAMMING as USER_TYPE_PROGRAMMING, USER_TYPE_REMOTE_ONLY as USER_TYPE_REMOTE_ONLY
from _typeshed import Incomplete
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, ServiceValidationError as ServiceValidationError
from typing import TypedDict
from zwave_js_server.const.command_class.access_control import SetCredentialResult, SetUserResult, UserCredentialRule, UserCredentialType, UserCredentialUserType
from zwave_js_server.model.node import Node as Node

_LOGGER: Incomplete
CREDENTIAL_TYPE_MAP: dict[UserCredentialType, str]
CREDENTIAL_TYPE_REVERSE_MAP: dict[str, UserCredentialType]
USER_TYPE_MAP: dict[UserCredentialUserType, str]
USER_TYPE_REVERSE_MAP: dict[str, UserCredentialUserType]
CREDENTIAL_RULE_MAP: dict[UserCredentialRule, str]
CREDENTIAL_RULE_REVERSE_MAP: dict[str, UserCredentialRule]
_SET_USER_RESULT_KEYS: dict[SetUserResult, str]
_SET_CREDENTIAL_RESULT_KEYS: dict[SetCredentialResult, str]

def _raise_on_set_user_error(status: SetUserResult) -> None: ...
def _raise_on_set_credential_error(status: SetCredentialResult) -> None: ...

class CredentialTypeCapability(TypedDict):
    num_slots: int
    min_length: int
    max_length: int
    supports_learn: bool

class CredentialCapabilitiesResult(TypedDict):
    supports_user_management: bool
    max_users: int
    supported_user_types: list[str]
    max_user_name_length: int
    supported_credential_rules: list[str]
    supported_credential_types: dict[str, CredentialTypeCapability]

class Credential(TypedDict):
    type: str
    slot: int

class UserEntry(TypedDict):
    user_id: int
    user_name: str | None
    active: bool
    user_type: str
    credential_rule: str | None
    credentials: list[Credential]

class UsersResult(TypedDict):
    max_users: int
    users: list[UserEntry]

class SetUserReturn(TypedDict):
    user_id: int

class SetCredentialReturn(TypedDict):
    credential_slot: int
    user_id: int

async def async_get_credential_capabilities(node: Node) -> CredentialCapabilitiesResult: ...
async def async_get_users(node: Node) -> UsersResult: ...
async def async_set_user(node: Node, user_id: int | None = None, user_name: str | None = None, user_type: UserCredentialUserType | None = None, credential_rule: UserCredentialRule | None = None, active: bool | None = None) -> SetUserReturn: ...
async def async_delete_user(node: Node, user_id: int) -> None: ...
async def async_delete_all_users(node: Node) -> None: ...
async def async_set_credential(node: Node, user_id: int, credential_type: UserCredentialType, credential_data: str, credential_slot: int | None = None) -> SetCredentialReturn: ...
async def async_delete_credential(node: Node, user_id: int, credential_type: UserCredentialType, credential_slot: int) -> None: ...
async def async_delete_all_credentials(node: Node, user_id: int) -> None: ...
