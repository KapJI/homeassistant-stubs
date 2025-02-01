from .agent import BackupAgent as BackupAgent, BackupAgentError as BackupAgentError, BackupAgentPlatformProtocol as BackupAgentPlatformProtocol, LocalBackupAgent as LocalBackupAgent
from .manager import BackupManager, BackupManagerError as BackupManagerError, BackupPlatformProtocol as BackupPlatformProtocol, BackupReaderWriter as BackupReaderWriter, BackupReaderWriterError as BackupReaderWriterError, CreateBackupEvent as CreateBackupEvent, IdleEvent as IdleEvent, IncorrectPasswordError as IncorrectPasswordError, ManagerBackup as ManagerBackup, NewBackup as NewBackup, RestoreBackupEvent as RestoreBackupEvent, RestoreBackupState as RestoreBackupState, WrittenBackup as WrittenBackup
from .models import AddonInfo as AddonInfo, AgentBackup as AgentBackup, Folder as Folder
from .util import suggested_filename as suggested_filename, suggested_filename_from_name_date as suggested_filename_from_name_date
from homeassistant.core import HomeAssistant, callback

__all__ = ['AddonInfo', 'AgentBackup', 'BackupAgent', 'BackupAgentError', 'BackupAgentPlatformProtocol', 'BackupManagerError', 'BackupPlatformProtocol', 'BackupReaderWriter', 'BackupReaderWriterError', 'CreateBackupEvent', 'Folder', 'IdleEvent', 'IncorrectPasswordError', 'LocalBackupAgent', 'ManagerBackup', 'NewBackup', 'RestoreBackupEvent', 'RestoreBackupState', 'WrittenBackup', 'async_get_manager', 'suggested_filename', 'suggested_filename_from_name_date']

@callback
def async_get_manager(hass: HomeAssistant) -> BackupManager: ...
