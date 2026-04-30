from .const import CREDENTIAL_RULE_MAP as CREDENTIAL_RULE_MAP, CREDENTIAL_RULE_REVERSE_MAP as CREDENTIAL_RULE_REVERSE_MAP, CREDENTIAL_TYPE_MAP as CREDENTIAL_TYPE_MAP, CREDENTIAL_TYPE_REVERSE_MAP as CREDENTIAL_TYPE_REVERSE_MAP, CRED_TYPE_FACE as CRED_TYPE_FACE, CRED_TYPE_FINGERPRINT as CRED_TYPE_FINGERPRINT, CRED_TYPE_FINGER_VEIN as CRED_TYPE_FINGER_VEIN, CRED_TYPE_PIN as CRED_TYPE_PIN, CRED_TYPE_RFID as CRED_TYPE_RFID, LOCK_TIMED_REQUEST_TIMEOUT_MS as LOCK_TIMED_REQUEST_TIMEOUT_MS, USER_STATUS_MAP as USER_STATUS_MAP, USER_STATUS_REVERSE_MAP as USER_STATUS_REVERSE_MAP, USER_TYPE_MAP as USER_TYPE_MAP, USER_TYPE_REVERSE_MAP as USER_TYPE_REVERSE_MAP
from _typeshed import Incomplete
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, ServiceValidationError as ServiceValidationError
from matter_server.client import MatterClient as MatterClient
from matter_server.client.models.node import MatterEndpoint as MatterEndpoint, MatterNode as MatterNode
from typing import Any, TypedDict

ERR_CREDENTIAL_TYPE_NOT_SUPPORTED: str
ERR_INVALID_CREDENTIAL_DATA: str
_DlStatus: Incomplete
SET_CREDENTIAL_STATUS_MAP: dict[int, str]
DoorLockFeature: Incomplete

class LockUserCredentialData(TypedDict):
    type: str
    index: int | None

class LockUserData(TypedDict):
    user_index: int | None
    user_name: str | None
    user_unique_id: int | None
    user_status: str
    user_type: str
    credential_rule: str
    credentials: list[LockUserCredentialData]
    creator_fabric_index: int | None
    last_modified_fabric_index: int | None
    next_user_index: int | None

class SetLockUserResult(TypedDict):
    user_index: int

class GetLockUsersResult(TypedDict):
    max_users: int
    users: list[LockUserData]

class GetLockInfoResult(TypedDict):
    supports_user_management: bool
    supported_credential_types: list[str]
    max_users: int | None
    max_pin_users: int | None
    max_rfid_users: int | None
    max_credentials_per_user: int | None
    min_pin_length: int | None
    max_pin_length: int | None
    min_rfid_length: int | None
    max_rfid_length: int | None

class SetLockCredentialResult(TypedDict):
    credential_index: int
    user_index: int | None
    next_credential_index: int | None

class GetLockCredentialStatusResult(TypedDict):
    credential_exists: bool
    user_index: int | None
    creator_fabric_index: int | None
    last_modified_fabric_index: int | None
    next_credential_index: int | None

def _get_lock_endpoint_from_node(node: MatterNode) -> MatterEndpoint | None: ...
def _get_feature_map(endpoint: MatterEndpoint) -> int | None: ...
def _lock_supports_usr_feature(endpoint: MatterEndpoint) -> bool: ...
def _get_attr(obj: Any, attr: str) -> Any: ...
def _get_supported_credential_types(feature_map: int) -> list[str]: ...
def _format_user_response(user_data: Any) -> LockUserData | None: ...

class LockEndpointNotFoundError(HomeAssistantError): ...
class UsrFeatureNotSupportedError(ServiceValidationError): ...
class UserSlotEmptyError(ServiceValidationError): ...
class NoAvailableUserSlotsError(ServiceValidationError): ...
class CredentialTypeNotSupportedError(ServiceValidationError): ...
class CredentialDataInvalidError(ServiceValidationError): ...
class SetCredentialFailedError(HomeAssistantError): ...

def _get_lock_endpoint_or_raise(node: MatterNode) -> MatterEndpoint: ...
def _ensure_usr_support(lock_endpoint: MatterEndpoint) -> None: ...
async def get_lock_info(matter_client: MatterClient, node: MatterNode) -> GetLockInfoResult: ...
async def set_lock_user(matter_client: MatterClient, node: MatterNode, *, user_index: int | None = None, user_name: str | None = None, user_unique_id: int | None = None, user_status: str | None = None, user_type: str | None = None, credential_rule: str | None = None) -> SetLockUserResult: ...
async def get_lock_users(matter_client: MatterClient, node: MatterNode) -> GetLockUsersResult: ...
async def clear_lock_user(matter_client: MatterClient, node: MatterNode, user_index: int) -> None: ...

_CREDENTIAL_TYPE_FEATURE_MAP: dict[str, int]
_CREDENTIAL_TYPE_CAPACITY_ATTR: Incomplete

def _validate_credential_type_support(lock_endpoint: MatterEndpoint, credential_type: str) -> None: ...
def _validate_credential_data(lock_endpoint: MatterEndpoint, credential_type: str, credential_data: str) -> None: ...
def _credential_data_to_bytes(credential_type: str, credential_data: str) -> bytes: ...
async def set_lock_credential(matter_client: MatterClient, node: MatterNode, *, credential_type: str, credential_data: str, credential_index: int | None = None, user_index: int | None = None, user_status: str | None = None, user_type: str | None = None) -> SetLockCredentialResult: ...
async def clear_lock_credential(matter_client: MatterClient, node: MatterNode, *, credential_type: str, credential_index: int) -> None: ...
async def get_lock_credential_status(matter_client: MatterClient, node: MatterNode, *, credential_type: str, credential_index: int) -> GetLockCredentialStatusResult: ...
